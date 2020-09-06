from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .capsman.capsman_aaa import CapsmanAaaResource
from .capsman.capsman_configuration import CapsmanConfigurationResource
from .capsman.capsman_channel import CapsmanChannelResource
from .capsman.capsman_datapath import CapsmanDatapathResource
from .capsman.capsman_manager import CapsmanManagerResource
from .capsman.capsman_provisioning import CapsmanProvisioningResource
from .interface.vlan import VlanResource
from .interface.interface import InterfaceResource
from .interface.ethernet import EthernetResource
from .wireless.wireless import WirelessResource
from .wireless.wireless_cap import WirelessCapResource
from .wireless.wireless_access_list import WirelessAccessListResource
from .wireless.wireless_connect_list import WirelessConnectListResource
from .wireless.wireless_security_profiles import (
    WirelessSecurityProfilesResource,
)
from .bridge.bridge import BridgeResource
from .bridge.bridge_settings import BridgeSettingsResource
from .bridge.bridge_port import BridgePortResource


RESOURCE_SUBSETS = dict(
    capsman_aaa=CapsmanAaaResource,
    capsman_configuration=CapsmanConfigurationResource,
    capsman_channel=CapsmanChannelResource,
    capsman_datapath=CapsmanDatapathResource,
    capsman_manager=CapsmanManagerResource,
    capsman_provisioning=CapsmanProvisioningResource,
    vlan=VlanResource,
    interface=InterfaceResource,
    ethernet=EthernetResource,
    wireless=WirelessResource,
    wireless_cap=WirelessCapResource,
    wireless_access_list=WirelessAccessListResource,
    wireless_connect_list=WirelessConnectListResource,
    wireless_security_profiles=WirelessSecurityProfilesResource,
    bridge=BridgeResource,
    bridge_settings=BridgeSettingsResource,
    bridge_port=BridgePortResource,
)
