from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class CapsmanChannelsResource(ResourceBase):
    resource_name = "capsman_channels"
    command_root = "/caps-man channels"
    related_resources = []
    gather_network_resources = ["capsman_channels"]
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
                "band": {
                    "type": "str",
                    "choices": [
                        "2ghz-b",
                        "2ghz-b/g",
                        "2ghz-b/g/n",
                        "2ghz-onlyg",
                        "2ghz-onlyn",
                        "5ghz-a",
                        "5ghz-a/n",
                        "5ghz-onlyn",
                    ],
                    "default": None,
                },
                "comment": {"type": "str"},
                "extension_channel": {
                    "type": "str",
                    "choices": [
                        "ce",
                        "ceee",
                        "ec",
                        "ecee",
                        "eece",
                        "eeec",
                        "disabled",
                    ],
                    "default": None,
                },
                "frequency": {"type": "int"},
                "name": {"type": "str", "required": True},
                "tx_power": {"type": "int"},
                "width": {"type": "str"},
                "save_selected": {"type": "str", "default": "yes"},
            },
        },
    }
