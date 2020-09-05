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
The module file for ros_vlan
"""

DOCUMENTATION = """
module: ros_vlan
author: Anthonius Munthi (@kilip)
short_description: VLAN Resource Module
description:
- This module manages the vlan configuration of Mikrotik RouterOS network devices.
options:
  state:
    type: str
    choices: ["merged","replaced","overridden","deleted"]
    description: Set module state
    default: merged
  config:
    description: A dictionary of `/interface vlan` parameters
    type: list
    elements: dict
    suboptions:
        vlan_id:
          type: int
          required: True

          description: |
            Virtual LAN identifier or tag that is used to distinguish VLANs. Must be equal
            for all computers that belong to the same VLAN.

        interface:
          type: str
          required: True

          description: |
            Name of physical interface on top of which VLAN will work

        arp:
          type: str
          choices:
            - 'disabled'
            - 'enabled'
            - 'proxy-arp'
            - 'reply-only'
          default: "enabled"
          description: |
            Address Resolution Protocol mode

        l2mtu:
          type: int

          description: |
            Layer2 MTU. For VLANS this value is not configurable. L(Read more&gt;&gt;,https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards)

        mtu:
          type: int
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
            - 'no'
            - 'yes'

          description: |
            802.1ad compatible Service Tag

        comment:
          type: str

          description: |
            Give notes for this resource

"""

EXAMPLES = """
# ----
# Using merged state
# ----
# before:
#  [admin@MikroTik] > /interface vlan export
#  /interface vlan
#  add interface=br-trunk name=vlan-100 vlan-id=100 arp=reply-only
#
- name: Merge configuration with device configuration
  kilip.routeros.ros_vlan:
    config:
      - name: vlan-100
        interface: br-trunk
        vlan_id: 100
        comment: 'new comment'
      - name: vlan-200
        interface: br-trunk
        vlan_id: 200
        comment: 'new comment'
    state: merged

# after:
#  [admin@MikroTik] > /interface vlan export
#  /interface vlan
#  add interface=br-trunk name=vlan-100 vlan-id=100 comment="new comment"
#  add interface=br-trunk name=vlan-200 vlan-id=200 comment="new comment"
#
# ----
# Using replaced state
# ----
# before:
#  [admin@MikroTik] > /interface vlan export
#  /interface vlan
#  add interface=br-trunk name=vlan-100 vlan-id=100 arp=reply-only
#
- name: Replace device configuration
  kilip.routeros.ros_vlan:
    config:
      - name: vlan-100
        interface: br-trunk
        vlan_id: 100
        comment: 'new comment'
    state: replaced

# after:
#  [admin@MikroTik] > /interface vlan export
#  /interface vlan
#  add interface=br-trunk name=vlan-100 vlan-id=100 comment="new comment"
#  add interface=br-trunk name=vlan-200 vlan-id=200 comment="new comment"
#
# ----
# Using overridden state
# ----
# before:
#  [admin@MikroTik] > /interface vlan export
#  /interface vlan
#  add interface=br-trunk name=vlan-100 vlan-id=100 arp=reply-only
#
- name: Override device configuration
  kilip.routeros.ros_vlan:
    config:
      - name: vlan-new
        interface: br-trunk
        vlan_id: 100
        comment: 'new comment'
    state: overridden

# after:
#  [admin@MikroTik] > /interface vlan export
#  /interface vlan
#  add name=vlan-new interface=br-trunk vlan-id=100 comment="new comment"
#
# ----
# Using deleted state
# ----
# before:
#  [admin@MikroTik] > /interface vlan export
#  /interface vlan
#  add interface=br-trunk name=vlan-100 vlan-id=100 arp=reply-only
#
- name: Delete VLAN Interface
  kilip.routeros.ros_vlan:
    config:
      - name: vlan-100
        interface: br-trunk
        vlan_id: 100
    state: deleted

# after:
#  [admin@MikroTik] > /interface vlan export
#
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
from ..module_utils.resources.interface.vlan import VlanResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=VlanResource.argument_spec)
    result = Config(module, VlanResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
