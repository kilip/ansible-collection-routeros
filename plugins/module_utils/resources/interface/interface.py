from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from ..base import ResourceBase
from ...utils import parse_config


class InterfaceResource(ResourceBase):
    """
    Class InterfaceResource defines configuration for /interface command
    """

    supported_interfaces = ["ethernet", "bridge", "vlan"]
    resource_name = "interface"
    command_root = "/interface"
    gather_network_resources = ["interface"]
    use_verbose_mode = True
    argument_spec = {
        "running_config": {"type": "str"},
        "state": {"choices": ["merged"], "default": "merged", "type": "str"},
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                "comment": {"type": "str"},
                "l2mtu": {"type": "int"},
                "mtu": {"type": "int"},
                "name": {"type": "str", "required": True},
            },
        },
    }

    def render_config(self, spec, conf):
        sp = re.split("set |add ", conf)
        intype = sp[0].strip()
        if intype not in self.supported_interfaces:
            return None
        del sp[0]

        configs = []
        for conf in sp:
            config = parse_config(
                spec, conf, self.facts_argument_spec, self.key_prefixes
            )
            config["type"] = intype
            if config:
                configs.append(config)
        return configs
