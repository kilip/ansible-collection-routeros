from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class UserResource(ResourceBase):
    resource_name = "user"
    command_root = "/user"
    related_resources = []
    gather_network_resources = ["user"]
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
                "group": {"type": "str"},
                "name": {"type": "str", "required": True},
                "password": {"type": "str"},
                "last_logged_in": {"type": "str"},
                "comment": {"type": "str"},
            },
        },
    }
