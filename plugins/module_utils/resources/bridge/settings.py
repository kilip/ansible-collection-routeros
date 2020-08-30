from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class BridgeSettingsResource(ResourceBase):
    """
    Class BridgeSettings contains definition for `/interface bridge settings`
    """

    resource_name = "bridge_settings"
    command_root = "/interface bridge settings"
    gather_network_resources = ["bridge_settings"]
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
                "use_ip_firewall": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "use_ip_firewall_for_pppoe": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "use_ip_firewall_for_vlan": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "allow_fast_path": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "comment": {"type": "str"},
            },
        },
    }
