from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
Unit Tests For ros_bridge_port module
"""

from ..facts_base import TestFactsBase


class TestBridgePortFacts(TestFactsBase):
    def setUp(self):
        self.fixture_file = "interface.bridge.bridge_port.yaml"
        TestFactsBase.setUp(self)

    def test_ros_facts(self):
        self.do_facts_test()
