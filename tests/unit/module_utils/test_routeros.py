from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..compat.unittest import TestCase
from ..compat.mock import patch
from ....plugins.module_utils.routeros import (
    generate_config_key,
    get_config,
    transform_response,
)


class TestRouterOS(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.mock_run_commands = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.run_commands"
        )
        self.run_commands = self.mock_run_commands.start()

        self.mock_module = patch("ansible.module_utils.basic.AnsibleModule")
        self.module = self.mock_module.start()
        self.load_fixture()

    def load_fixture(self):
        def load_config(*args, **kwargs):
            return ["config1", "config2"]

        self.run_commands.side_effect = load_config

    def test_generate_config_key(self):
        key = generate_config_key("/interface foo export verbose terse")
        self.assertEqual("interface_foo", key)

        key = generate_config_key(
            "/interface bridge port add name=foo key=Value"
        )
        self.assertEqual("interface_bridge_port", key)

    def test_get_config(self):
        output = get_config(self.module, "/interface test verbose terse")
        self.assertEqual("config1\nconfig2", output)

    def test_transform_response(self):
        response = """
/interface set [ find name=ether2 ] comment="new comment" dis
< name=ether2 ] comment="new comment" disabled=yes
< name=ether2 ] comment="new comment" disabled=yes
        """

        ret = transform_response("test", response)
        self.assertTrue(ret["success"])

        fail_response = (
            response
            + """

value mismatched

"""
        )
        ret = transform_response("test", fail_response)
        self.assertFalse(ret["success"])
        self.assertEqual(ret["response"], "value mismatched")
