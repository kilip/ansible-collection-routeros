from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.plugins.modules import ros_bridge
from ansible_collections.kilip.routeros.plugins.module_utils.utils import (
    gen_remove_invalid_resource,
)
from .utils import set_module_args
from .resource_module import TestResourceModule


class TestROSBridgeModule(TestResourceModule):

    module = ros_bridge

    def test_merged(self):
        set_module_args(dict(config=[dict(name="br-new")]))
        commands = ["/interface bridge add name=br-new"]
        self.execute_module(False, True, commands)

    def test_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(name="br-trunk", mtu=2000),
                    dict(name="br-wan", mtu=2000),
                    dict(name="br-new"),
                ],
                state="replaced",
            )
        )
        commands = [
            "/interface bridge set [ find name=br-trunk ] vlan-filtering=no",
            "/interface bridge set [ find name=br-trunk ] mtu=2000",
            "/interface bridge set [ find name=br-wan ] vlan-filtering=no",
            "/interface bridge set [ find name=br-wan ] mtu=2000",
            "/interface bridge add name=br-new",
        ]
        self.execute_module(False, True, commands)

    def test_overridden(self):
        set_module_args(dict(config=[dict(name="br-new")], state="overridden"))
        commands = [
            "/interface bridge remove [ find name=br-trunk ]",
            "/interface bridge remove [ find name=br-wan ]",
            "/interface bridge add name=br-new",
            gen_remove_invalid_resource(),
        ]
        self.execute_module(False, True, commands)

    def test_delete(self):
        set_module_args(dict(config=[dict(name="br-trunk")], state="deleted"))
        commands = [
            "/interface bridge remove [ find name=br-trunk ]",
            gen_remove_invalid_resource(),
        ]
        self.execute_module(False, True, commands)
