from __future__ import absolute_import, division, print_function

__metaclass__ = type

from parameterized import parameterized
from ..module_base import TestResourceModules, load_module_fixtures
from ......plugins.modules import ros_capsman_provisioning

module_fixtures = load_module_fixtures("capsman.capsman_provisioning.yaml")


class TestRosCapsmanProvisioningModule(TestResourceModules):
    module = ros_capsman_provisioning

    def setUp(self):
        TestResourceModules.setUp(self)

    @parameterized.expand(module_fixtures)
    def test_module(self, state, fixtures, spec, commands):
        self.do_test_module(state, fixtures, spec, commands)
