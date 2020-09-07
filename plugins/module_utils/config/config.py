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
    gen_remove_invalid_resource,
    ANSIBLE_REMOVE_INVALID_SCRIPT_NAME,
    filter_dict_having_none_value,
)


class Config(ConfigBase):
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
                response = load_config(self._module, commands)
                result["response"] = response

                self._module.debug(response)
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
        existing = get_config(self._module, "/system script export terse")
        lines = [
            "/ip address remove [find invalid];",
            "/ip dhcp-server remove [find invalid];",
        ]
        scripts = "".join(lines)
        commands = '/system script add name={0} policy=read,write source="{1}"'.format(
            script_name, scripts
        )
        if isinstance(existing, list):
            existing = "\n".join(existing)
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
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        resource = self.resource

        # remove non related first
        for each in have:
            exists = self._find_resource(each, want)
            if exists is None:
                commands.extend(resource.delete(each))
            else:
                have_dict = filter_dict_having_none_value(exists, each)
                commands.extend(resource.clear_config(exists, have_dict))

        for each in want:
            exists = self._find_resource(each, have)
            if exists is None:
                commands.extend(resource.add(each))
            else:
                commands.extend(resource.update(each, exists))

        if resource.has_delete_command:
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
        resource = self.resource

        if want:
            for each in want:
                existing = self._find_resource(each, have)
                if existing is not None:
                    commands.extend(resource.delete(existing))
        else:
            for each in have:
                commands.extend(resource.delete(each))

        if resource.has_delete_command:
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
        resource = self.resource

        for each in want:
            existing = self._find_resource(each, have)
            if existing is None:
                commands.extend(resource.add(each))
            else:
                commands.extend(resource.update(each, existing))

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
                commands.extend(resource.add(each))
            else:
                have_dict = filter_dict_having_none_value(each, existing)
                commands.extend(resource.clear_config(each, have_dict))
                # new = self._create_empty_resource(existing)
                commands.extend(resource.update(each, existing))

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

        cmd = resource.update(want, existing)
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
