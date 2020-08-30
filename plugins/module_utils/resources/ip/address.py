from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class AddressResource(ResourceBase):
    resource_name = "address"
    command_root = "/ip address"
    related_resources = []
    gather_network_resources = ["address"]
    resource_keys = ["address"]
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
                "address": {"type": "str", "required": True},
                "broadcast": {"type": "str", "default": "255.255.255.255"},
                "interface": {"type": "str"},
                "netmask": {"type": "str", "default": "0.0.0.0"},
                "network": {"type": "str", "default": "0.0.0.0"},
                "comment": {"type": "str"},
            },
        },
    }
