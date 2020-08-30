#!/usr/bin/python


"""
The module file for ros_bridge_port
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_bridge_port
short_description: Bridge Settings
description: Globally controlled settings and statistics for all bridge interfaces.
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
        description:
            - I(merged) M(ros_bridge_port) will update existing C(/interface bridge port) configuration, or create new C(/interface bridge port) when resource not found
            - I(replaced) M(ros_bridge_port) will restore existing C(/interface bridge port) configuration to its default value, then update existing resource with the new configuration. If the resource C(/interface bridge port) not found, M(ros_bridge_port) will create resource in C(/interface bridge port)
            - I(overridden) M(ros_bridge_port) will remove any resource in C(/interface bridge port) first, and then create new C(/interface bridge port) resources.
            - I(deleted) M({module}) when found module will delete C(/interface bridge port)
    config:
        description: A dictionary for L(ros_bridge_port)
        type: list
        elements: dict
        suboptions:
            auto_isolate:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Prevents STP blocking port from erroneously moving into a forwarding state if no BPDUs are received on the bridge. This property has no effect when protocol-mode is set to C(none).
            bpdu_guard:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Enables or disables BPDU Guard feature on a port. This feature disables a port if it receives a BPDU and requires the port to be manually re-enabled if a BPDU was received. Should be used to prevent a bridge from BPDU related attacks. This property has no effect when protocol-mode is set to C(none).
            bridge:
                type: str
                required: True
                description: |
                    The bridge interface the respective interface is grouped in.
            broadcast_flood:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    When enabled, bridge floods broadcast traffic to all bridge egress ports. When disabled, drops broadcast traffic on egress ports. Can be used to filter all broadcast traffic on an egress port. Broadcast traffic is considered as traffic that uses FF:FF:FF:FF:FF:FF as destination MAC address, such traffic is crucial for many protocols such as DHCP, ARP, NDP, BOOTP (Netinstall) and others. This option does not limit traffic flood to the CPU.
            edge:
                type: str
                default: auto
                choices:
                    - auto
                    - no
                    - no-discover
                    - yes
                    - yes-discover
                description: |
                    Set port as edge port or non-edge port, or enable edge discovery. Edge ports are connected to a LAN that has no other bridges attached. An edge port will skip the learning and the listening states in STP and will transition directly to the forwarding state, this reduces the STP initialization time. If the port is configured to discover edge port then as soon as the bridge detects a BPDU coming to an edge port, the port becomes a non-edge port. This property has no effect when protocol-mode is set to C(none).
                    - C(no) - non-edge port, will participate in learning and listening states in STP.
                    - C(no-discover) - non-edge port with enabled discovery, will participate in learning and listening states in STP, a port can become edge port if no BPDU is received.
                    - C(yes) - edge port without discovery, will transit directly to forwarding state.
                    - C(yes-discover) - edge port with enabled discovery, will transit directly to forwarding state.
                    - C(auto) - same as C(no-discover), but will additionally detect if bridge port is a Wireless interface with disabled bridge-mode, such interface will be automatically set as an edge port without discovery.
            external_fdb:
                type: str
                default: auto
                choices:
                    - auto
                    - no
                    - yes
                description: |
                    Whether to use wireless registration table to speed up bridge host learning. If there are no Wireless interfaces in a bridge, then setting external-fdb to C(yes) will disable MAC learning and the bridge will act as a hub (disables hardware offloading). Replaced with learn parameter in RouterOS v6.42
            fast_leave:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Enables IGMP Fast leave feature on the port. Bridge will stop forwarding traffic to a bridge port whenever a IGMP Leave message is received for appropriate multicast stream. This property only has effect when igmp-snooping is set to C(yes).
            frame_types:
                type: str
                default: admit-all
                choices:
                    - admit-all
                    - admit-only-untagged-and-priority-tagged
                    - admit-only-vlan-tagged
                description: |
                    Specifies allowed ingress frame types on a bridge port. This property only has effect when vlan-filtering is set to C(yes).
            ingress_filtering:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. Should be used with frame-types to specify if the ingress traffic should be tagged or untagged. This property only has effect when vlan-filtering is set to C(yes).
            learn:
                type: str
                default: auto
                choices:
                    - auto
                    - no
                    - yes
                description: |
                    Changes MAC learning behaviour on a bridge port
                    - C(yes) - enables MAC learning
                    - C(no) - disables MAC learning
                    - C(auto) - detects if bridge port is a Wireless interface and uses Wireless registration table instead of MAC learning, will use Wireless registration table if the L(Wireless interface,https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless) is disabled.
            multicast_router:
                type: str
                default: temporary-query
                choices:
                    - disabled
                    - permanent
                    - temporary-query
                description: |
                    Changes the state of a bridge port whether IGMP membership reports are going to be forwarded to this port. By default IGMP membership reports (most importantly IGMP Join messages) are only forwarded to ports that have a multicast router or a IGMP Snooping enabled bridge connected to. Without at least one port marked as a C(multicast-router) IPTV might not work properly, it can be either be detected automatically or forced manually.
                    - C(disabled) - IGMP membership reports are not forwarded through this port regardless what is connected to it.
                    - C(permanent) - IGMP membership reports are forwarded through this port regardless what is connected to it.
                    - C(temporary-query) - automatically detect multicast routers and IGMP Snooping enabled bridges.
                    You can improve security by forcing ports that have IPTV boxes connected to never become ports marked as C(multicast-router). This property only has effect when igmp-snooping is set to C(yes).
            horizon:
                type: int
                description: |
                    Use split horizon bridging to prevent bridging loops. Set the same value for group of ports, to prevent them from sending data to ports with the same horizon value. Split horizon is a software feature that disables hardware offloading. Read more about L(Bridge split horizon,https://wiki.mikrotik.com/wiki/MPLSVPLS#Split_horizon_bridging).
            internal_path_cost:
                type: str
                default: 10
                description: |
                    Path cost to the interface for MSTI0 inside a region. This property only has effect when protocol-mode is set to C(mstp).
            interface:
                type: str
                required: True
                description: |
                    Name of the interface.
            path_cost:
                type: str
                default: 10
                description: |
                    Path cost to the interface, used by STP to determine the "best" path, used by MSTP to determine "best" path between regions. This property has no effect when protocol-mode is set to C(none).
            point_to_point:
                type: str
                default: auto
                choices:
                    - auto
                    - yes
                    - no
                description: |
                    Specifies if a bridge port is connected to a bridge using a point-to-point link for faster convergence in case of failure. By setting this property to C(yes), you are forcing the link to be a point-to-point link, which will skip the checking mechanism, which detects and waits BPDUs from other devices from this single link, by setting this property to C(no), you are expecting that a link can receive BPDUs from multiple devices. By setting the property to C(yes), you are significantly improving (R/M)STP convergence time. In general, you should only set this property to C(no) if it is possible that another device can be connected between a link, this is mostly relevant to Wireless mediums and Ethernet hubs. If the Ethernet link is full-duplex, C(auto) enables point-to-point functionality. And this property has no effect when protocol-mode is set to C(none).
            priority:
                type: str
                default: 128
                description: |
                    The priority of the interface, used by STP to determine the root port, used by MSTP to determine root port between regions.
            pvid:
                type: str
                default: 1
                description: |
                    Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. This property only has effect when vlan-filtering is set to C(yes).
            restricted_role:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Enable the restricted role on a port, used by STP to forbid a port becoming a root port. This property only has effect when protocol-mode is set to C(mstp).
            restricted_tcn:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Disable topology change notification (TCN) sending on a port, used by STP to forbid network topology changes to propagate. This property only has effect when protocol-mode is set to C(mstp).
            tag_stacking:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Forces all packets to be treated as untagged packets. Packets on ingress port will be tagged with another VLAN tag regardless if a VLAN tag already exists, packets will be tagged with a VLAN ID that matches the pvid value and will use EtherType that is specified in ether-type. This property only has effect when vlan-filtering is set to C(yes).
            trusted:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    When enabled, it allows to forward DHCP packets towards DHCP server through this port. Mainly used to limit unauthorized servers to provide malicious information for users. This property only has effect when dhcp-snooping is set to C(yes).
            unknown_multicast_flood:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    When enabled, bridge floods unknown multicast traffic to all bridge egress ports. When disabled, drops unknown multicast traffic on egress ports. Multicast addresses that are in C(/interface bridge mdb) are considered as learned multicasts and therefore will not be flooded to all ports. Without IGMP Snooping all multicast traffic will be dropped on egress ports. Has effect only on an egress port. This option does not limit traffic flood to the CPU. Note that local multicast addresses (224.0.0.0/24) are not flooded when unknown-multicast-flood is disabled, as a result some protocols that rely on local multicast addresses might not work properly, such protocols are RIPv2m OSPF, mDNS, VRRP and others. Some protocols do send a IGMP join request and therefore are compatible with IGMP Snooping, some OSPF implementations are compatible with RFC1584, RouterOS OSPF implementation is not compatible with IGMP Snooping. This property should only be used when igmp-snooping is set to C(yes).
            unknown_unicast_flood:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    When enabled, bridge floods unknown unicast traffic to all bridge egress ports. When disabled, drops unknown unicast traffic on egress ports. If a MAC address is not learned in C(/interface bridge host), then the traffic is considered as unknown unicast traffic and will not be flooded to all ports. MAC address is learnt as soon as a packet on a bridge port is received, then the source MAC address is added to the bridge host table. Since it is required for the bridge to receive at least one packet on the bridge port to learn the MAC address, it is recommended to use static bridge host entries to avoid packets being dropped until the MAC address has been learnt. Has effect only on an egress port. This option does not limit traffic flood to the CPU.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.bridge.port import BridgePortResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=BridgePortResource.argument_spec)
    result = ResourceConfig(module, BridgePortResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
