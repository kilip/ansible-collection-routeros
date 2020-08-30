from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class FirewallAddressListResource(ResourceBase):
    resource_name = "firewall_address_list"
    command_root = "/ip firewall address-list"
    related_resources = []
    gather_network_resources = ["firewall_address_list"]
    resource_keys = ["list", "address"]
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
                "list": {"type": "str", "required": True},
                "timeout": {"type": "str"},
                "comment": {"type": "str"},
            },
        },
    }
