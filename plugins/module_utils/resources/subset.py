from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .interface.vlan import VlanResource
from .interface.interface import InterfaceResource
from .bridge.bridge import BridgeResource
from .bridge.bridge_settings import BridgeSettingsResource
from .bridge.bridge_port import BridgePortResource


RESOURCE_SUBSETS = dict(
    vlan=VlanResource,
    interface=InterfaceResource,
    bridge=BridgeResource,
    bridge_settings=BridgeSettingsResource,
    bridge_port=BridgePortResource,
)
