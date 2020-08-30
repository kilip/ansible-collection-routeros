from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class PppoeServerResource(ResourceBase):
    resource_name = "pppoe_server"
    command_root = "/interface pppoe-server"
    related_resources = []
    gather_network_resources = ["pppoe_server"]
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
                "authentication": {
                    "type": "list",
                    "elements": "str",
                    "choices": ["mschap2", "mschap1", "chap", "pap"],
                    "default": None,
                },
                "mrru": {"type": "str", "default": "disabled"},
                "default_profile": {"type": "str", "default": "default"},
                "interface": {"type": "str"},
                "keepalive_timeout": {"type": "str", "default": "10"},
                "max_mru": {"type": "str", "default": "1480"},
                "max_mtu": {"type": "str", "default": "1480"},
                "max_sessions": {"type": "str"},
                "one_session_per_host": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "service_name": {"type": "str"},
                "comment": {"type": "str"},
            },
        },
    }
