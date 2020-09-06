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
#     https://www.github.com/kilip/ansible-routeros-generator
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type


"""
The module file for ros_ethernet
"""

DOCUMENTATION = """
module: ros_ethernet
author: Anthonius Munthi (@kilip)
short_description: Ethernet Resource Module
description:
- This module manages the ethernet configuration of Mikrotik RouterOS network devices.
version_added: 1.0.0
options:
  state:
    type: str
    choices: ["merged","replaced","overridden","deleted"]
    description: Set module state
    default: merged
  config:
    description: A dictionary of `/interface ethernet` parameters
    type: list
    elements: dict
    suboptions:
        advertise:
          type: list
          elements: "str"
          choices:
            - '10000M-full'
            - '1000M-full'
            - '1000M-half'
            - '100M-full'
            - '100M-half'
            - '10M-full'
            - '10M-half'
            - '2500M-full'
            - '5000M-full'

          description: |
            Advertised speed and duplex modes for Ethernet interfaces over twisted pair,
            only applies when auto-negotiation is enabled. Advertising higher speeds than
            the actual interface supported speed will have no effect, multiple options are
            allowed.

        arp:
          type: str
          choices:
            - 'disabled'
            - 'enabled'
            - 'local-proxy-arp'
            - 'proxy-arp'
            - 'reply-only'
          default: "enabled"
          description: |
            Address Resolution Protocol mode:
            - disabled - the interface will not use ARP
            - enabled - the interface will use ARP
            - local-proxy-arp - the router performs proxy ARP on the interface and sends
              replies to the same interface
            - proxy-arp - the router performs proxy ARP on the interface and sends replies
              to other interfaces
            - reply-only - the interface will only reply to requests originated from
              matching IP address/MAC address combinations which are entered as static entries
              in the [ ARP](https://wiki.mikrotik.com/wiki/Manual:IP/ARP 'Manual:IP/ARP')
              table. No dynamic entries will be automatically stored in the ARP table.
              Therefore for communications to be successful, a valid static entry must already
              exist.

        auto_negotiation:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "yes"
          description: |
            When enabled, the interface 'advertises' its maximum capabilities to achieve the
            best connection possible.
            - **Note1:** Auto-negotiation should not be disabled on one end only, otherwise
              Ethernet Interfaces may not work properly.
            - **Note2:** Gigabit Ethernet and NBASE-T Ethernet links cannot work with
              auto-negotiation disabled.

        bandwidth:
          type: int

          description: |
            Sets max rx/tx bandwidth in kbps that will be handled by an interface. TX limit
            is supported on all Atheros [
            switch-chip](https://wiki.mikrotik.com/wiki/Manual:Switch_Chip_Features
            'Manual:Switch Chip Features') ports. RX limit is supported only on
            Atheros8327/QCA8337 switch-chip ports.

        cable_setting:
          type: str
          choices:
            - 'default'
            - 'short'
            - 'standard'
          default: "default"
          description: |
            Changes the cable length setting (only applicable to NS DP83815/6 cards)

        combo_mode:
          type: str
          choices:
            - 'auto'
            - 'copper'
            - 'sfp'
          default: "auto"
          description: |
            When auto mode is selected, the port that was first connected will establish the
            link. In case this link fails, the other port will try to establish a new link.
            If both ports are connected at the same time (e.g. after reboot), the priority
            will be the SFP/SFP+ port. When sfp mode is selected, the interface will only
            work through SFP/SFP+ cage. When copper mode is selected, the interface will
            only work through RJ45 Ethernet port.

        comment:
          type: str

          description: |
            Descriptive name of an item

        disable_running_check:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "yes"
          description: |
            Disable running check. If this value is set to 'no', the router automatically
            detects whether the NIC is connected with a device in the network or not.
            Default value is 'yes' because older NICs do not support it. (only applicable to
            x86)

        disabled:
          type: str
          choices:
            - 'yes'
            - 'no'
          default: "no"
          description: |
            Set interface disability.

        full_duplex:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "yes"
          description: |
            Defines whether the transmission of data appears in two directions
            simultaneously, only applies when auto-negotiation is disabled.

        l2mtu:
          type: int

          description: |
            Layer2 Maximum transmission unit. [ Read more&gt;&gt;
            ](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards
            'Maximum Transmission Unit on RouterBoards')

        mac_address:
          type: str

          description: |
            Media Access Control number of an interface.

        master_port:
          type: str
          default: "none"
          description: |
            Outdated property, more details about this property can be found in the [
            Master-port](https://wiki.mikrotik.com/wiki/Manual:Master-port
            'Manual:Master-port') page.

        mdix_enable:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "yes"
          description: |
            Whether the MDI/X auto cross over cable correction feature is enabled for the
            port (Hardware specific, e.g. ether1 on RB500 can be set to yes/no. Fixed to
            'yes' on other hardware.)

        mtu:
          type: int
          default: 1500
          description: |
            Layer3 Maximum transmission unit

        name:
          type: str
          required: True

          description: |
            Name of an interface

        poe_out:
          type: str
          choices:
            - 'auto-on'
            - 'forced-on'
            - 'off'
          default: "off"
          description: |
            Poe Out settings. [ C(Read more
            >>)](https://wiki.mikrotik.com/wiki/Manual:PoE-Out 'Manual:PoE-Out')

        poe_priority:
          type: int

          description: |
            Poe Out settings. [ C(Read more
            >>)](https://wiki.mikrotik.com/wiki/Manual:PoE-Out 'Manual:PoE-Out')

        rx_flow_control:
          type: str
          choices:
            - 'auto'
            - 'off'
            - 'on'
          default: "off"
          description: |
            When set to on, the port will process received pause frames and suspend
            transmission if required. **auto** is the same as **on** except when
            auto-negotiation=yes flow control status is resolved by taking into account what
            other end advertises.

        speed:
          type: str
          choices:
            - '100Mbps'
            - '10Gbps'
            - '10Mbps'
            - '1Gbps'

          description: |
            Sets interface data transmission speed which takes effect only when
            auto-negotiation is disabled.

        tx_flow_control:
          type: str
          choices:
            - 'auto'
            - 'off'
            - 'on'
          default: "off"
          description: |
            When set to on, the port will generate pause frames to the upstream device to
            temporarily stop the packet transmission. Pause frames are only generated when
            some routers output interface is congested and packets cannot be transmitted
            anymore. **auto** is the same as **on** except when auto-negotiation=yes flow
            control status is resolved by taking into account what other end advertises.

"""

EXAMPLES = """
# ----
# Using merged state
# ----
# before:
# [admin@MikroTik] > /interface ethernet export
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface ethernet
# set [ find default-name=ether1 ] comment="ether1 comment"
#
# configuration:
- name: Merge configuration with device configuration
  kilip.routeros.ros_ethernet:
    config:
      - name: ether1
        advertise:
          - 10M-full
          - 100M-full
          - 1000M-full
        comment: 'updated comment'
    state: merged

#
# after:
# [admin@MikroTik] > /interface ethernet export
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface ethernet
# set [ find default-name=ether1 ] comment="updated comment"
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
from ..module_utils.resources.interface.ethernet import EthernetResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=EthernetResource.argument_spec)
    result = Config(module, EthernetResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
