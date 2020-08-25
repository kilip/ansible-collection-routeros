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


class Resources(ConfigBase):
    """
    Base class for single network resource
    """

    gather_subset = ["!all", "!min"]
    resource = ""
    resource_facts_command = ""

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
        pass

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param obj_in_have: the current configuration as a dictionary
        :param interface_type: interface type
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []

        if want:
            for resource in want:
                for each in have:
                    if each["name"] == resource["name"]:
                        break
                else:
                    continue
                resource = dict(name=resource["name"])
                commands.extend(self.do_delete(resource, each))
        else:
            for each in have:
                want = dict()
                commands.extend(self.do_delete(want, each))
        return commands

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []

        for resource in want:
            for each in have:
                if each["name"] == resource["name"]:
                    break
            else:
                # configuring non-existing interface
                commands.extend(self.do_set_config(resource, dict()))
                continue
            commands.extend(self.do_set_config(resource, each))
        return commands

    def _state_replaced(self, want, have):
        pass

    @abstractmethod
    def do_set_config(self, want, have):
        pass

    @abstractmethod
    def do_delete(self, want, have):
        pass
