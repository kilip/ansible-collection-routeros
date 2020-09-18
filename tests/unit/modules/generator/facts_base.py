from __future__ import absolute_import, division, print_function

__metaclass__ = type

import yaml
import os
from ansible_collections.kilip.routeros.plugins.modules import ros_facts
from ...compat.mock import patch
from ..utils import set_module_args
from ..routeros_module import TestRouterOSModule, load_fixture


class TestFactsBase(TestRouterOSModule):
    fixture_file = ""
    config = dict()
    currentFixtures = ""
    module = ros_facts

    def setUp(self):
        TestRouterOSModule.setUp(self)

        self.config = self.load_facts_fixtures()
        self.currentFixtures = self.config.get("fixtures")

        self.mock_run_commands = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.legacy.run_commands"
        )
        self.run_commands = self.mock_run_commands.start()

        self.mock_routeros = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.resource.get_config"
        )
        self.routeros = self.mock_routeros.start()

    def load_from_file(*args, **kwargs):
        commands = kwargs["commands"]
        output = list()
        for command in commands:
            filename = str(command).replace(" ", "_").replace("/", "")
            output.append(load_fixture("legacy_facts/{0}".format(filename)))
        return output

    def load_facts_fixtures(self):
        fixture_file = self.fixture_file
        data = []
        path = os.path.join(os.path.dirname(__file__) + "/facts/fixtures")
        file = "{0}/{1}".format(path, fixture_file)
        with open(file, "r") as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return data

    def load_fixtures(self, commands=None):
        self.run_commands.side_effect = self.load_from_file
        self.routeros.side_effect = [self.config.get("fixtures")]

    def do_facts_test(self):
        config = self.config
        asserts = config.get("asserts")
        resource = config.get("resource")
        set_module_args(
            dict(gather_subset="config", gather_network_resources=resource)
        )
        result = self.execute_module()
        config = result["ansible_facts"]["ansible_network_resources"][resource]
        for ass in asserts:
            eval(ass, dict(), dict(result=config, self=self))
