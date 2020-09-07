#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Anthonius Munthi
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Ansible RouterOS Module Generator
#     and manual changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://github.com/kilip/ansible-routeros-generator
#
# ----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The module file for kilip.routeros.ros_bridge_settings
"""

DOCUMENTATION = """
module: ros_bridge_settings
author: Anthonius Munthi (@kilip)
short_description: Bridge Setting Module
description:
- This modules manages configuration in submenu `/interface bridge settings`.
version_added: 1.0.0
options:
  state:
    type: str
    choices: ["present","reset"]
    description: Set module state
    default: present
  config:
    description: A dictionary of `/interface bridge settings` parameters
    type: dict
    suboptions:
        allow_fast_path:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "yes"
          description: |
            Whether to enable a bridge [
            FastPath](https://wiki.mikrotik.com/wiki/Manual:Fast_Path 'Manual:Fast Path')
            globally.

        use_ip_firewall:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "no"
          description: |
            Force bridged traffic to also be processed by prerouting, forward and
            postrouting sections of IP routing ([ Packet
            Flow](https://wiki.mikrotik.com/wiki/Manual:Packet_Flow_v6 'Manual:Packet Flow
            v6')). This does not apply to routed traffic. This property is required in case
            you want to assign [ Simple
            Queues](https://wiki.mikrotik.com/wiki/Manual:Queue#Simple_Queues
            'Manual:Queue') or global [ Queue
            Tree](https://wiki.mikrotik.com/wiki/Manual:Queue#Queue_Tree 'Manual:Queue') to
            traffic in a bridge. Property use-ip-firewall-for-vlan is required in case
            bridge vlan-filtering is used.

        use_ip_firewall_for_pppoe:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "no"
          description: |
            Send bridged un-encrypted PPPoE traffic to also be processed by [
            IP/Firewall](https://wiki.mikrotik.com/wiki/Manual:IP/Firewall
            'Manual:IP/Firewall'). This property only has effect when use-ip-firewall is set
            to C(yes). This property is required in case you want to assign [ Simple
            Queues](https://wiki.mikrotik.com/wiki/Manual:Queue#Simple_Queues
            'Manual:Queue') or global [ Queue
            Tree](https://wiki.mikrotik.com/wiki/Manual:Queue#Queue_Tree 'Manual:Queue') to
            PPPoE traffic in a bridge.

        use_ip_firewall_for_vlan:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "no"
          description: |
            Send bridged VLAN traffic to also be processed by [
            IP/Firewall](https://wiki.mikrotik.com/wiki/Manual:IP/Firewall
            'Manual:IP/Firewall'). This property only has effect when use-ip-firewall is set
            to C(yes). This property is required in case you want to assign [ Simple
            Queues](https://wiki.mikrotik.com/wiki/Manual:Queue#Simple_Queues
            'Manual:Queue') or global [ Queue
            Tree](https://wiki.mikrotik.com/wiki/Manual:Queue#Queue_Tree 'Manual:Queue') to
            VLAN traffic in a bridge.

"""

EXAMPLES = """
# ----
# Change Bridge Setting Configuration
# ----
# before:
# [admin@MikroTik] > /interface bridge settings export verbose
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface bridge settings
# set allow-fast-path=no use-ip-firewall=yes use-ip-firewall-for-pppoe=yes use-ip-firewall-for-vlan=yes
#
# configuration:
- name: Configure Bridge Settings
  kilip.routeros.kilip.routeros.ros_bridge_settings:
    config:
      allow_fast_path: 'yes'
      use_ip_firewall: 'no'
      use_ip_firewall_for_pppoe: 'no'
      use_ip_firewall_for_vlan: 'no'
    state: present

#
# after:
# [admin@MikroTik] > /interface bridge settings export verbose
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface bridge settings
# set allow-fast-path=yes use-ip-firewall=no use-ip-firewall-for-pppoe=no use-ip-firewall-for-vlan=no
# ----
# Change Bridge Setting Configuration
# ----
# before:
# [admin@MikroTik] > /interface bridge settings export verbose
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface bridge settings
# set allow-fast-path=no use-ip-firewall=yes use-ip-firewall-for-pppoe=yes use-ip-firewall-for-vlan=yes
#
# configuration:
- name: Configure Bridge Settings
  kilip.routeros.kilip.routeros.ros_bridge_settings:
    state: reset

#
# after:
# [admin@MikroTik] > /interface bridge settings export verbose
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface bridge settings
# set allow-fast-path=yes use-ip-firewall-for-pppoe=no use-ip-firewall-for-vlan=no use-ip-firewall=no
"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
commands:
  description: The set of commands pushed to the remote device
  returned: always
  type: list
  sample: ['/interface bridge add name=sample']
"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.bridge.bridge_settings import (
    BridgeSettingsResource,
)
from ..module_utils.config.setting import Setting


def main():
    module = AnsibleModule(argument_spec=BridgeSettingsResource.argument_spec)
    result = Setting(module, BridgeSettingsResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
