from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .resource import ConfigResource
from ..resource.bridge import BridgeResource


class Bridge(ConfigResource):

    resource = BridgeResource
