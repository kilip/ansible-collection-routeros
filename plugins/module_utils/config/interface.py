from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .resource import ConfigResource
from ..resource.interface import InterfaceResource


class Interface(ConfigResource):

    resource = InterfaceResource

    def get_command_prefix(self, want, have):
        """
        This method will be prefixing command with interface type (ethernet, bridge, etc.)

        :param want: the configured resource
        :param have: the existing configuration
        :return: command prefix
        """
        intype = have["type"]
        root = self.resource.command_root
        prefix = f"{root} {intype}"
        return prefix
