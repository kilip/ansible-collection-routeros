#!/usr/bin/python


"""
The module file for ros_address
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_address
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
            - I(merged) M(ros_address) will update existing C(/ip address) configuration, or create new C(/ip address) when resource not found
            - I(replaced) M(ros_address) will restore existing C(/ip address) configuration to its default value, then update existing resource with the new configuration. If the resource C(/ip address) not found, M(ros_address) will create resource in C(/ip address)
            - I(overridden) M(ros_address) will remove any resource in C(/ip address) first, and then create new C(/ip address) resources.
            - I(deleted) M({module}) when found module will delete C(/ip address)
    config:
        description: A dictionary for L(ros_address)
        type: list
        elements: dict
        suboptions:
            address:
                type: str
                required: True
                description: |
                    IP address
            broadcast:
                type: str
                default: 255.255.255.255
                description: |
                    roadcasting IP address, calculated by default from an IP address and a network mask. Starting from v5RC6 this parameter is removed
            interface:
                type: str
                description: |
                    Interface name the IP address is assigned to
            netmask:
                type: str
                default: 0.0.0.0
                description: |
                    Delimits network address part of the IP address from the host part
            network:
                type: str
                default: 0.0.0.0
                description: |
                    IP address for the network. For point-to-point links it should be the address of the remote end. Starting from v5RC6 this parameter is configurable only for addresses with /32 netmask (point to point links)

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.ip.address import AddressResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=AddressResource.argument_spec)
    result = ResourceConfig(module, AddressResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
