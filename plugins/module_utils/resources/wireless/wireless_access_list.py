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


class WirelessAccessListResource(ResourceBase):
    resource_name = "wireless_access_list"
    command = "/interface wireless access-list"
    gather_network_resources = ["wireless_access_list"]
    keys = ["comment"]
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
                "ap_tx_limit": {"type": "int"},
                "authentication": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "yes",
                },
                "client_tx_limit": {"type": "int"},
                "comment": {"type": "str", "required": True},
                "disabled": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "forwarding": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "yes",
                },
                "interface": {"type": "str", "default": "any"},
                "mac_address": {"type": "str", "default": "00:00:00:00:00:00"},
                "management_protection_key": {"type": "str"},
                "private_algo": {
                    "type": "str",
                    "choices": [
                        "104bit-wep",
                        "40bit-wep",
                        "aes-ccm",
                        "none",
                        "tkip",
                    ],
                    "default": "none",
                },
                "private_key": {"type": "str"},
                "private_pre_shared_key": {"type": "str"},
                "signal_range": {"type": "str", "default": "-120..120"},
                "time": {"type": "str"},
            },
        },
    }
