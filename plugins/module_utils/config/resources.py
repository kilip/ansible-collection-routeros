from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ..connection import (
    load_config,
)

from abc import abstractmethod
from ..facts.facts import Facts

from ..utils import (
    generate_command_values,
    filter_dict_having_none_value,
)

class Resources(ConfigBase):
    """
    Base class for network resources
    """

    gather_subset = ["!all", "!min"]
    resource = ""
    resource_facts_command = ""
    resource_keys = ["name"]
    config_root = ""

    def __init__(
        self,
        module,
        resource,
        resource_facts_command
    ):
        super(Resources, self).__init__(module)
        self.resource = resource
        self.resource_facts_command = resource_facts_command

    def get_resource_facts(self, data=None):
        facts, _warning = Facts(self._module).get_facts(
            self.gather_subset,
            [self.resource],
            data
        )
        resource_facts = facts['ansible_network_resources'].get(self.resource)
        if not resource_facts:
            return []
        return resource_facts

    def execute_module(self):
        result = {"changed": False}
        commands = list()
        warnings = list()

        existing_resource_facts = []
        if self.state in self.ACTION_STATES:
            existing_resource_facts = self.get_resource_facts()

        if self.state in self.ACTION_STATES:
            commands.extend(self._set_config(existing_resource_facts))

        changed_resource_facts = []
        if commands and self.state in self.ACTION_STATES:
            if not self._module.check_mode:
                load_config(self._module, commands, self.resource_facts_command)
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
        keys = self.resource_keys
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
        keys = self.resource_keys
        finds = []
        for key in keys:
            finds.append(key + "=" + want[key])
        return "[ find %s ]" % (" and ".join(finds))

    def _configure(self, want, have):
        commands = []
        config_root = self.config_root
        prefix = f"%s add " % config_root
        filters = []
        if have:
            find_command = self._create_find_command(want)
            prefix = f"%s set %s " % (config_root,find_command)
            filters = self.resource_keys

        values = generate_command_values(want, have, filters)
        if values:
            cmd = prefix + " ".join(values)
            commands.append(cmd)
        return commands

    def _delete(self, resource):
        commands = []
        config_root = self.config_root
        find_command = self._create_find_command(resource)
        cmd = f'%s remove %s' % (config_root, find_command)
        commands.append(cmd)
        return commands

    def _remove_invalid(self, existing):
        return []
