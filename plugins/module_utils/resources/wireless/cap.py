from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class WirelessCapResource(ResourceBase):
    """
    Class WirelessCap contains definition for `/interface wireless cap`
    """

    resource_name = "wireless_cap"
    command_root = "/interface wireless cap"
    gather_network_resources = ["wireless_cap"]
    resource_keys = ["name"]
    config_type = "singular"
    argument_spec = {
        "running_config": {"type": "str"},
        "state": {
            "choices": ["present", "reset"],
            "default": "present",
            "type": "str",
        },
        "config": {
            "type": "dict",
            "options": {
                "interfaces": {"type": "list", "elements": "str"},
                "discovery_interfaces": {"type": "list", "elements": "str"},
                "caps_man_addressess": {"type": "list", "elements": "str"},
                "caps_man_names": {"type": "list", "elements": "str"},
                "caps_man_certificate_common_names": {
                    "type": "list",
                    "elements": "str",
                },
                "static_virtual": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "enabled": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "certificate": {
                    "type": "str",
                    "choices": ["certificate", "name", "none"],
                    "default": None,
                },
                "caps_man_addresses": {"type": "str", "default": "empty"},
                "bridge": {"type": "str"},
                "comment": {"type": "str"},
            },
        },
    }
