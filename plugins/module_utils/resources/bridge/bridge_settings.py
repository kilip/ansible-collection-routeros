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

from ..base import ResourceBase


class BridgeSettingsResource(ResourceBase):
    resource_name = "bridge_settings"
    command = "/interface bridge settings"
    gather_network_resources = ["bridge_settings"]
    keys = []
    type = "setting"
    supports = ["facts_verbose_mode"]
    argument_spec = {
        "state": {
            "choices": ["present", "reset"],
            "default": "present",
            "type": "str",
        },
        "config": {
            "type": "dict",
            "options": {
                "use_ip_firewall": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "use_ip_firewall_for_pppoe": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "use_ip_firewall_for_vlan": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "allow_fast_path": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "yes",
                },
            },
        },
    }
