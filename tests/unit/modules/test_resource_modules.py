from __future__ import absolute_import, division, print_function

__metaclass__ = type

import yaml
import os
import importlib
from glob import glob
from parameterized import parameterized
from ..compat.mock import patch
from .utils import set_module_args
from .routeros_module import TestRouterOSModule

# from ansible_collections.kilip.routeros.plugins.modules import ros_interface


def load_module_fixtures():
    data = []
    path = os.path.join(os.path.dirname(__file__) + "/fixtures", "modules")
    files = glob(path + "/*.*")
    for file in files:
        with open(file, "r") as stream:
            try:
                parsed = yaml.safe_load(stream)
                module = parsed["module"]
                fixtures.update(parsed["fixtures"])
                for test in parsed["tests"]:
                    spec = test["argument_spec"]
                    commands = test["commands"]
                    data.append((module, spec, commands))

            except yaml.YAMLError as exc:
                print(exc)
    return data


fixtures = dict()
module_fixtures = load_module_fixtures()


class TestResourceModules(TestRouterOSModule):
    def do_set_up(self):
        TestRouterOSModule.setUp(self)

        self.mock_get_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.run_commands"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.load_config"
        )
        self.load_config = self.mock_load_config.start()

    def load_module_fixture(*args, **kwargs):
        cmds = kwargs["commands"]
        output = []
        for cmd in cmds:
            cmd = str(cmd).replace(" ", "_").replace("/", "")
            if fixtures.get(cmd) is not None:
                cmd = fixtures[cmd]
            else:
                cmd = None
            if cmd:
                output.append(cmd)
        return output

    def load_fixtures(self, commands=None):
        self.get_config.side_effect = self.load_module_fixture
        self.load_config.side_effect = dict(
            diff=None, session="session", results=[], requests=[]
        )

    @parameterized.expand(module_fixtures)
    def test_module(self, module, spec, commands):
        self.module = importlib.import_module(
            "ansible_collections.kilip.routeros.plugins.modules.{0}".format(
                module
            )
        )
        self.do_set_up()
        set_module_args(spec)
        self.execute_module(False, True, commands, False)
