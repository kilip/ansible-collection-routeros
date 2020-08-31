#!/usr/bin/python


"""
The module file for ros_bridge_settings
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_bridge_settings
short_description: Bridge Settings
description: Globally controlled settings and statistics for all bridge interfaces.
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
    state:
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_bridge_settings) will update existing C(/interface bridge settings) configuration
            -  When Resource Not Exists:
               *  M(ros_bridge_settings) will create new C(/interface bridge settings),
            Replaced
            -  When Resource Exists:
               *  M(ros_bridge_settings) will restore related C(/interface bridge settings) to its default value.
               *  M(ros_bridge_settings) will update C(/interface bridge settings) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_bridge_settings) will create new C(/interface bridge settings)
            Overridden:
            *  M(ros_bridge_settings) will remove any existing item in C(/interface bridge settings)
            *  M(ros_bridge_settings) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_bridge_settings) will remove that item from C(/interface bridge settings) configuration
    config:
        description: A dictionary for L(ros_bridge_settings)
        suboptions:
            use_ip_firewall:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Force bridged traffic to also be processed by prerouting, forward and
                    postrouting sections of IP routing (L( Packet
                    Flow,https://wiki.mikrotik.com/wiki/Manual:Packet_Flow_v6) to traffic in a
                    bridge. Property use-ip-firewall-for-vlan is required in case bridge
                    vlan-filtering is used.
            use_ip_firewall_for_pppoe:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Send bridged un-encrypted PPPoE traffic to also be processed by
                    L(IP/Firewall,https://wiki.mikrotik.com/wiki/Manual:IP/Firewall) to PPPoE
                    traffic in a bridge.
            use_ip_firewall_for_vlan:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Send bridged VLAN traffic to also be processed by
                    L(IP/Firewall,https://wiki.mikrotik.com/wiki/Manual:IP/Firewall) to VLAN traffic
                    in a bridge.
            allow_fast_path:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Allows L(FastPath,https://wiki.mikrotik.com/wiki/Manual:Fast_Path).
config:
    type: list
state:
    choices:
        - present
        - reset
    default: present

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.bridge.settings import BridgeSettingsResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=BridgeSettingsResource.argument_spec)
    result = Config(module, BridgeSettingsResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
