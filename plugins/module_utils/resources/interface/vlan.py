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

from ..base import ResourceBase


class VlanResource(ResourceBase):
    resource_name = "vlan"
    command = "/interface vlan"
    gather_network_resources = ["vlan"]
    keys = ["name"]
    config_type = "config"
    argument_spec = {
        "state": {
            "choices": ["merged", "replaced", "overridden", "deleted"],
            "default": "merged",
            "type": "str",
        },
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                "arp": {
                    "type": "str",
                    "choices": [
                        "disabled",
                        "enabled",
                        "proxy-arp",
                        "reply-only",
                    ],
                    "default": "enabled",
                },
                "comment": {"type": "str"},
                "interface": {"type": "str", "required": True},
                "l2mtu": {"type": "int"},
                "mtu": {"type": "int", "default": 1500},
                "name": {"type": "str", "required": True},
                "use_service_tag": {"type": "str", "choices": ["no", "yes"]},
                "vlan_id": {"type": "int", "required": True},
            },
        },
    }
