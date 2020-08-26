from __future__ import absolute_import, division, print_function

__metaclass__ = type

from abc import abstractmethod
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)

from ..facts.facts import Facts
from ..routeros import (
    load_config
)
from ..utils import (
    filter_dict_having_none_value,
    generate_command_values
)

class ConfigResource(ConfigBase):

    def __init__(
        self,
        module,
        resource
    ):
        super(ConfigResource, self).__init__(module)
        self.resource = resource

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
        resource = self.resource

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
            self._remove_invalid(existing)

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
            have_dict = filter_dict_having_none_value(resource, existing)
            # TODO: add clear config for certain network resource
            # commands.extend(self._clear_config(dict(), have_dict))
            if existing:
                commands.extend(self._delete(have_dict))
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
                if each[key] != want[key]:
                    exist = False
            if exist:
                resource = each
        return resource

    def _create_find_command(self, want):
        keys = self.resource.resource_keys
        finds = []
        for key in keys:
            finds.append(key + "=" + want[key])
        return "[ find %s ]" % (" and ".join(finds))

    def _configure(self, want, have):
        commands = []
        resource = self.resource
        command_prefix = self.get_command_prefix(want, have)
        prefix = f"%s add " % command_prefix
        filters = resource.value_filters
        if have:
            find_command = self._create_find_command(want)
            prefix = f"%s set %s " % (command_prefix,find_command)
            filters.extend(resource.resource_keys)

        values = generate_command_values(want, have, filters)
        if values:
            cmd = prefix + " ".join(values)
            commands.append(cmd)
        return commands

    def _delete(self, want, have):
        commands = []
        prefix = self.get_command_prefix(want, have)
        find_command = self._create_find_command(want)
        cmd = f'%s remove %s' % (prefix, find_command)
        commands.append(cmd)
        commands.extend(self._remove_related_resource(want, have))
        return commands

    def _remove_related_resource(self, want, have):
        commands = []
        return commands

    def get_command_prefix(self, want, have):
        prefix = self.resource.command_root
        return prefix
