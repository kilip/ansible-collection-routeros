# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..compat.mock import patch
from .utils import set_module_args
from .routeros_module import TestRouterOSModule, load_fixture
from ansible_collections.kilip.routeros.plugins.modules import ros_facts


class TestROSFactsModule(TestRouterOSModule):

    module = ros_facts

    def setUp(self):
        TestRouterOSModule.setUp(self)
        self.mock_run_commands = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.legacy.run_commands"
        )
        self.run_commands = self.mock_run_commands.start()

    def load_from_file(*args, **kwargs):
        commands = kwargs["commands"]
        output = list()
        for command in commands:
            filename = str(command).replace(" ", "_").replace("/", "")
            output.append(load_fixture("legacy_facts/{0}".format(filename)))
        return output

    def load_fixtures(self, commands=None):
        self.run_commands.side_effect = self.load_from_file

    def test_gather_legacy_facts(self):
        set_module_args(dict(gather_subset="all"))
        result = self.execute_module(changed=False)

        self.assertEqual(
            result["ansible_facts"]["ansible_net_model"],
            "RouterBOARD 3011UiAS",
        )
