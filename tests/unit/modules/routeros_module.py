from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
import json

from ansible_collections.kilip.routeros.tests.unit.modules.utils import (
    AnsibleExitJson,
    AnsibleFailJson,
    ModuleTestCase,
)


fixture_path = os.path.join(os.path.dirname(__file__), "fixtures")
fixture_data = {}


def load_fixture(name):
    path = os.path.join(fixture_path, name)

    if path in fixture_data:
        return fixture_data[path]

    with open(path) as f:
        data = f.read()

    try:
        data = json.loads(data)
    except Exception:
        pass

    fixture_data[path] = data
    return data


class TestRouterOSModule(ModuleTestCase):
    def execute_module(
        self,
        failed=False,
        changed=False,
        commands=None,
        sort=True,
        defaults=False,
    ):
        self.load_fixtures(commands)

        if failed:
            result = self.failed()
            self.assertTrue(result["failed"], result)
        else:
            result = self.changed(changed)
            self.assertEqual(result["changed"], changed, result)

        if commands is not None:
            if sort:
                self.assertEqual(
                    sorted(commands),
                    sorted(result["commands"]),
                    result["commands"],
                )
            else:
                self.assertEqual(
                    commands, result["commands"], result["commands"]
                )

        return result

    def load_from_file(*args, **kwargs):
        commands = kwargs["commands"]
        output = list()
        for command in commands:
            filename = str(command).replace(" ", "_").replace("/", "")
            output.append(load_fixture("%s" % filename))
        return output

    def failed(self):
        with self.assertRaises(AnsibleFailJson) as exc:
            self.module.main()

        result = exc.exception.args[0]
        self.assertTrue(result["failed"], result)
        return result

    def changed(self, changed=False):
        with self.assertRaises(AnsibleExitJson) as exc:
            self.module.main()

        result = exc.exception.args[0]
        self.assertEqual(result["changed"], changed, result)
        return result

    def load_fixtures(self, commands=None):
        pass
