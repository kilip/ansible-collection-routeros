from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .base import FactsBase
from ..resource.bridge_port import BridgePortResource


class BridgePortFacts(FactsBase):

    resource = BridgePortResource()
