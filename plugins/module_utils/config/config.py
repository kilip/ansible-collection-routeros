from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)

from ..facts.facts import Facts
from ..routeros import load_config, get_config
from ..utils import (
    generate_command_values,
    gen_remove_invalid_resource,
    ANSIBLE_REMOVE_INVALID_SCRIPT_NAME,
)


class Config(ConfigBase):

    has_delete_command = False

    def __init__(self, module, resource):
        ConfigBase.__init__(self, module)
        self.resource = resource()

    def get_resource_facts(self, data=None):
        resource = self.resource
        facts, _warning = Facts(self._module).get_facts(
            resource.gather_subset, resource.gather_network_resources, data
        )
        resource_facts = facts["ansible_network_resources"].get(
            resource.resource_name
        )
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

    def add(self, want):
        resource = self.resource
        commands = []
        command_prefix = self.get_command_prefix(want)
        prefix = f"{command_prefix} add "

        # always remove default values for new resource
        defaults = resource.generate_dict()
        values = generate_command_values(want, defaults, [], resource.prefixes)
        if values:
            cmd = prefix + " ".join(values)
            commands.append(cmd)
        return commands

    def update(self, want, have):
        resource = self.resource
        find_command = self._create_find_command(want)
        command_prefix = self.get_command_prefix(want, have)
        prefix = f"{command_prefix} set {find_command} "
        commands = []
        filters = resource.keys
        for filter in resource.filters:
            filters.append(filter)

        # start generating values
        values = generate_command_values(
            want, have, filters, resource.prefixes
        )
        if values:
            cmd = prefix + " ".join(values)
            commands.append(cmd)
        return commands

    def delete(self, want):
        commands = []
        prefix = self.get_command_prefix(want)
        find_command = self._create_find_command(want)
        cmd = f"{prefix} remove {find_command}"
        commands.append(cmd)

        self.has_delete_command = True

        return commands

    def get_command_prefix(self, want, have=None):
        prefix = self.resource.get_command_prefix(want, have)
        return prefix

    def _inject_script(self):
        """
        Inject ansible-remove-invalid scripts into routeros
        :return generated inject script
        """
        script_name = ANSIBLE_REMOVE_INVALID_SCRIPT_NAME
        existing = get_config(self._module, "/system script export terse")
        lines = [
            ':log info \\"ansible: remove invalid config";',
            "/ip address remove [find invalid];",
            "/ip dhcp-server remove [find invalid];",
        ]
        scripts = "".join(lines)
        commands = f'/system script add name={script_name} policy=read,write source="{scripts}"'
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
            commands.extend(self.delete(existing))

        for resource in want:
            commands.extend(self.add(resource))

        if self.has_delete_command:
            cmd = gen_remove_invalid_resource()
            commands.append(cmd)

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
                if existing is not None:
                    commands.extend(self.delete(existing))
        else:
            for each in have:
                commands.extend(self.delete(each))

        if self.has_delete_command:
            cmd = gen_remove_invalid_resource()
            commands.append(cmd)
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
            if existing is None:
                commands.extend(self.add(resource))
            else:
                commands.extend(self.update(resource, existing))

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
        resource = self.resource

        for each in want:
            existing = self._find_resource(each, have)
            if existing is None:
                commands.extend(self.add(each))
            else:
                commands.extend(self._clear_config(existing))
                # new = self._create_empty_resource(existing)
                defaults = resource.generate_dict()
                commands.extend(self.update(each, defaults))

        return commands

    def _create_empty_resource(self, existing):
        """
        Create empty resource to be used in replaced state
        :param existing: existing resource config
        :return: the new config with resource keys only
        """
        new = dict()
        resource = self.resource
        for key in resource.keys:
            new[key] = existing[key]
        return new

    def _clear_config(self, existing):
        """
        Replace existing resource configuration with it's default values
        :param existing: resource config
        :rtype str
        :return: default resource configuration command
        """
        resource = self.resource
        defaults = resource.generate_dict()
        want = defaults
        empty_resource = self._create_empty_resource(existing)
        want.update(empty_resource)
        spec = resource.facts_argument_spec

        # remove required option from clear config
        for key in spec:
            if key in resource.keys:
                continue
            option = spec[key]
            required = option.get("required")
            if required is True:
                del want[key]
                del existing[key]

        cmd = self.update(want, existing)
        return cmd

    def _find_resource(self, want, have):
        """
        Find existing resource
        :param want: a configure
        :param have:
        :return:
        """
        keys = self.resource.keys
        resource = None
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
        keys = self.resource.keys
        finds = []
        for key in keys:
            if want.get(key) is None:
                continue
            finds.append(key.replace("_", "-") + "=" + want[key])
        return "[ find %s ]" % (" and ".join(finds))
