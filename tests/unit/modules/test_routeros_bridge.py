# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.tests.unit.compat.mock import patch
from ansible_collections.kilip.routeros.plugins.modules import routeros_bridge
from ansible_collections.kilip.routeros.plugins.module_utils.utils import (
    gen_remove_invalid_resource,
)
from ansible_collections.kilip.routeros.tests.unit.modules.utils import (
    set_module_args,
)
from .routeros_module import TestRouterOSModule, load_fixture


class TestRouterosBridgeModule(TestRouterOSModule):
    module = routeros_bridge

    def setUp(self):
        super(TestRouterosBridgeModule, self).setUp()
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
                    output.append(load_fixture("routeros_bridge%s" % filename))
                return output
            else:
                return dict(
                    diff=None, session="session", results=[], requests=[]
                )

        self.run_commands.side_effect = load_from_file

    def test_idempotence(self):
        set_module_args(
            dict(
                config=[
                    dict(name="br-trunk1", vlan=dict(vlan_filtering=False))
                ]
            )
        )
        self.execute_module(False, False)

    def test_merged(self):
        set_module_args(
            {
                "config": [
                    dict(name="br-new", comment="br-new comment"),
                    dict(name="br-trunk1", comment="br-trunk1 comment"),
                ]
            }
        )
        commands = [
            '/interface bridge add name=br-new comment="br-new comment"',
            '/interface bridge set [ find name=br-trunk1 ] comment="br-trunk1 comment"',
        ]
        self.execute_module(False, True, commands=commands)

    def test_deleted(self):
        set_module_args(
            dict(
                config=[dict(name="br-trunk1"), dict(name="br-trunk2")],
                state="deleted",
            )
        )
        commands = [
            "/interface bridge remove [ find name=br-trunk1 ]",
            gen_remove_invalid_resource(),
            "/interface bridge remove [ find name=br-trunk2 ]",
            gen_remove_invalid_resource(),
        ]
        self.execute_module(False, True, commands)

    def test_deleted_with_non_existing_resource(self):
        set_module_args(dict(config=[dict(name="br-foo")], state="deleted"))
        self.execute_module(False, False)

    def test_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(name="br-trunk1", vlan=dict(vlan_filtering=True)),
                    dict(name="br-trunk2", vlan=dict(vlan_filtering=True)),
                    dict(name="br-new", comment="new comment"),
                ],
                state="replaced",
            )
        )
        commands = [
            '/interface bridge set [ find name=br-trunk1 ] comment=""',
            "/interface bridge set [ find name=br-trunk1 ] vlan-filtering=yes",
            '/interface bridge set [ find name=br-trunk2 ] comment="" vlan-filtering=no',
            "/interface bridge set [ find name=br-trunk2 ] vlan-filtering=yes",
            '/interface bridge add name=br-new comment="new comment"',
        ]
        self.execute_module(False, True, commands)

    def test_overriden(self):
        set_module_args(
            dict(
                config=[dict(name="br-new", comment="new comment")],
                state="overridden",
            )
        )
        commands = [
            "/interface bridge remove [ find name=br-trunk1 ]",
            gen_remove_invalid_resource(),
            "/interface bridge remove [ find name=br-trunk2 ]",
            gen_remove_invalid_resource(),
            '/interface bridge add name=br-new comment="new comment"',
        ]
        self.execute_module(False, True, commands)
