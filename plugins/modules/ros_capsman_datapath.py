#!/usr/bin/python


"""
The module file for ros_capsman_datapath
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_capsman_datapath
short_description: Manage configuration for C(/caps-man datapath)
description: This M(ros_capsman_datapath) module provides management for RouterOS C(/caps-man datapath).
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
    state:
        choices:
            - merged
            - replaced
            - overridden
            - deleted
        default: merged
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_capsman_datapath) will update existing C(/caps-man datapath) configuration
            -  When Resource Not Exists:
               *  M(ros_capsman_datapath) will create new C(/caps-man datapath),
            Replaced
            -  When Resource Exists:
               *  M(ros_capsman_datapath) will restore related C(/caps-man datapath) to its default value.
               *  M(ros_capsman_datapath) will update C(/caps-man datapath) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_capsman_datapath) will create new C(/caps-man datapath)
            Overridden:
            *  M(ros_capsman_datapath) will remove any existing item in C(/caps-man datapath)
            *  M(ros_capsman_datapath) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_capsman_datapath) will remove that item from C(/caps-man datapath) configuration
    config:
        description: A dictionary for L(ros_capsman_datapath)
        type: list
        elements: dict

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.capsman.datapath import CapsmanDatapathResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=CapsmanDatapathResource.argument_spec)
    result = ResourceConfig(module, CapsmanDatapathResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
