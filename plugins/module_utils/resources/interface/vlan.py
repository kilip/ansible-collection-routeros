from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class VlanResource(ResourceBase):
    resource_name = "vlan"
    command_root = "/interface vlan"
    related_resources = []
    gather_network_resources = ["vlan"]
    resource_keys = ["interface", "name"]
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
                "interface": {"type": "str", "required": True},
                "l2mtu": {"type": "int"},
                "mtu": {"type": "str", "default": "1500"},
                "name": {"type": "str", "required": True},
                "use_service_tag": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": None,
                },
                "vlan_id": {"type": "str", "default": "1"},
                "comment": {"type": "str"},
            },
        },
    }
