from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class CapsmanAaaResource(ResourceBase):
    """
    Class CapsmanAaa contains definition for `/caps-man aaa`
    """

    resource_name = "capsman_aaa"
    command_root = "/caps-man aaa"
    gather_network_resources = ["capsman_aaa"]
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
                "mac_format": {"type": "str", "default": "xx:xx:xx:xx:xx:xx"},
                "mac_mode": {
                    "type": "str",
                    "choices": ["as-username", "as-username-and-password"],
                    "default": None,
                },
                "mac_caching": {
                    "type": "str",
                    "choices": ["disabled", "time-interval"],
                    "default": "disabled",
                },
                "interim_update": {
                    "type": "str",
                    "choices": ["disabled", "time-interval"],
                    "default": "disabled",
                },
                "called_format": {
                    "type": "str",
                    "choices": ["mac", "mac"],
                    "default": "mac:ssid",
                },
                "comment": {"type": "str"},
            },
        },
    }
