#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_facts
short_description: Gather facts for routeros configuration
description: This M(ros_facts) module provides gathering facts for RouterOS.
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
  gather_subset:
    description:
    - When supplied, this argument restricts the facts collected to a given subset.
    - Possible values for this argument include C(all), C(min), C(interface)
    - Specify a list of values to include a larger subset.
    - Use a value with an initial C(!) to collect all facts except that subset.
    required: false
    default: '!config'
    type: list
    elements: str
  gather_network_resources:
    description:
    - When supplied, this argument will restrict the facts collected to a given subset.
      Possible values for this argument include all and the resources like interfaces,
      vlans etc. Can specify a list of values to include a larger subset. Values can
      also be used with an initial C(M(!)) to specify that a specific subset should
      not be collected. Valid subsets are 'all', 'interface'
    type: list
    elements: str
"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.facts.facts import Facts


def main():
    argument_spec = {
        "gather_subset": dict(
            default=["!config"], type="list", elements="str"
        ),
        "gather_network_resources": dict(type="list", elements="str"),
    }
    warnings = []
    module = AnsibleModule(argument_spec=argument_spec)

    result = Facts(module).get_facts()
    ansible_facts, additional_warnings = result
    warnings.extend(additional_warnings)
    return module.exit_json(ansible_facts=ansible_facts, warnings=warnings)


if __name__ == "__main__":
    main()
