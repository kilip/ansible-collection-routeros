#!/usr/bin/python


"""
The module file for ros_interface
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_interface
short_description: Interface Configuration
description: Configuration for I(/interface)
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
            - I(merged) M(ros_interface) will update existing C(/interface) configuration, or create new C(/interface) when resource not found
            - I(replaced) M(ros_interface) will restore existing C(/interface) configuration to its default value, then update existing resource with the new configuration. If the resource C(/interface) not found, M(ros_interface) will create resource in C(/interface)
            - I(overridden) M(ros_interface) will remove any resource in C(/interface) first, and then create new C(/interface) resources.
            - I(deleted) M({module}) when found module will delete C(/interface)
    config:
        description: A dictionary for L(ros_interface)
        type: list
        elements: dict
        suboptions:
            l2mtu:
                type: int
                description: |
                    Layer2 Maximum transmission unit. Note that this property can not be configured on all interfaces. L( Read more&gt;&gt; ,/wiki/Maximum_Transmission_Unit_on_RouterBoards)
            mtu:
                type: int
                description: |
                    Layer3 Maximum transmission unit
            name:
                type: str
                required: True
                description: |
                    Name of an interface

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.interface.interface import InterfaceResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=InterfaceResource.argument_spec)
    result = ResourceConfig(module, InterfaceResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
