from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from .base import FactsBase
from ..resource.bridge import BridgeResource

class BridgeFacts(FactsBase):

    def get_resource(self):
        return BridgeResource
