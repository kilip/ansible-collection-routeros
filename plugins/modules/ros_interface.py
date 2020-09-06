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
The module file for ros_interface
"""

DOCUMENTATION = """
module: ros_interface
author: Anthonius Munthi (@kilip)
short_description: Interface Resource Module
description:
- This module manages the interface configuration of Mikrotik RouterOS network devices.
version_added: 1.0.0
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
        comment:
          type: str

          description: |
            Give notes for this resource

        disabled:
          type: str
          choices:
            - 'yes'
            - 'no'
          default: "no"
          description: |
            Set interface disability.

        l2mtu:
          type: str

          description: |
            Layer2 Maximum transmission unit. Note that this property can not be configured
            on all interfaces. [ Read more&gt;&gt;
            ](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards
            'Maximum Transmission Unit on RouterBoards')

        mtu:
          type: str

          description: |
            Layer3 Maximum transmission unit

        name:
          type: str
          required: True

          description: |
            Name of an interface

"""

EXAMPLES = """
# ----
# Using Merged
# ----
# before:
# [admin@MikroTik] > /interface export verbose
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface ethernet
# set [ find default-name=ether2 ] comment="ether2 comment" mtu=1500
# set [ find default-name=ether3 ] comment="ether3 comment" mtu=1500 disabled=yes
#
# configuration:
- name: Merge configuration with device configuration
  kilip.routeros.ros_interface:
    config:
      - name: ether2
        comment: 'ether2 updated'
        mtu: '2000'
      - name: ether3
        comment: 'ether3 updated'
        disabled: 'no'
        mtu: '3000'
    state: merged

#
# after:
# [admin@MikroTik] > /interface export verbose
# sep/06/2020 03:08:16 by RouterOS 6.47.2
# software id =
# /interface ethernet
# set [ find default-name=ether2 ] comment="ether2 updated" mtu=2000
# set [ find default-name=ether3 ] comment="ether3 updated" mtu=3000
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
from ..module_utils.resources.interface.interface import InterfaceResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=InterfaceResource.argument_spec)
    result = Config(module, InterfaceResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
