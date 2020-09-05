# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..compat.mock import patch
from .routeros_module import TestRouterOSModule


class TestResourceModule(TestRouterOSModule):
    def setUp(self):
        TestRouterOSModule.setUp(self)
        self.mock_run_commands = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.run_commands"
        )
        self.run_commands = self.mock_run_commands.start()
        self.mock_load_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.config.resource.load_config"
        )
        self.load_config = self.mock_load_config.start()

    def load_fixtures(self, commands=None):
        self.run_commands.side_effect = self.load_from_file
        self.load_config.return_value = dict(
            diff=None, session="session", results=[], requests=[]
        )
