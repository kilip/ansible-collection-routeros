from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..facts.facts import Facts
from ..routeros import load_config


class Setting(object):
    """
    Class to handle RouterOS Configuration
    """

    def __init__(self, module, resource):
        """
        Initialize new object
        """
        self._module = module
        self._resource = resource()
        self.state = module.params["state"]

    def get_resource_facts(self, data=None):
        resource = self._resource
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
        warnings = list()
        existing = self.get_resource_facts()
        commands = []

        commands.extend(self._configure_state(existing))

        if commands and not self._module.check_mode:
            load_config(self._module, commands)
            result["changed"] = True

        if result["changed"]:
            result["before"] = existing
            result["after"] = self.get_resource_facts()
            result["commands"] = commands

        result["warnings"] = warnings
        return result

    def _configure_state(self, existing):
        commands = []
        want = dict()
        state = self.state
        config = self._module.params.get("config")

        if config:
            want = config

        if state == "present":
            commands.extend(self._state_present(want, existing))
        else:
            commands.extend(self._state_reset(existing))

        return commands

    def _state_present(self, want, have):
        commands = []
        resource = self._resource
        prefix = resource.get_command_prefix(want, have)
        prefix = "{0} set ".format(prefix)

        values = resource.generate_command_values(want, have, [])
        values.sort()

        cmd = prefix + " ".join(values)
        commands.append(cmd)
        return commands

    def _state_reset(self, have):
        commands = []
        resource = self._resource
        want = self._resource.generate_dict()
        prefix = self._resource.get_command_prefix(want, have)
        prefix = "{0} set ".format(prefix)

        values = resource.generate_command_values(want, have, [])
        values.sort()

        cmd = prefix + " ".join(values)
        commands.append(cmd)

        return commands
