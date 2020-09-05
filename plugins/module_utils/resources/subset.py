from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .interface.interface import InterfaceResource
from .bridge.bridge import BridgeResource
from .bridge.bridge_settings import BridgeSettingsResource


RESOURCE_SUBSETS = dict(
    interface=InterfaceResource,
    bridge=BridgeResource,
    bridge_settings=BridgeSettingsResource,
)
