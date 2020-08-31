#!/usr/bin/python


"""
The module file for ros_firewall_address_list
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_firewall_address_list
short_description: Manage configuration for C(/ip firewall address-list)
description: This M(ros_firewall_address_list) module provides management for RouterOS C(/ip firewall address-list).
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
               *  M(ros_firewall_address_list) will update existing C(/ip firewall address-list) configuration
            -  When Resource Not Exists:
               *  M(ros_firewall_address_list) will create new C(/ip firewall address-list),
            Replaced
            -  When Resource Exists:
               *  M(ros_firewall_address_list) will restore related C(/ip firewall address-list) to its default value.
               *  M(ros_firewall_address_list) will update C(/ip firewall address-list) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_firewall_address_list) will create new C(/ip firewall address-list)
            Overridden:
            *  M(ros_firewall_address_list) will remove any existing item in C(/ip firewall address-list)
            *  M(ros_firewall_address_list) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_firewall_address_list) will remove that item from C(/ip firewall address-list) configuration
    config:
        description: A dictionary for L(ros_firewall_address_list)
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
from ..module_utils.resources.firewall.address_list import (
    FirewallAddressListResource,
)
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(
        argument_spec=FirewallAddressListResource.argument_spec
    )
    result = ResourceConfig(
        module, FirewallAddressListResource
    ).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
