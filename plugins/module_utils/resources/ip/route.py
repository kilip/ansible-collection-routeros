from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class RouteResource(ResourceBase):
    resource_name = "route"
    command_root = "/ip route"
    related_resources = []
    gather_network_resources = ["route"]
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
                "check_gateway": {
                    "type": "str",
                    "choices": ["arp", "ping"],
                    "default": None,
                },
                "comment": {"type": "str"},
                "distance": {"type": "str", "default": "1"},
                "dst_address": {"type": "str", "default": "0.0.0.0/0"},
                "gateway": {
                    "type": "str",
                    "choices": ", ip | string, [..]",
                    "default": None,
                },
                "pref_src": {"type": "str"},
                "route_tag": {"type": "int"},
                "routing_mark": {"type": "str"},
                "scope": {"type": "str", "default": "30"},
                "target_scope": {"type": "str", "default": "10"},
                "type": {
                    "type": "str",
                    "choices": [
                        "unicast",
                        "blackhole",
                        "prohibit",
                        "unreachable",
                    ],
                    "default": "unicast",
                },
                "vrf_interface": {"type": "str", "default": "10"},
            },
        },
    }
