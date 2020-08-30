#!/usr/bin/python


"""
The module file for ros_address_list
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_address_list
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
            - I(merged) M(ros_address_list) will update existing C(/ip firewall address-list) configuration, or create new C(/ip firewall address-list) when resource not found
            - I(replaced) M(ros_address_list) will restore existing C(/ip firewall address-list) configuration to its default value, then update existing resource with the new configuration. If the resource C(/ip firewall address-list) not found, M(ros_address_list) will create resource in C(/ip firewall address-list)
            - I(overridden) M(ros_address_list) will remove any resource in C(/ip firewall address-list) first, and then create new C(/ip firewall address-list) resources.
            - I(deleted) M({module}) when found module will delete C(/ip firewall address-list)
    config:
        description: A dictionary for L(ros_address_list)
        type: list
        elements: dict
        suboptions:
            address:
                type: str
                required: True
                description: |
                    A single IP address or range of IPs to add to address list or DNS name. You can input for example, 192.168.0.0-192.168.1.255 and it will auto modify the typed entry to 192.168.0.0/23 on saving.
            list:
                type: str
                required: True
                description: |
                    Name for the address list of the added IP address
            timeout:
                type: str
                description: |
                    Time after address will be removed from address list. If timeout is not specified, the address will be stored into the address list permanently.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.firewall.address_list import AddressListResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=AddressListResource.argument_spec)
    result = ResourceConfig(module, AddressListResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
