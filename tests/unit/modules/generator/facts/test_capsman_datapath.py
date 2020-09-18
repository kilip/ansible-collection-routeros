from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
Unit Tests For ros_capsman_datapath module
"""

from ..facts_base import TestFactsBase


class TestCapsmanDatapathFacts(TestFactsBase):
    def setUp(self):
        self.fixture_file = "capsman.capsman_datapath.yaml"
        TestFactsBase.setUp(self)

    def test_ros_facts(self):
        self.do_facts_test()
