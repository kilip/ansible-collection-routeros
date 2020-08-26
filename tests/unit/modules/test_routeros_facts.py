# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..compat.mock import patch
from ansible_collections.kilip.routeros.plugins.modules import routeros_facts
from .utils import set_module_args
from .routeros_module import TestRouterOSModule, load_fixture


class TestRouterosFactsModule(TestRouterOSModule):
    module = routeros_facts

    def setUp(self):
        super(TestRouterosFactsModule, self).setUp()
        self.mock_run_commands = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.legacy.run_commands"
        )
        self.run_commands = self.mock_run_commands.start()

        self.mock_routeros = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.run_commands"
        )
        self.routeros = self.mock_routeros.start()

    def load_fixtures(self, commands=None):
        def load_from_file(*args, **kwargs):
            commands = kwargs["commands"]
            output = list()
            for command in commands:
                filename = str(command).replace(" ", "_")
                output.append(load_fixture("routeros_facts%s" % filename))
            return output

        self.run_commands.side_effect = load_from_file
        self.routeros.side_effect = load_from_file

    def test_gather_legacy_facts(self):
        set_module_args(dict(gather_subset="all"))
        result = self.execute_module(changed=False)

        self.assertEqual(
            result["ansible_facts"]["ansible_net_model"],
            "RouterBOARD 3011UiAS",
        )

    def test_interface_facts(self):
        set_module_args(dict(gather_network_resources="interfaces"))
        result = self.execute_module(changed=False)

        interfaces = result["ansible_facts"]["ansible_network_resources"][
            "interfaces"
        ]
        interface1 = interfaces[0]
        interface2 = interfaces[1]

        # interface1 spec
        self.assertEqual(interface1["name"], "ether1")
        self.assertEqual(interface1["type"], "ethernet")
        self.assertEqual(interface1["comment"], "ether1 comment")
        self.assertFalse(interface1["disabled"])

        # interface2 spec
        self.assertEqual(interface2["name"], "foo")
        self.assertEqual(interface2["type"], "bridge")

    def test_bridge_facts(self):
        set_module_args(dict(gather_network_resources="bridges"))
        result = self.execute_module(False, False)
        bridges = result["ansible_facts"]["ansible_network_resources"][
            "bridges"
        ]
        bridge1 = bridges[0]
        bridge2 = bridges[1]

        # bridge 1 assert
        self.assertEqual(bridge1["name"], "br-trunk1")
        self.assertFalse(bridge1["vlan"]["vlan_filtering"])
        self.assertEqual(bridge1["stp"]["protocol_mode"], "rstp")

        # bridge 2 assert
        self.assertEqual(bridge2["name"], "br-trunk2")
        self.assertTrue(bridge2["vlan"]["vlan_filtering"])
        self.assertEqual(bridge2["stp"]["protocol_mode"], "mstp")
