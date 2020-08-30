from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class GroupResource(ResourceBase):
    resource_name = "group"
    command_root = "/user group"
    related_resources = []
    gather_network_resources = ["group"]
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
                "policy": {
                    "type": "list",
                    "elements": "str",
                    "choices": [
                        "local",
                        "telnet",
                        "ssh",
                        "ftp",
                        "reboot",
                        "read",
                        "write",
                        "policy",
                        "test",
                        "winbox",
                        "password",
                        "web",
                        "sniff",
                        "sensitive",
                        "api",
                        "romon",
                        "dude",
                        "tikapp",
                        "!local",
                        "!telnet",
                        "!ssh",
                        "!ftp",
                        "!reboot",
                        "!read",
                        "!write",
                        "!policy",
                        "!test",
                        "!winbox",
                        "!password",
                        "!web",
                        "!sniff",
                        "!sensitive",
                        "!api",
                        "!romon",
                        "!dude",
                        "!tikapp",
                    ],
                    "default": None,
                },
                "name": {"type": "str", "required": True},
                "skin": {"type": "str", "default": "default"},
                "comment": {"type": "str"},
            },
        },
    }
