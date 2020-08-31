#!/usr/bin/python


"""
The module file for ros_wireless_cap
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_wireless_cap
short_description: Manage configuration for C(/interface wireless cap)
description: This M(ros_wireless_cap) module provides management for RouterOS C(/interface wireless cap).
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
    state:
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_wireless_cap) will update existing C(/interface wireless cap) configuration
            -  When Resource Not Exists:
               *  M(ros_wireless_cap) will create new C(/interface wireless cap),
            Replaced
            -  When Resource Exists:
               *  M(ros_wireless_cap) will restore related C(/interface wireless cap) to its default value.
               *  M(ros_wireless_cap) will update C(/interface wireless cap) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_wireless_cap) will create new C(/interface wireless cap)
            Overridden:
            *  M(ros_wireless_cap) will remove any existing item in C(/interface wireless cap)
            *  M(ros_wireless_cap) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_wireless_cap) will remove that item from C(/interface wireless cap) configuration
    config:
        description: A dictionary for L(ros_wireless_cap)
        suboptions:
            enabled:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Disable or enable CAP feature
            interfaces:
                type: list
                elements: str
                description: |
                    List of wireless interfaces to be controlled by Manager
            certificate:
                type: str
                choices:
                    - certificate
                    - name
                    - none
                default: None
                description: |
                    Certificate to use for authenticating
            discovery_interfaces:
                type: list
                elements: str
                description: |
                    List of interfaces over which CAP should attempt to discover Manager
            caps_man_addresses:
                type: str
                default: empty
                description: |
                    List of Manager IP addresses that CAP will attempt to contact during discovery
            caps_man_names:
                type: list
                elements: str
                description: |
                    An ordered list of CAPs Manager names that the CAP will connect to, if empty -
                    CAP does not check Manager name
            caps_man_certificate_common_names:
                type: list
                elements: str
                description: |
                    List of Manager certificate CommonNames that CAP will connect to, if empty - CAP
                    does not check Manager certificate CommonName
            bridge:
                type: str
                description: |
                    Bridge to which interfaces should be added when local forwarding mode is used
            static_virtual:
                type: str
                choices:
                    - yes
                    - no
                default: no
                description: |
                    CAP will create Static Virtual Interfaces instead of Dynamic and will try to
                    reuse the same interface on reconnect to CAPsMAN if the MAC address will be the
                    same. Note if two or more interfaces will have the same MAC address the
                    assignment from the CAPsMAN could be random between those interfaces.
config:
    type: list
state:
    choices:
        - present
        - reset
    default: present

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.wireless.cap import WirelessCapResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=WirelessCapResource.argument_spec)
    result = Config(module, WirelessCapResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
