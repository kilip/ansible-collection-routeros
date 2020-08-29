#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: routeros_bridge
author: Anthonius Munthi @(kilip)
short_description: RouterOS Bridges Module
description:
- This module manages routeros bridges configuration
version_added: 1.0.0
options:
  name:
    description:
    type:
  state:

"""
EXAMPLES = """

"""
RETURN = """
"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.config.resource import ResourceConfig
from ..module_utils.resources.bridge import BridgeResource


def main():
    module = AnsibleModule(
        argument_spec=BridgeResource.argument_spec, supports_check_mode=True
    )
    result = ResourceConfig(module, BridgeResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
