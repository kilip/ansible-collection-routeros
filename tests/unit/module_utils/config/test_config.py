from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ...compat.unittest import TestCase
from ...compat.mock import patch
from ...modules.utils import (
    set_module_args,
)
from ...modules.routeros_module import (
    load_fixture
)
from .....plugins.module_utils.config.config import Config
from .....plugins.module_utils.resources.bridge.bridge import BridgeResource

fix_call = 0


class TestConfig(TestCase):

    def setUp(self):
        TestCase.setUp(self)

        self.mock_get_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.run_commands"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.load_config"
        )
        self.load_config = self.mock_load_config.start()

    def load_fixture(*args, **kwargs):
        global fix_call
        cmds = [
            "override.pre",
            "override.post"
        ]

        key = 0
        if fix_call > 2:
            key = 1
        fix_call += 1
        ret = load_fixture("test-config/" + cmds[key])
        return [ret]

    def _execute_module(self):
        self.load_config.side_effect = dict(
            diff=None, session="session", results=[], requests=[]
        )
        self.module = AnsibleModule(BridgeResource.argument_spec)
        self.config = Config(self.module, BridgeResource)
        return self.config.execute_module()

    def test_overridden(self):
        set_module_args(dict(
            state="overridden",
            config=[
                dict(name="br-trunk", comment="override")
            ]
        ))
        self.get_config.side_effect = self.load_fixture
        result = self._execute_module()
        self.assertTrue(result["changed"])

        result = self._execute_module()
        self.assertFalse(result["changed"])
