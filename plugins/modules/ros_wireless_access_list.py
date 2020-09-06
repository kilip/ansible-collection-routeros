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
The module file for ros_wireless_access_list
"""

DOCUMENTATION = """
module: ros_wireless_access_list
author: Anthonius Munthi (@kilip)
short_description: Wireless Access List Module
description:
- This module manages the Wireless Access List configuration of Mikrotik RouterOS network devices.
version_added: 1.0.0
options:
  state:
    type: str
    choices: ["merged","replaced","overridden","deleted"]
    description: Set module state
    default: merged
  config:
    description: A dictionary of `/interface wireless access-list` parameters
    type: list
    elements: dict
    suboptions:
        ap_tx_limit:
          type: int

          description: |
            Limit rate of data transmission to this client. Value 0 means no limit. Value is
            in bits per second.

        authentication:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "yes"
          description: |
            - *no* - Client association will always fail.
            - *yes* - Use authentication procedure that is specified in the L(**security-profile**,#Security_Profiles) of the interface.

        client_tx_limit:
          type: int

          description: |
            Ask client to limit rate of data transmission. Value 0 means no limit.
            This is a proprietary extension that is supported by RouterOS clients.
            Value is in bits per second.

        comment:
          type: str
          required: True

          description: |
            Short description of an entry

        disabled:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "no"
          description: |

        forwarding:
          type: str
          choices:
            - 'no'
            - 'yes'
          default: "yes"
          description: |
            - *no* - Client cannot send frames to other station that are connected to same
              access point.
            - *yes* - Client can send frames to other stations on the same access point.

        interface:
          type: str
          default: "any"
          description: |
            Rules with **interface**=*any* are used for any wireless interface and the
            **interface**=*all* defines
            [interface-list](https://wiki.mikrotik.com/wiki/Manual:Interface/List#Lists
            'Manual:Interface/List') '''all''' name. To make rule that applies only to one
            wireless interface, specify that interface as a value of this property.

        mac_address:
          type: str
          default: "00:00:00:00:00:00"
          description: |
            Rule matches client with the specified MAC address. Value *00:00:00:00:00:00*
            matches always.

        management_protection_key:
          type: str

          description: |

        private_algo:
          type: str
          choices:
            - '104bit-wep'
            - '40bit-wep'
            - 'aes-ccm'
            - 'none'
            - 'tkip'
          default: "none"
          description: |
            Only for WEP modes.

        private_key:
          type: str

          description: |
            Only for WEP modes.

        private_pre_shared_key:
          type: str

          description: |
            Used in WPA PSK mode.

        signal_range:
          type: str
          default: "-120..120"
          description: |
            Rule matches if signal strength of the station is within the range.
            If signal strength of the station will go out of the range that is specified in
            the rule, access point will disconnect that station.

        time:
          type: str

          description: |
            Rule will match only during specified time.
            Station will be disconnected after specified time ends. Both start and end time
            is expressed as time since midnight, 00:00.
            Rule will match only during specified days of the week.

"""

EXAMPLES = """
# ----
# Using merge state
# ----
# before:
# [admin@MikroTik] > /interface wireless access-list export
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface wireless access-list
# add comment=existing action accept signal-range=-79..120
#
# configuration:
- name: Merge with device configuration
  kilip.routeros.ros_wireless_access_list:
    config:
      - comment: existing
        signal_range: '-80..120'
      - comment: new
        signal_range: '-50..120'
        interface: wlan1
    state: merged

#
# after:
# [admin@MikroTik] > /interface wireless access-list export
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface wireless access-list
# add comment=existing action=accept signal-range=-80..120
# add comment=new action=accept signal-range=-50..120
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
from ..module_utils.resources.wireless.wireless_access_list import (
    WirelessAccessListResource,
)
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(
        argument_spec=WirelessAccessListResource.argument_spec
    )
    result = Config(module, WirelessAccessListResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
