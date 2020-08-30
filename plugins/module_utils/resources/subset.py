from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .capsman.aaa import CapsmanAaaResource
from .capsman.configuration import CapsmanConfigurationResource
from .capsman.channels import CapsmanChannelsResource
from .capsman.datapath import CapsmanDatapathResource
from .capsman.manager import CapsmanManagerResource
from .capsman.provisioning import CapsmanProvisioningResource
from .ip.static_dns import StaticDnsResource
from .ip.dns import DnsResource
from .ip.route import RouteResource
from .ip.dhcp_lease import DhcpLeaseResource
from .ip.address import AddressResource
from .ip.dhcp_server import DhcpServerResource
from .ip.dhcp_network import DhcpNetworkResource
from .ip.dhcp_client import DhcpClientResource
from .bridge.bridge import BridgeResource
from .bridge.settings import BridgeSettingsResource
from .bridge.port import BridgePortResource
from .interface.interface import InterfaceResource
from .interface.vlan import VlanResource
from .interface.pppoe_client import PppoeClientResource
from .interface.ethernet import EthernetResource
from .interface.pppoe_server import PppoeServerResource
from .wireless.cap import WirelessCapResource
from .user.group import GroupResource
from .user.user import UserResource
from .firewall.mangle import FirewallMangleResource
from .firewall.filter import FirewallFilterResource
from .firewall.address_list import FirewallAddressListResource
from .firewall.nat import FirewallNatResource
from .firewall.raw import FirewallRawResource


RESOURCE_SUBSETS = dict(
    capsman_aaa=CapsmanAaaResource,
    capsman_configuration=CapsmanConfigurationResource,
    capsman_channels=CapsmanChannelsResource,
    capsman_datapath=CapsmanDatapathResource,
    capsman_manager=CapsmanManagerResource,
    capsman_provisioning=CapsmanProvisioningResource,
    static_dns=StaticDnsResource,
    dns=DnsResource,
    route=RouteResource,
    dhcp_lease=DhcpLeaseResource,
    address=AddressResource,
    dhcp_server=DhcpServerResource,
    dhcp_network=DhcpNetworkResource,
    dhcp_client=DhcpClientResource,
    bridge=BridgeResource,
    bridge_settings=BridgeSettingsResource,
    bridge_port=BridgePortResource,
    interface=InterfaceResource,
    vlan=VlanResource,
    pppoe_client=PppoeClientResource,
    ethernet=EthernetResource,
    pppoe_server=PppoeServerResource,
    wireless_cap=WirelessCapResource,
    group=GroupResource,
    user=UserResource,
    firewall_mangle=FirewallMangleResource,
    firewall_filter=FirewallFilterResource,
    firewall_address_list=FirewallAddressListResource,
    firewall_nat=FirewallNatResource,
    firewall_raw=FirewallRawResource,
)
