#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: 
author: Anthonius Munthi @(kilip)
short_description: 
description:
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
from ..module_utils.argspec.bridges import  BridgesArgs
from ..module_utils.config.bridges import Bridges

def main():
    module = AnsibleModule(
        argument_spec=BridgesArgs.argument_spec,
        supports_check_mode=True
    )
    result = Bridges(module).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
