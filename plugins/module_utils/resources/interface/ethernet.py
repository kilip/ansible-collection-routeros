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

from ..base import ResourceBase


class EthernetResource(ResourceBase):
    resource_name = "ethernet"
    command = "/interface ethernet"
    gather_network_resources = ["ethernet"]
    keys = ["name"]
    config_type = "config"
    argument_spec = {
        "state": {
            "type": "str",
            "choices": ["merged", "replaced", "overridden", "deleted"],
            "default": "merged",
        },
        "config": {
            "type": "list",
            "elements": "dict",
            "options": {
                "advertise": {
                    "type": "list",
                    "choices": [
                        "10000M-full",
                        "1000M-full",
                        "1000M-half",
                        "100M-full",
                        "100M-half",
                        "10M-full",
                        "10M-half",
                        "2500M-full",
                        "5000M-full",
                    ],
                },
                "arp": {
                    "type": "str",
                    "choices": [
                        "disabled",
                        "enabled",
                        "local-proxy-arp",
                        "proxy-arp",
                        "reply-only",
                    ],
                    "default": "enabled",
                },
                "auto_negotiation": {"type": "bool", "default": True},
                "bandwidth": {"type": "int", "default": 0},
                "cable_setting": {
                    "type": "str",
                    "choices": ["default", "short", "standard"],
                    "default": "default",
                },
                "combo_mode": {
                    "type": "str",
                    "choices": ["auto", "copper", "sfp"],
                    "default": "auto",
                },
                "comment": {"type": "str"},
                "disable_running_check": {"type": "bool", "default": True},
                "disabled": {"type": "bool", "default": False},
                "full_duplex": {"type": "bool", "default": True},
                "l2mtu": {"type": "int"},
                "mac_address": {"type": "str"},
                "master_port": {"type": "str"},
                "mdix_enable": {"type": "bool", "default": True},
                "mtu": {"type": "int", "default": 1500},
                "name": {"type": "str", "required": True},
                "poe_out": {
                    "type": "str",
                    "choices": ["auto-on", "forced-on", "off"],
                    "default": "off",
                },
                "poe_priority": {"type": "int"},
                "rx_flow_control": {
                    "type": "str",
                    "choices": ["auto", "off", "on"],
                    "default": "off",
                },
                "speed": {
                    "type": "str",
                    "choices": ["100Mbps", "10Gbps", "10Mbps", "1Gbps"],
                },
                "tx_flow_control": {
                    "type": "str",
                    "choices": ["auto", "off", "on"],
                    "default": "off",
                },
            },
        },
    }
