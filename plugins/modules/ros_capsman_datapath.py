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
The module file for ros_capsman_datapath
"""

DOCUMENTATION = """
module: ros_capsman_datapath
author: Anthonius Munthi (@kilip)
short_description: CAPsMan DataPath Configuration Module
description:
- This modules manages CAPsMan DataPath Configuration on Mikrotik RouterOS network devices
version_added: 1.0.0
options:
  state:
    type: str
    choices: ["merged","replaced","overridden","deleted"]
    description: Set module state
    default: merged
  config:
    description: A dictionary of `/caps-man datapath` parameters
    type: list
    elements: dict
    suboptions:
        arp:
          type: str
          choices:
            - 'disabled'
            - 'enabled'
            - 'proxy-arp'
            - 'reply-only'
          default: "enabled"
          description: |
            Address Resolution Protocol setting
            - C(disabled) - the interface will not use ARP
            - C(enabled) - the interface will use ARP
            - C(proxy-arp) - the interface will use the ARP proxy feature
            - C(reply-only) - the interface will only reply to requests originated from
              matching IP address/MAC address combinations which are entered as static entries
              in the L(IP/ARP,https://wiki.mikrotik.com/wiki/Manual:IP/ARP) table. Therefore
              for communications to be successful, a valid static entry must already exist.

        bridge:
          type: str

          description: |
            Bridge to which particular interface should be automatically added as port.
            Required only when local-forwarding is not used.

        bridge_cost:
          type: int

          description: |
            bridge port cost to use when adding as bridge port

        bridge_horizon:
          type: int

          description: |
            bridge horizon to use when adding as bridge port

        client_to_client_forwarding:
          type: str
          choices:
            - 'yes'
            - 'no'
          default: "no"
          description: |
            controls if client-to-client forwarding between wireless clients connected to
            interface should be allowed, in local forwarding mode this function is performed
            by CAP, otherwise it is performed by CAPsMAN

        comment:
          type: str

          description: |
            Short description of the datapath

        interface_list:
          type: list
          elements: "str"

          description: |
            interface list for this datapath

        l2mtu:
          type: str

          description: |
            set Layer2 MTU size

        local_forwarding:
          type: str
          choices:
            - 'yes'
            - 'no'
          default: "no"
          description: |
            Controls forwarding mode. If disabled, all L2 and L3 data will be forwarded to
            CAPsMAN, and further forwarding decisions will be made only then.
            Note, if disabled, make sure that each CAP interface MAC Address that
            participates in the same broadcast domain is unique (including local MACs, like
            Bridge-MAC).

        mtu:
          type: str

          description: |
            set MTU size

        name:
          type: str
          required: True

          description: |
            Name for datapath

        openflow_switch:
          type: str

          description: |
            OpenFlow switch port (when enabled) to add interface to

        vlan_id:
          type: int

          description: |
            VLAN ID to assign to interface if vlan-mode enables use of VLAN tagging

        vlan_mode:
          type: str
          choices:
            - 'use-service-tag'
            - 'use-tag'

          description: |
            Enables and specifies the type of VLAN tag to be assigned to the interface
            (causes all received data to get tagged with VLAN tag and allows the interface
            to only send out data tagged with given tag)

"""

EXAMPLES = """
# ----
# Using Merged
# ----
# before:
# [admin@MikroTik] > /caps-man datapath export
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /caps-man datapath
# add name=test
#
# configuration:
- name: Merge with device configuration
  kilip.routeros.ros_capsman_datapath:
    state: merged
    config:
      - name: test
        bridge: br-trunk
        arp: reply-only
      - name: new
        bridge: br-trunk
        arp: reply-only

#
# after:
# [admin@MikroTik] > /caps-man datapath export
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /caps-man datapath
# add name=test bridge=br-trunk arp=reply-only
# add name=new bridge=br-trunk arp=reply-only
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
from ..module_utils.resources.capsman.capsman_datapath import (
    CapsmanDatapathResource,
)
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=CapsmanDatapathResource.argument_spec)
    result = Config(module, CapsmanDatapathResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
