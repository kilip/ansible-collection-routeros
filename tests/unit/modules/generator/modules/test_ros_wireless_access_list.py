from __future__ import absolute_import, division, print_function

__metaclass__ = type

from parameterized import parameterized
from ..module_base import TestResourceModules, load_module_fixtures
from ......plugins.modules import ros_wireless_access_list

module_fixtures = load_module_fixtures(
    "interface.wireless.wireless_access_list.yaml"
)


class TestRosWirelessAccessListModule(TestResourceModules):
    module = ros_wireless_access_list

    def setUp(self):
        TestResourceModules.setUp(self)

    @parameterized.expand(module_fixtures)
    def test_module(self, state, fixtures, spec, commands):
        self.do_test_module(state, fixtures, spec, commands)
