# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.tests.unit.compat.mock import patch
from ansible_collections.kilip.routeros.plugins.modules import routeros_interfaces
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.kilip.routeros.tests.unit.modules.utils import (
    set_module_args,
)
from .routeros_module import TestRouterOSModule, load_fixture


class TestRouterosInterfacesModule(TestRouterOSModule):
    module = routeros_interfaces

    def setUp(self):
        super(TestRouterosInterfacesModule, self).setUp()
        self.mock_get_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.interfaces.get_config"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.config.interfaces.load_config"
        )
        self.load_config = self.mock_load_config.start()

    def load_fixtures(self, commands=None):
        def load_from_file(*args, **kwargs):
            commands = kwargs["commands"]
            commands = to_list(commands)
            output = list()
            for command in commands:
                filename = str(command).replace(" ", "_")
                output.append(load_fixture("routeros_interfaces%s.cfg" % filename))
            return "\n".join(output)

        def load_config_from_file(*args, **kwargs):
            command = args[1]
            filename = str(command).replace(" ", "_")
            output = load_fixture("routeros_facts%s.cfg" % filename)
            return output

        self.get_config.side_effect = load_config_from_file
        self.load_config.return_value = dict(diff=None, session="session", results=[],requests=[])

    def test_configure_interfaces(self):
        set_module_args(
            {
                'config': [
                    dict(
                        name="ether1",
                        comment="ether1 config comment"
                    )
                ]
            }
        )
        commands = [
            '/interface ethernet set [ find name=ether1 ] comment="ether1 config comment"'
        ]
        self.execute_module(changed=True, commands=commands)

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
        self.execute_module(changed=False, commands=[])

