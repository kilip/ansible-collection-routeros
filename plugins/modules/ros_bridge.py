#!/usr/bin/python


"""
The module file for ros_bridge
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_bridge
short_description: Bridge Interface Setup
description: This M(ros_bridge) will configure resource in C(/interface bridge)
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
               *  M(ros_bridge) will update existing C(/interface bridge) configuration
            -  When Resource Not Exists:
               *  M(ros_bridge) will create new C(/interface bridge),
            Replaced
            -  When Resource Exists:
               *  M(ros_bridge) will restore related C(/interface bridge) to its default value.
               *  M(ros_bridge) will update C(/interface bridge) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_bridge) will create new C(/interface bridge)
            Overridden:
            *  M(ros_bridge) will remove any existing item in C(/interface bridge)
            *  M(ros_bridge) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_bridge) will remove that item from C(/interface bridge) configuration
    config:
        description: A dictionary for L(ros_bridge)
        type: list
        elements: dict
        suboptions:
            add_dhcp_option82:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Whether to add DHCP Option-82 information (Agent Remote ID and Agent Circuit ID) to DHCP packets. Can be used together with Option-82 capable DHCP server to assign IP addresses and implement policies. This property only has effect when dhcp-snooping is set to C(yes).
            admin_mac:
                type: str
                description: |
                    Static MAC address of the bridge. This property only has effect when auto-mac is set to C(no).
            ageing_time:
                type: str
                default: 00:05:00
                description: |
                    How long a hosts information will be kept in the bridge database.
            arp:
                type: str
                default: enabled
                choices:
                    - disabled
                    - enabled
                    - proxy-arp
                    - reply-only
                description: |
                    Address Resolution Protocol setting
                    - C(disabled) - the interface will not use ARP
                    - C(enabled) - the interface will use ARP
                    - C(proxy-arp) - the interface will use the ARP proxy feature
                    - C(reply-only) - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the L(IP/ARP,https://wiki.mikrotik.com/wiki/Manual:IP/ARP) table. Therefore for communications to be successful, a valid static entry must already exist.
            arp_timeout:
                type: str
                default: auto
                choices:
                    - auto
                    - integer
                description: |
                    ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value C(auto) equals to the value of arp-timeout in L(IP/Settings,https://wiki.mikrotik.com/wiki/Manual:IP/Settings), default is 30s.
            auto_mac:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Automatically select one MAC address of bridge ports as a bridge MAC address.
            comment:
                type: str
                description: |
                    Short description of the interface.
            dhcp_snooping:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Enables or disables DHCP Snooping on the bridge.
            disabled:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Changes whether the bridge is disabled.
            ether_type:
                type: str
                default: 0x8100
                choices:
                    - 0x9100
                    - 0x8100
                    - 0x88a8
                description: |
                    Changes the EtherType, which will be used to determine if a packet has a VLAN tag. Packets that have a matching EtherType are considered as tagged packets. This property only has effect when vlan-filtering is set to C(yes).
            fast_forward:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Special and faster case of [FastPath](https://wiki.mikrotik.com/wiki/Manual:Fast_Path "Manual:Fast
                    Path") which works only on bridges with 2 interfaces (enabled by default only for new bridges). More details can be found in the L(Fast Forward,https://wiki.mikrotik.com/wiki/Manual:Interface/Bridge#Fast_Forward) section.
            forward_delay:
                type: str
                default: 00:00:15
                description: |
                    Time which is spent during the initialization phase of the bridge interface (i.e., after router startup or enabling the interface) in listening/learning state before the bridge will start functioning normally.
            frame_types:
                type: str
                default: admit-all
                choices:
                    - admit-all
                    - admit-only-untagged-and-priority-tagged
                    - admit-only-vlan-tagged
                description: |
                    Specifies allowed ingress frame types on a bridge port. This property only has effect when vlan-filtering is set to C(yes).
            igmp_snooping:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Enables multicast group and port learning to prevent multicast traffic from flooding all interfaces in a bridge.
            igmp_version:
                type: str
                default: 2
                choices:
                    - 2
                    - 3
                description: |
                    Selects the IGMP version in which IGMP general membership queries will be generated. This property only has effect when igmp-snooping is set to C(yes).
            ingress_filtering:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. Should be used with frame-types to specify if the ingress traffic should be tagged or untagged. This property only has effect when vlan-filtering is set to C(yes).
            last_member_interval:
                type: str
                default: 1s
                description: |
                    If a port has fast-leave set to C(no) and a bridge port receives a IGMP Leave message, then a IGMP Snooping enabled bridge will send a IGMP query to make sure that no devices has subscribed to a certain multicast stream on a bridge port. If a IGMP Snooping enabled bridge does not receive a IGMP membership report after amount of last-member-interval, then the bridge considers that no one has subscribed to a certain multicast stream and can stop forwarding it. This property only has effect when igmp-snooping is set to C(yes).
            last_member_query_count:
                type: str
                default: 2
                description: |
                    How many times should last-member-interval pass until a IGMP Snooping bridge will stop forwarding a certain multicast stream. This property only has effect when igmp-snooping is set to C(yes).
            max_hops:
                type: str
                default: 20
                description: |
                    Bridge count which BPDU can pass in a MSTP enabled network in the same region before BPDU is being ignored. This property only has effect when protocol-mode is set to C(mstp).
            max_message_age:
                type: str
                default: 00:00:20
                description: |
                    How long to remember Hello messages received from other STP/RSTP enabled bridges. This property only has effect when protocol-mode is set to C(stp) or C(rstp).
            membership_interval:
                type: str
                default: 4m20s
                description: |
                    Amount of time after an entry in the Multicast Database (MDB) is removed if a IGMP membership report is not received on a certain port. This property only has effect when igmp-snooping is set to C(yes).
            mld_version:
                type: str
                default: 1
                choices:
                    - 1
                    - 2
                description: |
                    Selects the MLD version. Version 2 adds support for source-specific multicast. This property only has effect when RouterOS IPv6 package is enabled and igmp-snooping is set to C(yes).
            mtu:
                type: str
                default: 1500
                description: |
                    Maximum Transmission Unit
            multicast_querier:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Multicast querier generates IGMP general membership queries to which all IGMP capable devices respond with a IGMP membership report, usually a PIM (multicast) router generates these queries. By using this property you can make a IGMP Snooping enabled bridge to generate IGMP general membership queries. This property should be used whenever there is no PIM (multicast) router in a Layer2 network or IGMP packets must be sent through multiple IGMP Snooping enabled bridges to reach a PIM (multicast) router. Without a multicast querier in a Layer2 network the Multicast Database (MDB) is not being updated and IGMP Snooping will not function properly. This property only has effect when igmp-snooping is set to C(yes).
            multicast_router:
                type: str
                default: temporary-query
                choices:
                    - disabled
                    - permanent
                    - temporary-query
                description: |
                    Changes the state of a bridge itself if IGMP membership reports are going to be forwarded to it. This property can be used to forward IGMP membership reports to the bridge for statistics or to analyse them.
                    - C(disabled) - IGMP membership reports are not forwarded to the bridge itself regardless what is connected to it.
                    - C(permanent) - IGMP membership reports are forwarded through this the bridge itself regardless what is connected to it.
                    - C(temporary-query) - automatically detect multicast routers and IGMP Snooping enabled bridges. This property only has effect when igmp-snooping is set to C(yes).
            name:
                type: str
                required: True
                description: |
                    Name of the bridge interface
            priority:
                type: int
                description: |
                    Bridge priority, used by STP to determine root bridge, used by MSTP to determine CIST and IST regional root bridge. This property has no effect when protocol-mode is set to C(none).
            protocol_mode:
                type: str
                default: rstp
                choices:
                    - none
                    - rstp
                    - stp
                    - mstp
                description: |
                    Select Spanning tree protocol (STP) or Rapid spanning tree protocol (RSTP) to ensure a loop-free topology for any bridged LAN. RSTP provides for faster spanning tree convergence after a topology change. Select MSTP to ensure loop-free topology across multiple VLANs. Since RouterOS v6.43 it is possible to forward Reserved MAC addresses that are in 01:80:C2:XX:XX:XX range, this can be done by setting the protocol-mode to C(none).
            pvid:
                type: str
                default: 1
                description: |
                    Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. It applies e.g. to frames sent from bridge IP and destined to a bridge port. This property only has effect when vlan-filtering is set to C(yes).
            querier_interval:
                type: str
                default: 4m15s
                description: |
                    Used to change the interval how often a bridge checks if it is the active multicast querier. This property only has effect when igmp-snooping and multicast-querier is set to C(yes).
            query_interval:
                type: str
                default: 2m5s
                description: |
                    Used to change the interval how often IGMP general membership queries are sent out. This property only has effect when igmp-snooping and multicast-querier is set to C(yes).
            query_response_interval:
                type: str
                default: 10s
                description: |
                    Interval in which a IGMP capable device must reply to a IGMP query with a IGMP membership report. This property only has effect when igmp-snooping and multicast-querier is set to C(yes).
            region_name:
                type: str
                description: |
                    MSTP region name. This property only has effect when protocol-mode is set to C(mstp).
            region_revision:
                type: str
                description: |
                    MSTP configuration revision number. This property only has effect when protocol-mode is set to C(mstp).
            startup_query_count:
                type: str
                default: 2
                description: |
                    Specifies how many times must startup-query-interval pass until the bridge starts sending out IGMP general membership queries periodically. This property only has effect when igmp-snooping and multicast-querier is set to C(yes).
            startup_query_interval:
                type: str
                default: 31s250ms
                description: |
                    Used to change the amount of time after a bridge starts sending out IGMP general membership queries after the bridge is enabled. This property only has effect when igmp-snooping and multicast-querier is set to C(yes).
            transmit_hold_count:
                type: str
                default: 6
                description: |
                    The Transmit Hold Count used by the Port Transmit state machine to limit transmission rate.
            vlan_filtering:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Globally enables or disables VLAN functionality for bridge.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.bridge.bridge import BridgeResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=BridgeResource.argument_spec)
    result = ResourceConfig(module, BridgeResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
