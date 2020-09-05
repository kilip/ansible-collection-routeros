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
The module file for ros_interface
"""

DOCUMENTATION = """
module: ros_interface
author: Anthonius Munthi (@kilip)
short_description: Interface Resource Module
description:
- This module manages the interface configuration of Mikrotik RouterOS network devices.
options:
  state:
    type: str
    choices: ["merged"]
    description: Set module state
    default: merged
  config:
    description: A dictionary of `/interface` parameters
    type: list
    elements: dict
    suboptions:
        disabled:
          type: str
          choices:
            - 'yes'
            - 'no'
          default: "no"
          description: |
            Set interface disability.

        l2mtu:
          type: int

          description: |
            Layer2 Maximum transmission unit. Note that this property can not be configured
            on all interfaces. L(Read more&gt;&gt; ,https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards)

        mtu:
          type: int

          description: |
            Layer3 Maximum transmission unit

        name:
          type: str

          description: |
            Name of an interface

        comment:
          type: str

          description: |
            Give notes for this resource

"""

EXAMPLES = """
# ----
# Using Merged
# ----
# before:
#  [admin@MikroTik] > /interface export
#  # sep/04/2020 07:20:39 by RouterOS 6.47.2
#  # software id =
#  #
#  #
#  #
#  /interface ethernet
#  set [ find default-name=ether1 ] comment="ether1 comment" mtu=1500
#  set [ find default-name=ether2 ] comment="ether2 comment" disabled=yes
#  /interface bridge
#  add name=br-wan comment="wan bridge"
#
- name: Merge configuration with device configuration
  kilip.routeros.ros_interface:
    config:
      - name: ether1
        comment: 'ether1 updated'
        mtu: 1000
      - name: ether2
        comment: 'ether2 updated'
        mtu: 2000
        disabled: false
      - name: br-wan
        disabled: true
        mtu: 3000
        comment: 'br-wan updated'
    state: merged

# after:
#  [admin@MikroTik] > /interface export
#  /interface ethernet
#  set [ find default-name=ether1 ] comment="ether1 updated" mtu=1000
#  set [ find default-name=ether2 ] comment="ether2 updated" mtu=2000
#  /interface bridge
#  add name=br-wan comment="br-wan updated" mtu=3000 disabled=yes
#"""

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
from ..module_utils.resources.interface.interface import InterfaceResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=InterfaceResource.argument_spec)
    result = Config(module, InterfaceResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
