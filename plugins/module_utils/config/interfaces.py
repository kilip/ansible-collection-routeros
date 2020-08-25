from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: routeros_interfaces
short_description: Interfaces resource module
description: This module manages the interface attributes of Mikrotik RouterOS network devices.
version_added: 1.0.0
author: Anthonius Munthi <https://itstoni.com>
options:
  config:
    description: A dictionary of interface options
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - The name of interface
        type: str
        required: true
      comment:
        description:
        - Interface comment
        type: str
        required: false
      disabled:
        description:
        - Set interface disabled
        type: str
        required: false
      mtu:
        description:
        - Layer3 Maximum transmission unit
        type: int
        required: false
      l2mtu:
        description:
        - Layer2 Maximum transmission unit. Note that this property can not be configured on all interfaces.
        type: int
        required: false
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
    to_text
)
from ..facts.facts import Facts
from ..facts.interfaces import INTERFACES_FACTS_COMMAND
from ..utils import (
    dict_to_set,
    key_to_routeros,
    value_to_routeros,
)
from ..connection import (
    load_config,
    reset_config,
)


class Interfaces(ConfigBase):
    """
    The interfaces class
    """

    gather_subset = ["!all", "!min"]
    gather_network_resources = ["interfaces"]
    params = ("comment", "disabled", "l2mtu", "mtu")

    def __init__(self, module):
        super(Interfaces, self).__init__(module)

    def get_interfaces_facts(self, data=None, use_cache=True):
        """ Get the 'facts' (the current configuration)
        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources, data
        )
        interfaces_facts = facts["ansible_network_resources"].get("interfaces")
        if not interfaces_facts:
            return []

        return interfaces_facts

    def execute_module(self):
        """ Execute the module
        :rtype: A dictionary
        :returns: The result from moduel execution
        """
        result = {"changed": False}
        commands = list()
        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_interfaces_facts = self.get_interfaces_facts()
        else:
            existing_interfaces_facts = []

        if self.state in self.ACTION_STATES or self.state == "rendered":
            commands.extend(self.set_config(existing_interfaces_facts))

        if commands and self.state in self.ACTION_STATES:
            if not self._module.check_mode:
                rsp = load_config(self._module, commands)
                result["responses"] = rsp["results"]
                result["requests"] = rsp["requests"]
                reset_config(INTERFACES_FACTS_COMMAND)
            result["changed"] = True

        if self.state in self.ACTION_STATES:
            result["commands"] = commands

        changed_interfaces_facts = self.get_interfaces_facts(None, False)

        if self.state in self.ACTION_STATES:
            result["before"] = existing_interfaces_facts
            if result["changed"]:
                result["after"] = changed_interfaces_facts

        result["warnings"] = warnings
        return result

    def set_config(self, existing_interfaces_facts):
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

        have = existing_interfaces_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
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

        if self.state == "merged" or self.state == "rendered":
            commands = self._state_merged(want, have)

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

        for interface in want:
            for each in have:
                default_name = each.get('default-name')
                if each["name"] == interface["name"]:
                    break
                elif default_name and default_name == interface["name"]:
                    break
            else:
                # configuring non-existing interface
                commands.extend(self._set_config(interface, dict()))
                continue
            commands.extend(self._set_config(interface, each))

        return commands

    def _set_config(self, want, have):
        # Set the interface config based on the want and have config
        commands = []
        interface = f"/interface %s set [ find name=%s ] " % (have['type'], want['name'])

        # Get the diff b/w want and have
        want_dict = dict_to_set(want)
        have_dict = dict_to_set(have)
        diff = want_dict - have_dict

        if diff:
            diff = dict(diff)
            cmd = []
            for item in self.params:
                if diff.get(item):
                    key = key_to_routeros(item)
                    value = value_to_routeros(want.get(item))
                    cmd.append(key + "=" + value)
            command = interface + " ".join(cmd)
            commands.append(command)

        return commands
