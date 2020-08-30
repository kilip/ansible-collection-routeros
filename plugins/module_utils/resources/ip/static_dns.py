from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class StaticDnsResource(ResourceBase):
    resource_name = "static_dns"
    command_root = "/ip dns static"
    related_resources = []
    gather_network_resources = ["static_dns"]
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
                "address": {"type": "str"},
                "name": {"type": "str", "required": True},
                "regex": {"type": "str"},
                "ttl": {"type": "str"},
                "type": {"type": "str"},
                "comment": {"type": "str"},
            },
        },
    }
