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


class CapsmanManagerResource(ResourceBase):
    resource_name = "capsman_manager"
    command = "/caps-man manager"
    gather_network_resources = ["capsman_manager"]
    keys = ["name"]
    config_type = "setting"
    supports = ["export-verbose-mode"]
    argument_spec = {
        "state": {
            "type": "str",
            "choices": ["present", "reset"],
            "default": "present",
        },
        "config": {
            "type": "dict",
            "options": {
                "ca_certificate": {"type": "str"},
                "certificate": {
                    "type": "str",
                    "choices": ["auto", "certificate name", "none"],
                },
                "enabled": {"type": "bool", "default": False},
                "package_path": {"type": "str"},
                "require_peer_certificate": {"type": "bool", "default": False},
                "upgrade_policy": {
                    "type": "str",
                    "choices": [
                        "none",
                        "require-same-version",
                        "suggest-same-upgrade",
                    ],
                },
            },
        },
    }
