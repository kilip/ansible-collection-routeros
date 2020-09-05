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


class BridgePortResource(ResourceBase):
    resource_name = "bridge_port"
    command = "/interface bridge port"
    gather_network_resources = ["bridge_port"]
    keys = ["bridge", "interface"]
    type = "config"
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
                "disabled": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "auto_isolate": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "bpdu_guard": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "bridge": {"type": "str", "required": True},
                "broadcast_flood": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "yes",
                },
                "edge": {
                    "type": "str",
                    "choices": [
                        "auto",
                        "no",
                        "no-discover",
                        "yes",
                        "yes-discover",
                    ],
                    "default": "auto",
                },
                "external_fdb": {
                    "type": "str",
                    "choices": ["auto", "no", "yes"],
                    "default": "auto",
                },
                "fast_leave": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "frame_types": {
                    "type": "str",
                    "choices": [
                        "admit-all",
                        "admit-only-untagged-and-priority-tagged",
                        "admit-only-vlan-tagged",
                    ],
                    "default": "admit-all",
                },
                "ingress_filtering": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "learn": {
                    "type": "str",
                    "choices": ["auto", "no", "yes"],
                    "default": "auto",
                },
                "multicast_router": {
                    "type": "str",
                    "choices": ["disabled", "permanent", "temporary-query"],
                    "default": "temporary-query",
                },
                "horizon": {"type": "int", "default": 0},
                "internal_path_cost": {"type": "int", "default": 10},
                "interface": {"type": "str", "required": True},
                "path_cost": {"type": "int", "default": 10},
                "point_to_point": {
                    "type": "str",
                    "choices": ["auto", "no", "yes"],
                    "default": "auto",
                },
                "priority": {"type": "int", "default": 128},
                "pvid": {"type": "int", "default": 1},
                "restricted_role": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "restricted_tcn": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "tag_stacking": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "trusted": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "unknown_multicast_flood": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "yes",
                },
                "unknown_unicast_flood": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "yes",
                },
                "comment": {"type": "str"},
            },
        },
    }