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


class BridgeResource(ResourceBase):
    resource_name = "bridge"
    command = "/interface bridge"
    gather_network_resources = ["bridge"]
    keys = ["name"]
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
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "add_dhcp_option82": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "admin_mac": {"type": "str", "default": "none"},
                "ageing_time": {"type": "str", "default": "00:05:00"},
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
                "arp_timeout": {"type": "str", "default": "auto"},
                "auto_mac": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "yes",
                },
                "comment": {"type": "str"},
                "dhcp_snooping": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "ether_type": {
                    "type": "str",
                    "choices": ["0x8100", "0x88a8", "0x9100"],
                    "default": "0x8100",
                },
                "fast_forward": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "yes",
                },
                "forward_delay": {"type": "str", "default": "00:00:15"},
                "frame_types": {
                    "type": "str",
                    "choices": [
                        "admit-all",
                        "admit-only-untagged-and-priority-tagged",
                        "admit-only-vlan-tagged",
                    ],
                    "default": "admit-all",
                },
                "igmp_snooping": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "igmp_version": {
                    "type": "str",
                    "choices": ["2", "3"],
                    "default": "2",
                },
                "ingress_filtering": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "last_member_interval": {"type": "str", "default": "1s"},
                "last_member_query_count": {"type": "int", "default": 2},
                "max_hops": {"type": "int", "default": 20},
                "max_message_age": {"type": "str", "default": "00:00:20"},
                "membership_interval": {"type": "str", "default": "4m20s"},
                "mld_version": {
                    "type": "str",
                    "choices": ["1", "2"],
                    "default": "1",
                },
                "mtu": {"type": "int", "default": 0},
                "multicast_querier": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
                "multicast_router": {
                    "type": "str",
                    "choices": ["disabled", "permanent", "temporary-query"],
                    "default": "temporary-query",
                },
                "name": {"type": "str", "required": True},
                "priority": {"type": "int", "default": 32768},
                "protocol_mode": {
                    "type": "str",
                    "choices": ["mstp", "none", "rstp", "stp"],
                    "default": "rstp",
                },
                "pvid": {"type": "int", "default": 1},
                "querier_interval": {"type": "str", "default": "4m15s"},
                "query_interval": {"type": "str", "default": "2m5s"},
                "query_response_interval": {"type": "str", "default": "10s"},
                "region_name": {"type": "str"},
                "region_revision": {"type": "int", "default": 0},
                "startup_query_count": {"type": "int", "default": 2},
                "startup_query_interval": {
                    "type": "str",
                    "default": "31s250ms",
                },
                "transmit_hold_count": {"type": "int", "default": 6},
                "vlan_filtering": {
                    "type": "str",
                    "choices": ["no", "yes"],
                    "default": "no",
                },
            },
        },
    }
