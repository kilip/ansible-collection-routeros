from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .interface.vlan import VlanResource
from .interface.interface import InterfaceResource
from .interface.ethernet import EthernetResource
from .wireless.wireless import WirelessResource
from .wireless.wireless_cap import WirelessCapResource
from .wireless.wireless_access_list import WirelessAccessListResource
from .wireless.wireless_connect_list import WirelessConnectListResource
from .bridge.bridge import BridgeResource
from .bridge.bridge_settings import BridgeSettingsResource
from .bridge.bridge_port import BridgePortResource


RESOURCE_SUBSETS = dict(
    vlan=VlanResource,
    interface=InterfaceResource,
    ethernet=EthernetResource,
    wireless=WirelessResource,
    wireless_cap=WirelessCapResource,
    wireless_access_list=WirelessAccessListResource,
    wireless_connect_list=WirelessConnectListResource,
    bridge=BridgeResource,
    bridge_settings=BridgeSettingsResource,
    bridge_port=BridgePortResource,
)
