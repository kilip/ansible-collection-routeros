#!/usr/bin/python


"""
The module file for ros_capsman_datapath
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_capsman_datapath
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
        description:
            - I(merged) M(ros_capsman_datapath) will update existing C(/caps-man datapath) configuration, or create new C(/caps-man datapath) when resource not found
            - I(replaced) M(ros_capsman_datapath) will restore existing C(/caps-man datapath) configuration to its default value, then update existing resource with the new configuration. If the resource C(/caps-man datapath) not found, M(ros_capsman_datapath) will create resource in C(/caps-man datapath)
            - I(overridden) M(ros_capsman_datapath) will remove any resource in C(/caps-man datapath) first, and then create new C(/caps-man datapath) resources.
            - I(deleted) M({module}) when found module will delete C(/caps-man datapath)
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
