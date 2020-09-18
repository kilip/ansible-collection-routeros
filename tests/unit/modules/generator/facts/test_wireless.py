from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
Unit Tests For ros_wireless module
"""

from ..facts_base import TestFactsBase


class TestWirelessFacts(TestFactsBase):
    def setUp(self):
        self.fixture_file = "interface.wireless.wireless.yaml"
        TestFactsBase.setUp(self)

    def test_ros_facts(self):
        self.do_facts_test()
