from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
Unit Tests For ros_wireless_access_list module
"""

from ..facts_base import TestFactsBase


class TestWirelessAccessListFacts(TestFactsBase):
    def setUp(self):
        self.fixture_file = "interface.wireless.wireless_access_list.yaml"
        TestFactsBase.setUp(self)

    def test_ros_facts(self):
        self.do_facts_test()
