from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .base import ResourceBase

class InterfaceResource(ResourceBase):
    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "name": {"type": "str"},
                "comment": {"type": "str"},
                "disabled": {"type": "bool", "default": None},
                "type": {"type": "str"}
            },
            "type": "list"
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
            ],
            "default": "merged",
            "type": "str",
        },
    }
    resource_name = "interfaces"
    command_root = "/interface"
    related_resources = []
    gather_network_resources = ["interfaces"]
    filters = ['type']