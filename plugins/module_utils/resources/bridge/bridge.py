from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class BridgeResource(ResourceBase):
    resource_name = "bridge"
    command_root = "/interface bridge"
    related_resources = []
    gather_network_resources = ["bridge"]
    resource_keys = ["name"]
    config_type = "plural"
    argument_spec = {
        "running_config": {"type": "str"},
        "state": {
            "choices": ["merged", "replaced", "deleted", "overridden"],
            "default": "merged",
            "type": "str",
        },
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                "add_dhcp_option82": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "admin_mac": {"type": "str"},
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
                "arp_timeout": {
                    "type": "str",
                    "choices": ["auto", "integer"],
                    "default": "auto",
                },
                "auto_mac": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "comment": {"type": "str"},
                "dhcp_snooping": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "disabled": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "ether_type": {
                    "type": "str",
                    "choices": ["0x9100", "0x8100", "0x88a8"],
                    "default": "0x8100",
                },
                "fast_forward": {
                    "type": "str",
                    "choices": ["yes", "no"],
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
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "igmp_version": {
                    "type": "str",
                    "choices": ["2", "3"],
                    "default": "2",
                },
                "ingress_filtering": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "last_member_interval": {"type": "str", "default": "1s"},
                "last_member_query_count": {"type": "str", "default": "2"},
                "max_hops": {"type": "str", "default": "20"},
                "max_message_age": {"type": "str", "default": "00:00:20"},
                "membership_interval": {"type": "str", "default": "4m20s"},
                "mld_version": {
                    "type": "str",
                    "choices": ["1", "2"],
                    "default": "1",
                },
                "mtu": {"type": "str", "default": "1500"},
                "multicast_querier": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "multicast_router": {
                    "type": "str",
                    "choices": ["disabled", "permanent", "temporary-query"],
                    "default": "temporary-query",
                },
                "name": {"type": "str", "required": True},
                "priority": {"type": "int"},
                "protocol_mode": {
                    "type": "str",
                    "choices": ["none", "rstp", "stp", "mstp"],
                    "default": "rstp",
                },
                "pvid": {"type": "str", "default": "1"},
                "querier_interval": {"type": "str", "default": "4m15s"},
                "query_interval": {"type": "str", "default": "2m5s"},
                "query_response_interval": {"type": "str", "default": "10s"},
                "region_name": {"type": "str"},
                "region_revision": {"type": "str"},
                "startup_query_count": {"type": "str", "default": "2"},
                "startup_query_interval": {
                    "type": "str",
                    "default": "31s250ms",
                },
                "transmit_hold_count": {"type": "str", "default": "6"},
                "vlan_filtering": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
            },
        },
    }
