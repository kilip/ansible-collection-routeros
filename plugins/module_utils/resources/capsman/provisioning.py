from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class CapsmanProvisioningResource(ResourceBase):
    resource_name = "capsman_provisioning"
    command_root = "/caps-man provisioning"
    related_resources = []
    gather_network_resources = ["capsman_provisioning"]
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
                "action": {
                    "type": "str",
                    "choices": [
                        "create-disabled",
                        "create-enabled",
                        "create-dynamic-enabled",
                        "none",
                    ],
                    "default": None,
                },
                "comment": {"type": "str"},
                "common_name_regexp": {"type": "str"},
                "hw_supported_modes": {
                    "type": "str",
                    "choices": [
                        "a",
                        "a-turbo",
                        "ac",
                        "an",
                        "b",
                        "g",
                        "g-turbo",
                        "gn",
                    ],
                    "default": None,
                },
                "identity_regexp": {"type": "str"},
                "ip_address_ranges": {"type": "str"},
                "master_configuration": {"type": "str"},
                "name_format": {
                    "type": "str",
                    "choices": [
                        "cap",
                        "identity",
                        "prefix",
                        "prefix-identity",
                    ],
                    "default": "cap",
                },
                "name_prefix": {"type": "str"},
                "radio_mac": {"type": "str", "default": "00:00:00:00:00:00"},
                "slave_configurations": {"type": "str"},
            },
        },
    }
