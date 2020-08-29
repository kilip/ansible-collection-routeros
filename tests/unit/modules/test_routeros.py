# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.tests.unit.compat.mock import patch
from ansible_collections.kilip.routeros.plugins.modules import routeros
from .utils import set_module_args
from .routeros_module import TestRouterOSModule, load_fixture


class TestRouterosBridgeModule(TestRouterOSModule):
    module = routeros

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
                resource="interface",
                config=[dict(name="ether1")],
                state="deleted",
            )
        )
        self.execute_module(False, False)

    def test_merged(self):
        set_module_args(
            dict(
                resource="bridge",
                config=[dict(name="br-wan", comment="WAN Bridge")],
                state="merged",
            )
        )
        commands = ['/interface bridge add name=br-wan comment="WAN Bridge"']
        self.execute_module(False, True, commands)
