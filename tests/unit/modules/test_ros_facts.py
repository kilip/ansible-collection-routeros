# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..compat.mock import patch
from ansible_collections.kilip.routeros.plugins.modules import ros_facts
from .utils import set_module_args
from .routeros_module import TestRouterOSModule


class TestROSFactsModule(TestRouterOSModule):

    module = ros_facts

    def setUp(self):
        super(TestROSFactsModule, self).setUp()
        self.mock_run_commands = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.legacy.run_commands"
        )
        self.run_commands = self.mock_run_commands.start()

        self.mock_routeros = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.run_commands"
        )
        self.routeros = self.mock_routeros.start()

    def load_fixtures(self, commands=None):
        self.run_commands.side_effect = self.load_from_file
        self.routeros.side_effect = self.load_from_file

    def gather_network_resource(self, name):
        set_module_args(dict(gather_network_resources=name))
        result = self.execute_module()
        return result["ansible_facts"]["ansible_network_resources"][name]

    def test_gather_legacy_facts(self):
        set_module_args(dict(gather_subset="all"))
        result = self.execute_module(changed=False)

        self.assertEqual(
            result["ansible_facts"]["ansible_net_model"],
            "RouterBOARD 3011UiAS",
        )

    def test_gather_interface_facts(self):
        set_module_args(dict(gather_network_resources="interface"))

        result = self.execute_module()
        interfaces = result["ansible_facts"]["ansible_network_resources"][
            "interface"
        ]
        self.assertEqual(len(interfaces), 15)

    def test_gather_bridge_facts(self):
        set_module_args(dict(gather_network_resources="bridge"))

        result = self.execute_module()
        bridges = result["ansible_facts"]["ansible_network_resources"][
            "bridge"
        ]
        self.assertEqual(len(bridges), 2)
        bridge1 = bridges[0]
        bridge2 = bridges[1]

        self.assertEqual(bridge1["name"], "br-trunk")
        self.assertEqual(bridge2["name"], "br-wan")

    def test_gather_bridge_settings(self):
        result = self.gather_network_resource("bridge_settings")
        self.assertTrue(result["use_ip_firewall"])
        self.assertTrue(result["use_ip_firewall_for_pppoe"])
        self.assertTrue(result["use_ip_firewall_for_vlan"])
        self.assertFalse(result["allow_fast_path"])

    def test_gather_vlan(self):
        result = self.gather_network_resource("vlan")
        vlan1 = result[0]
        vlan2 = result[1]

        self.assertEqual(vlan1["interface"], "br-trunk")
        self.assertEqual(vlan2["interface"], "br-trunk")

    def test_bridge_port(self):
        result = self.gather_network_resource("bridge_port")
        port1 = result[0]
        port2 = result[1]
        port3 = result[2]

        self.assertEqual(port1["bridge"], "br-wan")
        self.assertEqual(port1["interface"], "ether1")

        self.assertEqual(port2["bridge"], "br-local")
        self.assertEqual(port2["interface"], "ether2")

        self.assertEqual(port3["bridge"], "br-local")
        self.assertEqual(port3["interface"], "ether3")

    def test_group(self):
        result = self.gather_network_resource("group")
        group = result[0]
        self.assertEqual(group["name"], "group1")
        self.assertEqual(group["policy"], ["reboot", "!api"])

    def test_capsman_configuration(self):
        result = self.gather_network_resource("capsman_configuration")
        config = result[0]
        print(config)
        self.assertEqual(config["datapath_bridge"], "br-trunk")
