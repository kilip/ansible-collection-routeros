from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
Unit Tests For ros_ethernet module
"""

from ..facts_base import TestFactsBase


class TestEthernetFacts(TestFactsBase):
    def setUp(self):
        self.fixture_file = "interface.ethernet.yaml"
        TestFactsBase.setUp(self)

    def test_ros_facts(self):
        self.do_facts_test()
