from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.plugins.modules import ros_bridge_port
from ansible_collections.kilip.routeros.plugins.module_utils.utils import (
    gen_remove_invalid_resource,
)
from .utils import set_module_args
from .resource_module import TestResourceModule


class TestROSBridgePortModule(TestResourceModule):

    module = ros_bridge_port

    def test_failed_arguments(self):
        # require bridge to be defined
        set_module_args(dict(config=[dict(bridge="test")]))
        self.execute_module(True)

        # require interface to be defined
        set_module_args(dict(config=[dict(interface="foo")]))
        self.execute_module(True)

    def test_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(bridge="br-local", interface="ether2", pvid=100),
                    dict(bridge="br-local", interface="ether10"),
                ]
            )
        )
        commands = [
            "/interface bridge port set [ find bridge=br-local and interface=ether2 ] pvid=100",
            "/interface bridge port add bridge=br-local interface=ether10",
        ]
        self.execute_module(False, True, commands)

    def test_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(bridge="br-local", interface="ether2", pvid=100),
                    dict(bridge="br-local", interface="ether10"),
                ],
                state="replaced",
            )
        )
        commands = [
            "/interface bridge port set [ find bridge=br-local and interface=ether2 ] pvid=1",
            "/interface bridge port set [ find bridge=br-local and interface=ether2 ] pvid=100",
            "/interface bridge port add bridge=br-local interface=ether10",
        ]
        self.execute_module(False, True, commands)

    def test_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(bridge="br-local", interface="ether2", pvid=100),
                    dict(bridge="br-local", interface="ether10"),
                ],
                state="overridden",
            )
        )
        commands = [
            "/interface bridge port remove [ find bridge=br-wan and interface=ether1 ]",
            "/interface bridge port remove [ find bridge=br-local and interface=ether2 ]",
            "/interface bridge port remove [ find bridge=br-local and interface=ether3 ]",
            "/interface bridge port add bridge=br-local interface=ether2 pvid=100",
            "/interface bridge port add bridge=br-local interface=ether10",
            gen_remove_invalid_resource(),
        ]
        self.execute_module(False, True, commands)

    def test_deleted(self):
        set_module_args(
            dict(
                config=[dict(bridge="br-local", interface="ether2")],
                state="deleted",
            )
        )
        commands = [
            "/interface bridge port remove [ find bridge=br-local and interface=ether2 ]",
            gen_remove_invalid_resource(),
        ]
        self.execute_module(False, True, commands)
