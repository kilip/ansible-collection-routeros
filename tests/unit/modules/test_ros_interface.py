from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.plugins.modules import ros_interface
from .utils import set_module_args
from .resource_module import TestResourceModule


class TestROSInterfaceModule(TestResourceModule):

    module = ros_interface

    def test_failed_state_mode(self):
        args = dict(config=[dict(name="ether1", comment="test comment")])

        args["state"] = "replaced"
        set_module_args(args)
        self.execute_module(True)

    def test_merged(self):
        set_module_args(
            dict(config=[dict(name="ether1", comment="test comment")])
        )

        commands = [
            '/interface set [ find name=ether1 ] comment="test comment"'
        ]
        self.execute_module(False, True, commands)
