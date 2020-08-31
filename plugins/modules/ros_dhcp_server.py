#!/usr/bin/python


"""
The module file for ros_dhcp_server
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_dhcp_server
short_description: Interface Configuration
description: Configuration for I(/interface)
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
    state:
        choices:
            - merged
            - replaced
            - overridden
            - deleted
        default: merged
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_dhcp_server) will update existing C(/ip dhcp-server) configuration
            -  When Resource Not Exists:
               *  M(ros_dhcp_server) will create new C(/ip dhcp-server),
            Replaced
            -  When Resource Exists:
               *  M(ros_dhcp_server) will restore related C(/ip dhcp-server) to its default value.
               *  M(ros_dhcp_server) will update C(/ip dhcp-server) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_dhcp_server) will create new C(/ip dhcp-server)
            Overridden:
            *  M(ros_dhcp_server) will remove any existing item in C(/ip dhcp-server)
            *  M(ros_dhcp_server) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_dhcp_server) will remove that item from C(/ip dhcp-server) configuration
    config:
        description: A dictionary for L(ros_dhcp_server)
        type: list
        elements: dict
        suboptions:
            add_arp:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Whether to add dynamic ARP entry. If set to C(no) either L( ARP mode,/wiki/Manual:IP/ARP#ARP_Modes) entries should be administratively defined in C(/ip arp) submenu.
            address_pool:
                type: str
                ignore: true
                description: |
                    L( IP pool,/wiki/Manual:IP/Pools), from which to take IP addresses for the clients. If set to static-only, then only the clients that have a static lease (added in L( lease,#Leases) submenu) will be allowed.
            allow_dual_stack_queue:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Creates a single simple queue entry for both IPv4 and IPv6 addresses, uses the MAC address and DUID for identification. Requires L( IPv6 DHCP Server,/wiki/Manual:IPv6/DHCP_Server) to have this option enabled as well to work properly.
            always_broadcast:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Always send replies as broadcasts even if destination IP is known. Will add additional load on L2 network.
            authoritative:
                type: str
                default: yes
                choices:
                    - after-10sec-delay
                    - after-2sec-delay
                    - yes
                    - no
                description: |
                    Option changes the way how server responds to DHCP requests:
                    - yes - replies to clients request for an address that is not available from this server, dhcp server will send negative acknowledgment (DHCPNAK)
                    - no - dhcp server ignores clients requests for addresses that are not available from this server
                    - after-10sec-delay - requests with "secs &lt; 10" will be processed as in "no" setting case and requests with "secs &gt;= 10" will be processed as in "yes" case.
                    - after-2sec-delay - requests with "secs &lt; 2" will be processed as in "no" setting case and requests with "secs &gt;= 2" will be processed as in "yes" case.
                    If all requests with "secs &lt; x" should be ignored, then delay-threshold=x setting should be used.
            bootp_lease_time:
                type: str
                ignore: true
                description: |
                    Accepts two predefined options or time value:
                    - forever - lease never expires
                    - lease-time - use time from lease-time parameter
            bootp_support:
                type: str
                default: static
                choices:
                    - none
                    - static
                    - dynamic
                description: |
                    Support for BOOTP clients:
                    - none - do not respond to BOOTP requests
                    - static - offer only static leases to BOOTP clients
                    - dynamic - offer static and dynamic leases for BOOTP clients
            client_mac_limit:
                type: str
                ignore: true
                description: |
                    Specifies whether to limit specific number of clients per single MAC address or leave unlimited. Note that this setting should not be used in relay setups.
            conflict_detection:
                type: str
                choices:
                    - yes
                    - no
                default: None
                description: |
                    Allows to disable/enable conflict detection. If option is enabled, then whenever server tries to assign a lease it will send ICMP and ARP messages to detect whether such address in the network already exist. If any of above get reply address is considered already used. Conflict detection must be disabled when any kind of DHCP client limitation per port or per mac is used.
            delay_threshold:
                type: str
                ignore: true
                description: |
                    If secs field in DHCP packet is smaller than delay-threshold, then this packet is ignored. If set to none - there is no threshold (all DHCP packets are processed)
            dhcp_option_set:
                type: str
                ignore: true
                description: |
                    Use custom set of DHCP options defined in option sets menu.
            insert_queue_before:
                type: str
                ignore: true
                description: |
                    Specify where to place dynamic simple queue entries for static DCHP leases with rate-limit parameter set.
            interface:
                type: str
                description: |
                    Interface on which server will be running.
            lease_script:
                type: str
                description: |
                    Script that will be executed after lease is assigned or de-assigned. Internal "global" variables that can be used in the script:
                    - leaseBound - set to "1" if bound, otherwise set to "0"
                    - leaseServerName - dhcp server name
                    - leaseActMAC - active mac address
                    - leaseActIP - active IP address
                    - lease-hostname - client hostname
                    - lease-options - array of received options
            lease_time:
                type: str
                default: 10m
                description: |
                    The time that a client may use the assigned address. The client will try to renew this address after a half of this time and will request a new address after time limit expires.
            name:
                type: str
                required: True
                description: |
                    Reference name
            parent_queue:
                type: str
                ignore: true
            relay:
                type: str
                default: 0.0.0.0
                description: |
                    The IP address of the relay this DHCP server should process requests from:
                    - 0.0.0.0 - the DHCP server will be used only for direct requests from clients (no DHCP relay allowed)
                    - 255.255.255.255 - the DHCP server should be used for any incoming request from a DHCP relay except for those, which are processed by another DHCP server that exists in the C(/ip dhcp-server) submenu.
            src_address:
                type: str
                default: 0.0.0.0
                description: |
                    The address which the DHCP client must send requests to in order to renew an IP address lease. If there is only one static address on the DHCP server interface and the source-address is left as 0.0.0.0, then the static address will be used. If there are multiple addresses on the interface, an address in the same subnet as the range of given addresses should be used.
            use_framed_as_classless:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Forward RADIUS Framed-Route as a DHCP Classless-Static-Route to DHCP-client. Whenever both Framed-Route and Classless-Static-Route is received Classless-Static-Route is preferred.
            use_radius:
                type: str
                default: no
                choices:
                    - yes
                    - no
                    - accounting
                description: |
                    Whether to use RADIUS server:
                    - no - do not use RADIUS;
                    - yes - use RADIUS for accounting and lease;
                    - accounting - use RADIUS for accounting only.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.ip.dhcp_server import DhcpServerResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=DhcpServerResource.argument_spec)
    result = ResourceConfig(module, DhcpServerResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
