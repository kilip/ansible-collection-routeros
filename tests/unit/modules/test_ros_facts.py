# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import yaml
import os
from glob import glob
from parameterized import parameterized
from ..compat.mock import patch
from .utils import set_module_args
from .routeros_module import TestRouterOSModule, load_fixture
from ansible_collections.kilip.routeros.plugins.modules import ros_facts


def load_facts_fixtures():
    data = []
    path = os.path.join(os.path.dirname(__file__) + "/fixtures", "facts")
    files = glob(path + "/*.*")
    for file in files:
        with open(file, "r") as stream:
            try:
                parsed = yaml.safe_load(stream)
                data.append((parsed["resource"], parsed))
            except yaml.YAMLError as exc:
                print(exc)
    return data


resource_fixtures = load_facts_fixtures()
fixtures = dict()


class TestROSFactsModule(TestRouterOSModule):

    module = ros_facts

    def setUp(self):
        TestRouterOSModule.setUp(self)
        self.mock_run_commands = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.facts.legacy.run_commands"
        )
        self.run_commands = self.mock_run_commands.start()

        self.mock_routeros = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.run_commands"
        )
        self.routeros = self.mock_routeros.start()

    def load_from_file(*args, **kwargs):
        commands = kwargs["commands"]
        output = list()
        for command in commands:
            filename = str(command).replace(" ", "_").replace("/", "")
            output.append(load_fixture(f"facts/legacy/{filename}"))
        return output

    def load_config(*args, **kwargs):
        cmds = kwargs["commands"]
        output = []
        for cmd in cmds:
            cmd = str(cmd).replace(" ", "_").replace("/", "")
            cmd = fixtures[cmd]
            output.append(cmd)
        return output

    def load_fixtures(self, commands=None):
        self.run_commands.side_effect = self.load_from_file
        self.routeros.side_effect = self.load_config

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

    @parameterized.expand(resource_fixtures)
    def test_resource_facts(self, resource, config):
        fixtures.update(config["fixtures"])
        asserts = config["asserts"]

        set_module_args(
            dict(gather_subset="config", gather_network_resources=resource)
        )
        result = self.execute_module()
        config = result["ansible_facts"]["ansible_network_resources"][resource]
        for ass in asserts:
            eval(ass, dict(), dict(result=config, self=self))
