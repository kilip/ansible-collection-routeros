#!/usr/bin/python


"""
The module file for ros_firewall_raw
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_firewall_raw
short_description: Manage configuration for C(/ip firewall raw)
description: This M(ros_firewall_raw) module provides management for RouterOS C(/ip firewall raw).
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
            Overridden:
            *  M(ros_firewall_raw) will remove any existing item in C(/ip firewall raw)
            *  M(ros_firewall_raw) will create new item using value in the C(argument_spec)
    config:
        description: A dictionary for L(ros_firewall_raw)
        type: list
        elements: dict
        suboptions:
            action:
                choices:
                    - accept
                    - add-dst-to-address-list
                    - add-src-to-address-list
                    - drop
                    - jump
                    - log
                    - no-track
                    - passthrough
                    - return
                type: str
                default: accept
                description: |
                    Action to take if packet is matched by the rule:
                    - accept - accept the packet. Packet is not passed to next firewall rule.
                    - add-dst-to-address-list - add destination address to L( address
                    list,/wiki/Manual:IP/Firewall/Address_list) specified by C(address-list)
                    parameter
                    - add-src-to-address-list - add source address to L( address
                    list,/wiki/Manual:IP/Firewall/Address_list) specified by C(address-list)
                    parameter
                    - drop - silently drop the packet
                    - jump - jump to the user defined chain specified by the value of C(jump-target)
                    parameter
                    - log - add a message to the system log containing following data: in-interface,
                    out-interface, src-mac, protocol, src-ip:port-&gt;dst-ip:port and length of the
                    packet. After packet is matched it is passed to next rule in the list, similar
                    as C(passthrough)
                    - notrack - do not send packet to connection tracking.
                    - passthrough - ignore this rule and go to next one (useful for statistics).
                    - return - passes control back to the chain from where the jump took place
            address_list:
                type: str
                description: |
                    Name of the address list to be used. Applicable if action is
                    C(add-dst-to-address-list) or C(add-src-to-address-list)
            address_list_timeout:
                type: str
                default: none-dynamic
                choices:
                    - none-dynamic
                    - none-static
                    - time
                description: |
                    Time interval after which the address will be removed from the address list
                    specified by C(address-list) parameter. Used in conjunction with
                    C(add-dst-to-address-list) or C(add-src-to-address-list) actions
                    - Value of none-dynamic (C(00:00:00)) will leave the address in the address list
                    till reboot
                    - Value of none-static will leave the address in the address list forever and
                    will be included in configuration export/backup
            chain:
                type: str
                description: |
                    Specifies to which chain rule will be added. If the input does not match the
                    name of an already defined chain, a new chain will be created.
            comment:
                type: str
                description: |
                    Descriptive comment for the rule.
            dscp:
                type: int
                description: |
                    Matches DSCP IP header field.
            dst_address:
                type: str
                description: |
                    Matches packets which destination is equal to specified IP or falls into
                    specified IP range.
            dst_address_list:
                type: str
                description: |
                    Matches destination address of a packet against user-defined L( address
                    list,/wiki/Manual:IP/Firewall/Address_list)
            dst_address_type:
                type: str
                choices:
                    - unicast
                    - local
                    - broadcast
                    - multicast
                default: None
                description: |
                    Matches destination address type:
                    - unicast - IP address used for point to point transmission
                    - local - if dst-address is assigned to one of routers interfaces
                    - broadcast - packet is sent to all devices in subnet
                    - multicast - packet is forwarded to defined group of devices
            dst_limit:
                type: int
                description: |
                    Matches packets until a given rate is exceeded. Rate is defined as packets per
                    time interval. As opposed to the limit matcher, every flow has its own limit.
                    Flow is defined by mode parameter. Parameters are written in following format:
                    C(count[/time],burst,mode[/expire]).
                    - count - packet count per time interval per flow to match
                    - time - specifies the time interval in which the packet count per flow cannot
                    be exceeded (optional, 1s will be used if not specified)
                    - burst - initial number of packets per flow to match: this number gets
                    recharged by one every C(time)/C(count), up to this number
                    - mode - this parameter specifies what unique fields define flow (src-address,
                    dst-address, src-and-dst-address, dst-address-and-port, addresses-and-dst-port)
                    - expire - specifies interval after which flow with no packets will be allowed
                    to be deleted (optional)
            dst_port:
                type: int
                description: |
                    List of destination port numbers or port number ranges
            fragment:
                type: str
                choices:
                    - yes
                    - no
                default: None
                description: |
                    Matches fragmented packets. First (starting) fragment does not count. If
                    connection tracking is enabled there will be no fragments as system
                    automatically assembles every packet
            hotspot:
                type: str
                choices:
                    - auth
                    - from-client
                    - http
                    - local-dst
                    - to-client
                default: None
            icmp_options:
                type: int
                description: |
                    Matches ICMP type:code fileds
            in_bridge_port:
                type: str
                description: |
                    Actual interface the packet has entered the router, if incoming interface is
                    bridge. Works only if use-ip-firewall is enabled in bridge settings.
            in_interface:
                type: str
                description: |
                    Interface the packet has entered the router
            in_interface_list:
                type: str
                description: |
                    Set of interfaces defined in L( interface list,/wiki/Manual:Interface/List).
                    Works the same as in-interface
            ingress_priority:
                type: int
                description: |
                    Matches ingress priority of the packet. Priority may be derived from VLAN, WMM
                    or MPLS EXP bit. L( Read more&gt;&gt;,/wiki/Manual:WMM)
            ipsec_policy:
                type: str
                choices:
                    - in
                    - ipsec
                    - none
                default: None
                description: |
                    Matches the policy used by IPsec. Value is written in following format:
                    C(<b>direction, policy</b>). Direction is Used to select whether to match the
                    policy used for decapsulation or the policy that will be used for encapsulation.
                    - in - valid in the PREROUTING chain
                    - out - valid in the OUTPUT chain
                    - ipsec - matches if the packet is subject to IPsec processing;
                    - none - matches packet that is not subject to IPsec processing (for example,
                    IpSec transport packet).
                    For example, if router receives IPsec encapsulated Gre packet, then rule
                    C(ipsec-policy=in,ipsec) will match Gre packet, but rule C(ipsec-policy=in,none)
                    will match ESP packet.
            ipv4_options:
                type: str
                choices:
                    - any
                    - loose-source-routing
                    - no-record-route
                    - no-router-alert
                    - no-source-routing
                    - no-timestamp
                    - none
                    - record-route
                    - router-alert
                    - strict-source-routing
                    - timestamp
                default: None
                description: |
                    Matches IPv4 header options.
                    - any - match packet with at least one of the ipv4 options
                    - loose-source-routing - match packets with loose source routing option. This
                    option is used to route the internet datagram based on information supplied by
                    the source
                    - no-record-route - match packets with no record route option. This option is
                    used to route the internet datagram based on information supplied by the source
                    - no-router-alert - match packets with no router alter option
                    - no-source-routing - match packets with no source routing option
                    - no-timestamp - match packets with no timestamp option
                    - record-route - match packets with record route option
                    - router-alert - match packets with router alter option
                    - strict-source-routing - match packets with strict source routing option
                    - timestamp - match packets with timestamp
            jump_target:
                type: str
                description: |
                    Name of the target chain to jump to. Applicable only if C(action=jump)
            limit:
                type: int
                description: |
                    Matches packets up to a limited rate (packet rate or bit rate). Rule using this
                    matcher will match until this limit is reached. Parameters are written in
                    following format: C(count[/time],burst:mode).
                    - count - packet or bit count per time interval to match
                    - time - specifies the time interval in which the packet or bit count cannot be
                    exceeded (optional, 1s will be used if not specified)
                    - burst - initial number of packets or bits to match: this number gets recharged
                    every 10ms so burst should be at least 1/100 of rate per second
                    - mode - packet or bit mode
            log:
                type: str
                choices:
                    - yes
                    - no
                default: None
                description: |
                    Preferred method of logging instead of C(action=log)
            log_prefix:
                type: str
                description: |
                    Adds specified text at the beginning of every log message. Applicable if
                    C(action=log)
            nth:
                type: int
                description: |
                    Matches every nth packet. L( Read more
                    &gt;&gt;,/wiki/Manual:NTH_in_RouterOS_3.x)
            out_bridge_port:
                type: str
                description: |
                    Actual interface the packet is leaving the router, if outgoing interface is
                    bridge. Works only if use-ip-firewall is enabled in bridge settings.
            out_interface:
                type: str
                description: |
                    Interface the packet is leaving the router
            out_interface_list:
                type: str
                description: |
                    Set of interfaces defined in L( interface list,/wiki/Manual:Interface/List).
                    Works the same as out-interface
            packet_size:
                type: int
                description: |
                    Matches packets of specified size or size range in bytes.
            per_connection_classifier:
                type: str
                description: |
                    PCC matcher allows to divide traffic into equal streams with ability to keep
                    packets with specific set of options in one particular stream. L( Read more
                    &gt;&gt;,/wiki/Manual:PCC)
            port:
                type: int
                description: |
                    Matches if any (source or destination) port matches the specified list of ports
                    or port ranges. Applicable only if C(protocol) is TCP or UDP
            priority:
                type: int
            protocol:
                type: str
                default: tcp
                description: |
                    Matches particular IP protocol specified by protocol name or number
            psd:
                type: int
                description: |
                    Attempts to detect TCP and UDP scans. Parameters are in following format
                    C(WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight)
                    - WeightThreshold - total weight of the latest TCP/UDP packets with different
                    destination ports coming from the same host to be treated as port scan sequence
                    - DelayThreshold - delay for the packets with different destination ports coming
                    from the same host to be treated as possible port scan subsequence
                    - LowPortWeight - weight of the packets with privileged (&lt;1024) destination
                    port
                    - HighPortWeight - weight of the packet with non-priviliged destination port
            random:
                type: int
                description: |
                    Matches packets randomly with given probability.
            src_address:
                type: str
                description: |
                    Matches packets which source is equal to specified IP or falls into specified IP
                    range.
            src_address_list:
                type: str
                description: |
                    Matches source address of a packet against user-defined L( address
                    list,/wiki/Manual:IP/Firewall/Address_list)
            src_address_type:
                type: str
                choices:
                    - unicast
                    - local
                    - broadcast
                    - multicast
                default: None
                description: |
                    Matches source address type:
                    - unicast - IP address used for point to point transmission
                    - local - if address is assigned to one of routers interfaces
                    - broadcast - packet is sent to all devices in subnet
                    - multicast - packet is forwarded to defined group of devices
            src_port:
                type: int
                description: |
                    List of source ports and ranges of source ports. Applicable only if protocol is
                    TCP or UDP.
            src_mac_address:
                type: str
                description: |
                    Matches source MAC address of the packet
            tcp_flags:
                type: str
                choices:
                    - ack
                    - cwr
                    - ece
                    - fin
                    - psh
                    - rst
                    - syn
                    - urg
                default: None
                description: |
                    Matches specified TCP flags
                    - ack - acknowledging data
                    - cwr - congestion window reduced
                    - ece - ECN-echo flag (explicit congestion notification)
                    - fin - close connection
                    - psh - push function
                    - rst - drop connection
                    - syn - new connection
                    - urg - urgent data
            tcp_mss:
                type: int
                description: |
                    Matches TCP MSS value of an IP packet
            tls_host:
                type: str
                description: |
                    Allows to match traffic based on TLS hostname. Accepts L(GLOB
                    syntax,https://en.wikipedia.org/wiki/Glob_(programming)) for wildcard matching.
                    Note that matcher will not be able to match hostname if TLS handshake frame is
                    fragmented into multiple TCP segments (packets).
            ttl:
                type: int
                description: |
                    Matches packets TTL value

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.firewall.raw import FirewallRawResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=FirewallRawResource.argument_spec)
    result = ResourceConfig(module, FirewallRawResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
