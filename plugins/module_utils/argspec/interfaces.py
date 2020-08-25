from __future__ import absolute_import, division, print_function

__metaclass__ = type


class InterfacesArgs(object):
    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "name": {"type": "str"},
                "comment": {"type": "str"},
                "disabled": {"type": "bool", "default": None},
                "type": {
                    "choices": ["ethernet", "bridge", "vlan"],
                    "type": "str"
                }
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
