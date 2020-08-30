from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class PppoeClientResource(ResourceBase):
    resource_name = "pppoe_client"
    command_root = "/interface pppoe-client"
    related_resources = []
    gather_network_resources = ["pppoe_client"]
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
                "allow": {
                    "type": "list",
                    "elements": "str",
                    "choices": ["mschap2", "mschap1", "chap", "pap"],
                    "default": ["mschap2", "mschap1", "chap", "pap"],
                },
                "mrru": {"type": "str", "default": "disabled"},
                "ac_name": {"type": "str"},
                "add_default_route": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "default_route_distance": {"type": "bytes"},
                "dial_on_demand": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "interface": {"type": "str"},
                "keepalive_timeout": {"type": "int"},
                "max_mru": {"type": "str", "default": "1460"},
                "max_mtu": {"type": "str", "default": "1460"},
                "name": {"type": "str", "required": True},
                "password": {"type": "str"},
                "profile": {"type": "str", "default": "default"},
                "service_name": {"type": "str"},
                "use_peer_dns": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "user": {"type": "str"},
                "comment": {"type": "str"},
            },
        },
    }
