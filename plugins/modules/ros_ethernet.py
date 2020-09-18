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
module: ros_ethernet
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
short_description: Ethernet Resource Module
description:
  - This module manages the ethernet configuration of Mikrotik RouterOS network devices.
options:
  state:
    choices:
      - merged
      - replaced
      - overridden
      - deleted
    default: merged
    description: Set state for this module
  config:
    type: list
    elements: dict
    suboptions:
      advertise:
        type: list
        choices:
          - 10000M-full
          - 1000M-full
          - 1000M-half
          - 100M-full
          - 100M-half
          - 10M-full
          - 10M-half
          - 2500M-full
          - 5000M-full
        description: Advertised speed and duplex modes for Ethernet interfaces over twisted pair, only applies when C(auto-negotiation) is enabled. Advertising higher speeds than the actual interface supported speed will have no effect, multiple options are allowed.
      arp:
        type: str
        choices:
          - disabled
          - enabled
          - local-proxy-arp
          - proxy-arp
          - reply-only
        default: enabled
        description: |
          Address Resolution Protocol mode:
          - C(disabled) - the interface will not use ARP
          - C(enabled) - the interface will use ARP
          - C(local-proxy-arp) - the router performs proxy ARP on the interface and sends replies to the same interface
          - C(proxy-arp) - the router performs proxy ARP on the interface and sends replies to other interfaces
          - C(reply-only) - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the L(ARP, https://wiki.mikrotik.com/wiki/Manual:IP/ARP) table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
      auto_negotiation:
        type: bool
        default: True
        description: |
          When enabled, the interface "advertises" its maximum capabilities to achieve the best connection possible.
          - **Note1:** Auto-negotiation should not be disabled on one end only, otherwise Ethernet Interfaces may not work properly.
          - **Note2:** Gigabit Ethernet and NBASE-T Ethernet links cannot work with auto-negotiation disabled.
      bandwidth:
        type: int
        default: 0
        description: Sets max rx/tx bandwidth in kbps that will be handled by an interface. TX limit is supported on all Atheros L(switch-chip, https://wiki.mikrotik.com/wiki/Manual:Switch_Chip_Features) ports. RX limit is supported only on Atheros8327/QCA8337 switch-chip ports.
      cable_setting:
        type: str
        choices:
          - default
          - short
          - standard
        default: default
        description: Changes the cable length setting (only applicable to NS DP83815/6 cards)
      combo_mode:
        type: str
        choices:
          - auto
          - copper
          - sfp
        default: auto
        description: When C(auto) mode is selected, the port that was first connected will establish the link. In case this link fails, the other port will try to establish a new link. If both ports are connected at the same time (e.g. after reboot), the priority will be the SFP/SFP+ port. When C(sfp) mode is selected, the interface will only work through SFP/SFP+ cage. When C(copper) mode is selected, the interface will only work through RJ45 Ethernet port.
      comment:
        type: str
        description: Descriptive name of an item
      disable_running_check:
        type: bool
        default: True
        description: Disable running check. If this value is set to 'no', the router automatically detects whether the NIC is connected with a device in the network or not. Default value is 'yes' because older NICs do not support it. (only applicable to x86)
      disabled:
        type: bool
        default: False
        description: Set interface disability.
      full_duplex:
        type: bool
        default: True
        description: Defines whether the transmission of data appears in two directions simultaneously, only applies when C(auto-negotiation) is disabled.
      l2mtu:
        type: int
        description: Layer2 Maximum transmission unit. L(Read more&gt;&gt; , https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards)
      mac_address:
        type: str
        description: Media Access Control number of an interface.
      master_port:
        type: str
        description: Outdated property, more details about this property can be found in the L(Master-port, https://wiki.mikrotik.com/wiki/Manual:Master-port) page.
      mdix_enable:
        type: bool
        default: True
        description: Whether the MDI/X auto cross over cable correction feature is enabled for the port (Hardware specific, e.g. ether1 on RB500 can be set to yes/no. Fixed to 'yes' on other hardware.)
      mtu:
        type: int
        default: 1500
        description: Layer3 Maximum transmission unit
      name:
        type: str
        required: True
        description: Name of an interface
      poe_out:
        type: str
        choices:
          - auto-on
          - forced-on
          - off
        default: off
        description: Poe Out settings. L(C(Read more >>), https://wiki.mikrotik.com/wiki/Manual:PoE-Out)
      poe_priority:
        type: int
        description: Poe Out settings. L(C(Read more >>), https://wiki.mikrotik.com/wiki/Manual:PoE-Out)
      rx_flow_control:
        type: str
        choices:
          - auto
          - off
          - on
        default: off
        description: When set to on, the port will process received pause frames and suspend transmission if required. **auto** is the same as **on** except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises.
      speed:
        type: str
        choices:
          - 100Mbps
          - 10Gbps
          - 10Mbps
          - 1Gbps
        description: Sets interface data transmission speed which takes effect only when C(auto-negotiation) is disabled.
      tx_flow_control:
        type: str
        choices:
          - auto
          - off
          - on
        default: off
        description: When set to on, the port will generate pause frames to the upstream device to temporarily stop the packet transmission. Pause frames are only generated when some routers output interface is congested and packets cannot be transmitted anymore. **auto** is the same as **on** except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises.
"""

EXAMPLES = """
# Using merged state
#
# before state:
# [admin@MikroTik] > /interface ethernet export
# /interface ethernet
# set comment="ether1 comment" name=ether1
#
- name: Merge configuration with device configuration
  kilip.routeros.ros_ethernet:
    config:
      - name: ether1
        advertise:
          - 10M-full
          - 100M-full
          - 1000M-full
        comment: updated comment
    state: merged
#
# after state:
# [admin@MikroTik] > /interface ethernet export
# # RouterOS Output
# #
# /interface ethernet
# add advertise=10M-full,100M-full,1000M-full comment="updated comment" name=ether1
#
#
"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.interface.ethernet import EthernetResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=EthernetResource.argument_spec)
    result = Config(module, EthernetResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
