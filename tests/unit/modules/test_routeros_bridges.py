# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..compat.mock import patch
from ansible_collections.kilip.routeros.plugins.modules import routeros_bridges
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from .utils import (
    set_module_args,
)
from .routeros_module import TestRouterOSModule, load_fixture


class TestRouterosBridgesModule(TestRouterOSModule):
    module = routeros_bridges

    def setUp(self):
        super(TestRouterosBridgesModule, self).setUp()
        self.mock_get_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.bridges.get_config"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.config.resources.load_config"
        )
        self.load_config = self.mock_load_config.start()

    def load_fixtures(self, commands=None):
        def load_config_from_file(*args, **kwargs):
            command = args[1]
            filename = str(command).replace(" ", "_")
            output = load_fixture("routeros_facts%s.cfg" % filename)
            return output

        self.get_config.side_effect = load_config_from_file
        self.load_config.return_value = dict(diff=None, session="session", results=[],requests=[])

    def test_create_new_bridge(self):
        set_module_args(dict(
            config=[
                dict(
                    name="br-new1",
                    comment="br-new1 comment",
                    vlan=dict(vlan_filtering=True)
                ),
                dict(
                    name="br-new2",
                    comment="br-new2 comment",
                    vlan=dict(vlan_filtering=False)
                )
            ]
        ))
        commands = [
            '/interface bridge add name=br-new1 comment="br-new1 comment" vlan-filtering=yes',
            '/interface bridge add name=br-new2 comment="br-new2 comment" vlan-filtering=no',
        ]
        self.execute_module(changed=True, commands=commands)

    def test_update_existing_bridge(self):
        set_module_args(dict(
            config=[
                dict(
                    name="br-trunk1",
                    comment="br-trunk1 comment",
                    vlan=dict(vlan_filtering=True)
                )
            ],
        ))
        commands = [
            '/interface bridge set [ find name=br-trunk1 ] comment="br-trunk1 comment" vlan-filtering=yes'
        ]
        self.execute_module(changed=True, commands=commands)

    def test_delete_existing_bridge(self):
        set_module_args(dict(
            config=[
                dict(
                    name="br-trunk1",
                )
            ],
            state="deleted"
        ))
        commands = [
            '/interface bridge remove [ find name=br-trunk1 ]'
        ]
        self.execute_module(changed=True, commands=commands)
