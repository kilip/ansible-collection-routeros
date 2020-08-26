# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.tests.unit.compat.mock import patch
from ansible_collections.kilip.routeros.plugins.modules import routeros_interfaces
from ansible_collections.kilip.routeros.tests.unit.modules.utils import (
    set_module_args,
)
from .routeros_module import TestRouterOSModule, load_fixture


class TestRouterosInterfacesModule(TestRouterOSModule):
    module = routeros_interfaces

    def setUp(self):
        super(TestRouterosInterfacesModule, self).setUp()
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
                return dict(diff=None, session="session", results=[],requests=[])

        self.run_commands.side_effect = load_from_file
        #self.load_config.return_value = dict(diff=None, session="session", results=[],requests=[])

    def test_configure_interfaces(self):
        set_module_args(
            {
                'config': [
                    dict(
                        name="ether1",
                        comment="ether1 update comment"
                    )
                ]
            }
        )
        commands = [
            '/interface ethernet set [ find name=ether1 ] comment="ether1 update comment"'
        ]
        self.execute_module(False, True, commands=commands)

    def test_idempotence(self):
        set_module_args(
            {
                'config': [
                    dict(
                        name="ether1",
                        comment="ether1 comment"
                    )
                ]
            }
        )
        commands = []
        self.execute_module(False, False, commands=commands)

