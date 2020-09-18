from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
Unit Tests For ros_bridge_settings module
"""

from ..facts_base import TestFactsBase


class TestBridgeSettingsFacts(TestFactsBase):
    def setUp(self):
        self.fixture_file = "interface.bridge.bridge_settings.yaml"
        TestFactsBase.setUp(self)

    def test_ros_facts(self):
        self.do_facts_test()
