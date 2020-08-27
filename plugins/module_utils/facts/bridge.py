from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .base import FactsBase
from ..resource.bridge import BridgeResource


class BridgeFacts(FactsBase):

    resource = BridgeResource()
