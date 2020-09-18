from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
Unit Tests For ros_wireless_cap module
"""

from ..facts_base import TestFactsBase


class TestWirelessCapFacts(TestFactsBase):
    def setUp(self):
        self.fixture_file = "interface.wireless.wireless_cap.yaml"
        TestFactsBase.setUp(self)

    def test_ros_facts(self):
        self.do_facts_test()
