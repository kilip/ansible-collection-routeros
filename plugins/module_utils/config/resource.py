from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)

from ..resource.base import ResourceBase
from ..facts.facts import Facts
from ..routeros import (
    load_config,
    get_config,
)
from ..utils import (
    generate_command_values,
    gen_remove_invalid_resource,
    ANSIBLE_REMOVE_INVALID_SCRIPT_NAME
)


class ConfigResource(ConfigBase):

    resource = ResourceBase

    def get_resource_facts(self, data=None):
        resource = self.resource
        facts, _warning = Facts(self._module).get_facts(
            resource.gather_subset,
            resource.gather_network_resources,
            data
        )
        resource_facts = facts['ansible_network_resources'].get(resource.resource_name)
        if not resource_facts:
            return []
        return resource_facts

    def execute_module(self):
        result = {"changed": False}
        commands = list()
        warnings = list()

        self._inject_script()

        existing_resource_facts = []
        if self.state in self.ACTION_STATES:
            existing_resource_facts = self.get_resource_facts()

        if self.state in self.ACTION_STATES:
            commands.extend(self._set_config(existing_resource_facts))

        changed_resource_facts = []
        if commands and self.state in self.ACTION_STATES:
            if not self._module.check_mode:
                load_config(self._module, commands)
            result["changed"] = True

        if self.state in self.ACTION_STATES:
            result["commands"] = commands

        if self.state in self.ACTION_STATES:
            changed_resource_facts = self.get_resource_facts()

        if self.state in self.ACTION_STATES:
            result["before"] = existing_resource_facts
            if result["changed"]:
                result["after"] = changed_resource_facts

        result["warnings"] = warnings
        return result

    def _inject_script(self):
        """
        Inject ansible-remove-invalid scripts into routeros
        :return generated inject script
        """
        script_name = ANSIBLE_REMOVE_INVALID_SCRIPT_NAME
        existing = get_config(self._module, '/system script export terse')
        lines = [
            ":global ansiblerminterface;",
            ":log info \\\"ansible: remove invalid config for interface: \\$ansiblerminterface\\\";",
            "/ip address remove [find invalid];",
            "/ip dhcp-server remove [find invalid];"
        ]
        scripts = "".join(lines)
        commands = f"/system script add name={script_name} policy=read,write source=\"{scripts}\""
        match = re.search(r"name\=" + script_name, existing, re.M)
        if not match:
            load_config(self._module, commands)

    def _set_config(self, existing):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the deisred configuration
        """
        config = self._module.params.get("config")
        want = []
        if config:
            for each in config:
                want.append(each)
        have = existing
        resp = self._set_state(want, have)
        return to_list(resp)

    def _set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the deisred configuration
        """
        commands = []

        if (
            self.state in ("overridden", "merged", "replaced", "rendered")
            and not want
        ):
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    self.state
                )
            )

        if self.state == "overridden":
            commands = self._state_overridden(want, have)
        elif self.state == "deleted":
            commands = self._state_deleted(want, have)
        elif self.state == "merged" or self.state == "rendered":
            commands = self._state_merged(want, have)
        elif self.state == "replaced":
            commands = self._state_replaced(want, have)

        return commands

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []

        for existing in have:
            commands.extend(self._delete(existing))

        for resource in want:
            commands.extend(self._configure(resource, dict()))

        return commands

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param have: the existing configuration
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []

        if want:
            for resource in want:
                existing = self._find_resource(resource, have)
                commands.extend(self._delete(existing))
        else:
            for each in have:
                commands.extend(self._delete(each))
        return commands

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []

        for resource in want:
            existing = self._find_resource(resource, have)
            commands.extend(self._configure(resource, existing))
        return commands

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :param interface_type: interface type
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the deisred configuration
        """
        commands = []

        for resource in want:
            existing = self._find_resource(resource, have)
            # have_dict = filter_dict_having_none_value(resource, existing)
            # TODO: add clear config for certain network resource
            # commands.extend(self._clear_config(dict(), have_dict))
            if existing:
                commands.extend(self._delete(resource))
            commands.extend(self._configure(resource, dict()))
        return commands

    def _find_resource(self, want, have):
        """
        Find existing resource
        :param want: a configure
        :param have:
        :return:
        """
        keys = self.resource.resource_keys
        resource = dict()
        for each in have:
            exist = True
            for key in keys:
                if each.get(key) is None:
                    exist = False
                    continue
                if each[key] != want[key]:
                    exist = False
            if exist:
                resource = each
        return resource

    def _create_find_command(self, want):
        keys = self.resource.resource_keys
        finds = []
        for key in keys:
            if want.get(key) is None:
                continue
            finds.append(key + "=" + want[key])
        return "[ find %s ]" % (" and ".join(finds))

    def _configure(self, want, have):
        commands = []
        resource = self.resource
        command_prefix = self.get_command_prefix(want, have)
        prefix = f"{command_prefix} add "
        filters = resource.value_filters
        if have:
            find_command = self._create_find_command(want)
            prefix = f"{command_prefix} set {find_command} "
            filters.extend(resource.resource_keys)

        values = generate_command_values(want, have, filters)
        if values:
            cmd = prefix + " ".join(values)
            commands.append(cmd)
        return commands

    def _delete(self, want):
        commands = []
        prefix = self.get_command_prefix(want)
        find_command = self._create_find_command(want)
        cmd = f"{prefix} remove {find_command}"
        commands.append(cmd)

        if self.resource.remove_related_resource:
            key = self.resource.related_resource_key
            if want.get(key) is not None:
                name = want[key]
                cmd = gen_remove_invalid_resource(name)
                commands.append(cmd)
        return commands

    def get_command_prefix(self, want, have=None):
        prefix = self.resource.command_root
        return prefix
