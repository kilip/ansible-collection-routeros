# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..compat.mock import patch
#from ansible_collections.kilip.routeros.tests.unit.compat.mock import patch
from ansible_collections.kilip.routeros.plugins.modules import routeros_facts
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.kilip.routeros.tests.unit.modules.utils import (
    set_module_args,
)
from .routeros_module import TestRouterOSModule, load_fixture


class TestRouterosFactsModule(TestRouterOSModule):
    module = routeros_facts

    def setUp(self):
        super(TestRouterosFactsModule, self).setUp()
        self.mock_run_commands = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.base.run_commands"
        )
        self.run_commands = self.mock_run_commands.start()

        self.mock_get_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.interfaces.get_config"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_bridge_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.bridges.get_config"
        )
        self.bridge_get_config = self.mock_bridge_config.start()

    def load_fixtures(self, commands=None):
        def load_from_file(*args, **kwargs):
            commands = kwargs["commands"]
            output = list()
            for command in commands:
                filename = str(command).replace(" ", "_")
                output.append(load_fixture("routeros_facts%s.cfg" % filename))
            return output

        def load_config_from_file(*args, **kwargs):
            command = args[1]
            filename = str(command).replace(" ", "_")
            output = load_fixture("routeros_facts%s.cfg" % filename)
            return output

        self.run_commands.side_effect = load_from_file
        self.get_config.side_effect = load_config_from_file
        self.bridge_get_config.side_effect = load_config_from_file

    def test_gather_legacy_facts(self):
        set_module_args(dict(
            gather_subset="all"
        ))
        result = self.execute_module(changed=False)

        self.assertEqual(
            result["ansible_facts"]["ansible_net_model"],
            "RouterBOARD 3011UiAS"
        )

    def test_gather_interfaces_facts(self):
        set_module_args(
            dict(
                gather_network_resources="interfaces"
            )
        )
        result = self.execute_module()
        ansible_facts = result['ansible_facts']
        resources = ansible_facts['ansible_network_resources']['interfaces']
        ether1 = resources[0]
        self.assertEqual(
            ether1['name'],
            'ether1'
        )
        self.assertEqual(
            ether1['comment'],
            'ether1 comment'
        )

    def test_gather_bridges_facts(self):
        set_module_args(
            dict(
                gather_network_resources="bridges"
            )
        )
        result = self.execute_module()
        facts = result['ansible_facts']
        resources = facts['ansible_network_resources']
        bridges = resources['bridges']
        bridge1 = bridges[0]
        bridge2 = bridges[1]
        self.assertEqual(
            bridge1.get('name'),
            'br-trunk1'
        )
        self.assertEqual(
            bridge2.get('name'),
            'br-trunk2'
        )
        self.assertTrue(bridge1.get("stp") is not None)
        self.assertTrue(bridge1.get("stp") is not None)
        self.assertTrue(bridge1.get("vlan") is not None)
        self.assertEqual(bridge1['vlan']['vlan_filtering'], False)
        self.assertEqual(bridge2['vlan']['vlan_filtering'], True)

