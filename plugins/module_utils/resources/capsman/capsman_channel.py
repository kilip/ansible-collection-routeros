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


class CapsmanChannelResource(ResourceBase):
    resource_name = "capsman_channel"
    command = "/caps-man channel"
    gather_network_resources = ["capsman_channel"]
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
                "band": {
                    "type": "str",
                    "choices": [
                        "2ghz-b",
                        "2ghz-b/g",
                        "2ghz-b/g/n",
                        "2ghz-onlyg",
                        "2ghz-onlyn",
                        "5ghz-a",
                        "5ghz-a/n",
                        "5ghz-onlyn",
                    ],
                },
                "comment": {"type": "str"},
                "disabled": {"type": "bool", "default": False},
                "extension_channel": {
                    "type": "str",
                    "choices": [
                        "Ce",
                        "Ceee",
                        "disabled",
                        "eC",
                        "eCee",
                        "eeCe",
                        "eeeC",
                    ],
                },
                "frequency": {"type": "int"},
                "name": {"type": "str", "required": True},
                "save_selected": {"type": "bool", "default": True},
                "tx_power": {"type": "int"},
                "width": {"type": "str"},
            },
        },
    }
