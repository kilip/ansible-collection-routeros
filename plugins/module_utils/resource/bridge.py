from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .base import ResourceBase

class BridgeResource(ResourceBase):
    argument_spec = {
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                # general section
                "name": {"type": "str", "required": True},
                "comment": {"type": "str"},
                "mtu": {
                    "type": "string",
                },
                "arp": {
                    "choices": [
                        "disabled",
                        "enabled",
                        "local-proxy-arp",
                        "proxy-arp"
                        "reply-only"
                    ],
                    "type": "str"
                },
                "arp_timeout": {"type": "str"},  # in mikrotik time
                "admin_mac": {
                    "type": "string"
                },
                "ageing_time": {"type": "str"},  # in mikrotik time
                "fast_forward": {"type": "bool", "default": None},
                "igmp_snooping": {"type": "bool", "default": None},
                "dhcp_snooping": {
                    "type": "bool",
                    "default": None
                },

                # stp section
                "stp": {
                    "type": "dict",
                    "options": {
                        "protocol_mode": {
                            "choices": [
                                "mstp",
                                "none"
                                "rstp"
                                "stp"
                            ],
                            "type": "str"
                        },
                        "priority": {
                            "type": "str"  # actual type is hex
                        },
                        "max_message_age": {"type": "str"},  # in mikrotik time
                        "forward_delay": {"type": "str"},  # in mikrotik time
                        "transmit_hold_count": {
                            "type": "int"
                        },
                        "max_hops": {"type": "int"},
                    },
                },

                # vlan section
                "vlan": {
                    "type": "dict",
                    "options": {
                        "vlan_filtering": {"type": "bool"},
                        "ether_type": {
                            "choices": ["0x8100", "0x88a8", "0x9100"],
                            "type": "str"
                        },
                        "pvid": {"type": "int"},
                        "frame_types": {
                            "choices": [
                                "admit-all",
                                "admit-only-untagged-and-priority-tagged",
                                "admit-only-vlan-tagged",
                            ],
                            "type": "str"
                        },
                        "ingress_filtering": {"type": "bool", "default": None},
                    }
                },

                # unknown sections
                "add_dhcp_option82": {
                    "type": "bool",
                    "default": None
                },
                "igmp_version": {
                    "choices": [1, 2],
                    "type": "int"
                },
                "querier_interval": {
                    "type": "int"
                },
                "disabled": {
                    "type": "bool"
                },
                "multicast_querier": {"type": "bool", "default": None},
                "query_interval": {"type": "int"},
                "multicast_router": {
                    "choices": ["disabled", "permanent", "temporary-query"],
                    "type": "str"
                },
                "region_name": {"type": "str"},
                "auto_mac": {"type": "bool", "default": None},
            }
        },
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
            ],
            "type": "str",
            "default": "merged"
        }
    }
    resource_name = "bridges"
    command_root = "/interface bridge"
    related_resources = [
        "/ip firewall",
        "/ip address",
        "/ip bridge port",
        "/ip dhcp-server",
    ]
    gather_network_resources = ["bridges"]
    filters = []