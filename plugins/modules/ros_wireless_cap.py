#!/usr/bin/python


"""
The module file for ros_wireless_cap
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_wireless_cap
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
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
                    An ordered list of CAPs Manager names that the CAP will connect to, if empty - CAP does not check Manager name
            caps_man_certificate_common_names:
                type: list
                elements: str
                description: |
                    List of Manager certificate CommonNames that CAP will connect to, if empty - CAP does not check Manager certificate CommonName
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
                    CAP will create Static Virtual Interfaces instead of Dynamic and will try to reuse the same interface on reconnect to CAPsMAN if the MAC address will be the same. Note if two or more interfaces will have the same MAC address the assignment from the CAPsMAN could be random between those interfaces.
config:
    type: list
state:
    choices:
        - present
        - reset
    default: present
    description:
        - I(present) will update C(/interface wireless cap) config with passed argument_spec values.
        - I(reset) will restore C(/interface wireless cap) to its default values

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
