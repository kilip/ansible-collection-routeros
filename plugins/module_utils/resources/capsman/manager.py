from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class CapsmanManagerResource(ResourceBase):
    """
    Class CapsmanManager contains definition for `/caps-man manager`
    """

    resource_name = "capsman_manager"
    command_root = "/caps-man manager"
    gather_network_resources = ["capsman_manager"]
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
                "enabled": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "certificate": {
                    "type": "str",
                    "choices": ["auto", "certificate", "name", "none"],
                    "default": None,
                },
                "ca_certificate": {
                    "type": "str",
                    "choices": ["auto", "certificate", "name", "none"],
                    "default": None,
                },
                "require_peer_certificate": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "package_path": {
                    "type": "str",
                    "choices": ["string"],
                    "default": None,
                },
                "upgrade_policy": {
                    "type": "str",
                    "choices": [
                        "none",
                        "require-same-version",
                        "suggest-same-upgrade",
                    ],
                    "default": None,
                },
                "comment": {"type": "str"},
            },
        },
    }
