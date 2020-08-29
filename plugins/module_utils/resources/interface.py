from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from .base import ResourceBase


class InterfaceResource(ResourceBase):

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "name": {"type": "str"},
                "comment": {"type": "str"},
                "disabled": {"type": "bool", "default": None},
                "type": {"type": "str"},
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {"choices": ["merged"], "default": "merged", "type": "str"},
    }
    resource_name = "interfaces"
    command_root = "/interface"
    use_verbose_mode = True
    related_resources = []
    gather_network_resources = ["interfaces"]
    value_filters = ["name", "type"]

    def get_command_prefix(self, want, have=None):
        """
        This method will be prefixing command with interface type (ethernet, bridge, etc.)

        :param want: the configured resource
        :param have: the existing configuration
        :return: command prefix
        """
        if have is None:
            have = want

        intype = have["type"]
        root = self.command_root
        prefix = f"{root} {intype}"
        return prefix

    def render_config(self, spec, conf):
        config = super().render_config(spec, conf)
        if config["type"] == "unsupported":
            return {}
        return config

    def _custom_config(self, spec, conf):
        config = {}
        match = re.search(r"(\S+)", conf, re.M)
        if match:
            intype = match.group(1).strip()
            config["type"] = self._get_interface_type(intype)
        return config

    def _get_interface_type(self, type):
        intype = "unsupported"
        known_types = ["ethernet", "bridge", "vlan"]
        if type.lower() in known_types:
            intype = type.lower()
        return intype
