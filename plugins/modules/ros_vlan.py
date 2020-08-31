#!/usr/bin/python


"""
The module file for ros_vlan
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_vlan
short_description: VLAN Interface Configuration
description: |
    Virtual Local Area Network (VLAN) is a Layer 2 method
    that allows multiple Virtual LANs on a single physical interface (ethernet, wireless, etc.),
    giving the ability to segregate LANs efficiently.
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
               *  M(ros_vlan) will update existing C(/interface vlan) configuration
            -  When Resource Not Exists:
               *  M(ros_vlan) will create new C(/interface vlan),
            Replaced
            -  When Resource Exists:
               *  M(ros_vlan) will restore related C(/interface vlan) to its default value.
               *  M(ros_vlan) will update C(/interface vlan) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_vlan) will create new C(/interface vlan)
            Overridden:
            *  M(ros_vlan) will remove any existing item in C(/interface vlan)
            *  M(ros_vlan) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_vlan) will remove that item from C(/interface vlan) configuration
    config:
        description: A dictionary for L(ros_vlan)
        type: list
        elements: dict
        suboptions:
            arp:
                type: str
                default: enabled
                choices:
                    - disabled
                    - enabled
                    - proxy-arp
                    - reply-only
                description: |
                    Address Resolution Protocol mode
            interface:
                type: str
                required: True
                description: |
                    Name of physical interface on top of which VLAN will work
            l2mtu:
                type: int
                description: |
                    Layer2 MTU. For VLANS this value is not configurable. L( Read
                    more&gt;&gt;,/wiki/Maximum_Transmission_Unit_on_RouterBoards)
            mtu:
                type: str
                default: 1500
                description: |
                    Layer3 Maximum transmission unit
            name:
                type: str
                required: True
                description: |
                    Interface name
            use_service_tag:
                type: str
                choices:
                    - yes
                    - no
                default: None
                description: |
                    802.1ad compatible Service Tag
            vlan_id:
                type: str
                default: 1
                description: |
                    Virtual LAN identifier or tag that is used to distinguish VLANs. Must be equal
                    for all computers that belong to the same VLAN.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.interface.vlan import VlanResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=VlanResource.argument_spec)
    result = ResourceConfig(module, VlanResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
