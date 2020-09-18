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
#     https://github.com/kilip/routeros-generator
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: ros_wireless_cap
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
short_description: Wireless CAP Setting
description:
  - This module manages the Wireless CAP setting of Mikrotik RouterOS network devices.
supports:
  - export-verbose-mode
options:
  state:
    choices:
      - present
      - reset
    default: present
    description: Set state for this module
  config:
    type: dict
    suboptions:
      bridge:
        type: str
        description: Bridge to which interfaces should be added when local forwarding mode is used
      caps_man_addresses:
        type: list
        description: List of Manager IP addresses that CAP will attempt to contact during discovery
      caps_man_certificate_common_names:
        type: list
        description: List of Manager certificate CommonNames that CAP will connect to, if empty - CAP does not check Manager certificate CommonName
      caps_man_names:
        type: list
        description: An ordered list of CAPs Manager names that the CAP will connect to, if empty - CAP does not check Manager name
      certificate:
        type: str
        description: Certificate to use for authenticating
      discovery_interfaces:
        type: list
        description: List of interfaces over which CAP should attempt to discover Manager
      enabled:
        type: bool
        default: False
        description: Disable or enable CAP feature
      interfaces:
        type: list
        description: List of wireless interfaces to be controlled by Manager
      lock_to_caps_man:
        type: bool
        default: False
      static_virtual:
        type: bool
        default: False
        description: CAP will create Static Virtual Interfaces instead of Dynamic and will try to reuse the same interface on reconnect to CAPsMAN if the MAC address will be the same. Note if two or more interfaces will have the same MAC address the assignment from the CAPsMAN could be random between those interfaces.
"""

EXAMPLES = """
# Change Wireless CAP Setting
#
# before state:
# [admin@MikroTik] > /interface wireless cap export
# /interface wireless cap
# set bridge=none certificate=none enabled=no lock-to-caps-man=no static-virtual=no
#
- name: Configure Wireless CAP
  kilip.routeros.ros_wireless_cap:
    config:
      interfaces:
        - wlan1
        - wlan2
    state: present
#
# after state:
# [admin@MikroTik] > /interface wireless cap export
# # RouterOS Output
# #
# /interface wireless cap
# set interfaces=wlan1,wlan2
#
#
"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.interface.wireless.wireless_cap import (
    WirelessCapResource,
)
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=WirelessCapResource.argument_spec)
    result = Config(module, WirelessCapResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
