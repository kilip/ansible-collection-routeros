from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
import yaml
from ..routeros_module import TestRouterOSModule
from ..utils import set_module_args
from ...compat.mock import patch


def load_module_fixtures(fixture_file):
    data = []
    path = os.path.join(os.path.dirname(__file__) + "/modules/fixtures")
    file = "{0}/{1}".format(path, fixture_file)
    with open(file, "r") as stream:
        try:
            parsed = yaml.safe_load(stream)
            fixtures = parsed["fixtures"]
            for test in parsed["tests"]:
                spec = test["argument_spec"]
                state = spec["state"]
                commands = test["commands"]
                data.append((state, fixtures, spec, commands))

        except yaml.YAMLError as exc:
            print(exc)
    return data


class TestResourceModules(TestRouterOSModule):
    state = ""
    fixtures = ""

    def setUp(self):
        TestRouterOSModule.setUp(self)
        self.mock_get_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.run_commands"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.kilip.routeros.plugins.module_utils.routeros.load_config"
        )
        self.load_config = self.mock_load_config.start()

    def load_module_fixtures(*args, **kwargs):
        cmds = kwargs["commands"]
        test = "\n".join(cmds)
        if "/system script export terse" in cmds:
            return "#\n#\n"
        elif "export" in test:
            return args[0].fixtures
        else:
            return []

    def load_fixtures(self, commands=None):
        self.get_config.side_effect = self.load_module_fixtures
        self.load_config.side_effect = dict(
            diff=None, session="session", results=[], requests=[]
        )

    def do_test_module(self, state, fixtures, spec, commands):
        print(commands)
        self.state = state
        self.fixtures = [fixtures]
        set_module_args(spec)
        self.execute_module(False, True, commands, False)
