from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from .base import FactsBase
from ..resource.interface import InterfaceResource


class InterfaceFacts(FactsBase):

    resource = InterfaceResource()

    def additional_config(self, spec, conf):
        config = {}
        match = re.search(r"(\S+)", conf, re.M)
        if match:
            intype = match.group(1).strip()
            config["type"] = self._get_interface_type(intype)

        return config

    def _get_interface_type(self, type):
        intype = "unknown"
        known_types = ["ethernet", "bridge", "vlan"]
        if type.lower() in known_types:
            intype = type.lower()
        return intype
