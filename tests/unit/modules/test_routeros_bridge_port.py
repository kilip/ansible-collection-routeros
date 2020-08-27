# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.tests.unit.compat.mock import patch
from ansible_collections.kilip.routeros.plugins.modules import (
    routeros_bridge_port,
)
from ansible_collections.kilip.routeros.tests.unit.modules.utils import (
    set_module_args,
)
from ansible_collections.kilip.routeros.plugins.module_utils.utils import (
    gen_remove_invalid_resource,
)
from .routeros_module import TestRouterOSModule, load_fixture


class TestRouterosBridgePortModule(TestRouterOSModule):
    module = routeros_bridge_port

    def setUp(self):
        super(TestRouterosBridgePortModule, self).setUp()
        self.mock_run_commands = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.run_commands"
        )
        self.run_commands = self.mock_run_commands.start()

    def load_fixtures(self, commands=None):
        def load_from_file(*args, **kwargs):
            if kwargs.get("commands") is not None:
                commands = kwargs["commands"]
                output = list()
                for command in commands:
                    filename = str(command).replace(" ", "_")
                    output.append(load_fixture("routeros_facts%s" % filename))
                return output
            else:
                return dict(
                    diff=None, session="session", results=[], requests=[]
                )

        self.run_commands.side_effect = load_from_file

    def test_idempotence(self):
        set_module_args(
            {
                "config": [
                    dict(
                        bridge="br-wan",
                        interface="ether1",
                        stp=dict(auto_isolate=True),
                    )
                ]
            }
        )
        self.execute_module()

    def test_deleted(self):
        set_module_args(
            {
                "config": [dict(bridge="br-wan", interface="ether1")],
                "state": "deleted",
            }
        )
        commands = [
            "/interface bridge port remove [ find bridge=br-wan and interface=ether1 ]"
        ]
        self.execute_module(False, True, commands)

    def test_merged(self):
        set_module_args(
            {
                "config": [
                    dict(bridge="br-new", interface="ether3"),
                    dict(
                        bridge="br-trunk",
                        interface="ether2",
                        vlan=dict(tag_stacking=True),
                    ),
                ]
            }
        )
        commands = [
            "/interface bridge port add bridge=br-new interface=ether3",
            "/interface bridge port set [ find bridge=br-trunk and interface=ether2 ] tag-stacking=yes",
        ]
        self.execute_module(False, True, commands=commands)

    def test_replaced(self):
        set_module_args(
            {
                "config": [
                    dict(
                        bridge="br-wan",
                        interface="ether1",
                        vlan=dict(tag_stacking=False),
                    ),
                    dict(bridge="br-new", interface="ether3")
                ],
                "state": "replaced",
            }
        )
        commands = [
            "/interface bridge port set [ find bridge=br-wan and interface=ether1 ] tag-stacking=no",
            "/interface bridge port add bridge=br-new interface=ether3",
        ]
        self.execute_module(False, True, commands=commands)

    def test_overriden(self):
        set_module_args(
            {
                "config": [
                    dict(
                        bridge="br-wan",
                        interface="ether1",
                        vlan=dict(tag_stacking=False),
                    ),
                    # dict(bridge="br-trunk", interface="ether2")
                ],
                "state": "overridden",
            }
        )
        commands = [
            '/interface bridge port remove [ find bridge=br-wan and interface=ether1 ]',
            '/interface bridge port remove [ find bridge=br-trunk and interface=ether2 ]',
            '/interface bridge port add bridge=br-wan interface=ether1 tag-stacking=no',
        ]
        self.execute_module(False, True, commands)
