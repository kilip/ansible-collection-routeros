.. _ros_firewall_nat_module:


ros_firewall_nat -- Manage configuration for ``/ip firewall nat``
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_firewall_nat <ros_firewall_nat_module>` module provides management for RouterOS ``/ip firewall nat``.






Parameters
----------

  state (optional, any, merged)
    Overridden:
*  :ref:`ros_firewall_nat <ros_firewall_nat_module>` will remove any existing item in ``/ip firewall nat``
*  :ref:`ros_firewall_nat <ros_firewall_nat_module>` will create new item using value in the ``argument_spec``



  config (optional, list, None)
    A dictionary for L(ros_firewall_nat)


    action (optional, str, accept)
      Action to take if packet is matched by the rule:
- accept - accept the packet. Packet is not passed to next NAT rule.
- add-dst-to-address-list - add destination address to `Address
list </wiki/Address_list>`_ specified by ``address-list`` parameter
- add-src-to-address-list - add source address to `Address
list </wiki/Address_list>`_ specified by ``address-list`` parameter
- dst-nat - replaces destination address and/or port of an IP packet to values
specified by ``to-addresses`` and ``to-ports`` parameters
- jump - jump to the user defined chain specified by the value of ``jump-target``
parameter
- log - add a message to the system log containing following data: in-interface,
out-interface, src-mac, protocol, src-ip:port-&gt;dst-ip:port and length of the
packet. After packet is matched it is passed to next rule in the list, similar
as ``passthrough``
- masquerade - replaces source port of an IP packet to one specified by
``to-ports`` parameter and replace source address of an IP packet to IP
determined by routing facility. ``<a href="#Masquerade"> Read more >></a>``
- netmap - creates a static 1:1 mapping of one set of IP addresses to another
one. Often used to distribute public IP addresses to hosts on private networks
- passthrough - if packet is matched by the rule, increase counter and go to
next rule (useful for statistics).
- redirect - replaces destination port of an IP packet to one specified by
``to-ports`` parameter and destination address to one of the routers local
addresses
- return - passes control back to the chain from where the jump took place
- same - gives a particular client the same source/destination IP address from
supplied range for each connection. This is most frequently used for services
that expect the same client address for multiple connections from the same
client
- src-nat - replaces source address of an IP packet to values specified by
``to-addresses`` and ``to-ports`` parameters



    address_list (optional, str, None)
      Name of the address list to be used. Applicable if action is
``add-dst-to-address-list`` or ``add-src-to-address-list``



    address_list_timeout (optional, str, none-dynamic)
      Time interval after which the address will be removed from the address list
specified by ``address-list`` parameter. Used in conjunction with
``add-dst-to-address-list`` or ``add-src-to-address-list`` actions
- Value of none-dynamic (``00:00:00``) will leave the address in the address list
till reboot
- Value of none-static will leave the address in the address list forever and
will be included in configuration export/backup



    chain (True, str, None)
      Specifies to which chain rule will be added. If the input does not match the
name of an already defined chain, a new chain will be created.



    comment (optional, str, None)
      Descriptive comment for the rule.



    connection_bytes (optional, int, None)
      Matches packets only if a given amount of bytes has been transfered through the
particular connection. 0 - means infinity, for example
``connection-bytes=2000000-0`` means that the rule matches if more than 2MB has
been transfered through the relevant connection



    connection_limit (optional, int, None)
      Matches connections per address or address block after given value is reached.



    connection_mark (optional, str, None)
      Matches packets marked via mangle facility with particular connection mark. If
no-mark is set, rule will match any unmarked connection.



    connection_rate (optional, int, None)
      Connection Rate is a firewall matcher that allow to capture traffic based on
present speed of the connection. ``<a class="mw-redirect"
href="/wiki/Connection_Rate" title="Connection Rate"> Read more>></a>``



    connection_type (optional, str, None)
      Matches packets from related connections based on information from their
connection tracking helpers. A relevant connection helper must be enabled under
` /ip firewall service-port </wiki/IP/Services#Service_Ports>`_



    content (optional, str, None)
      Match packets that contain specified text



    dscp (optional, int, None)
      Matches DSCP IP header field.



    dst_address (optional, str, None)
      Matches packets which destination is equal to specified IP or falls into
specified IP range.



    dst_address_list (optional, str, None)
      Matches destination address of a packet against user-defined ` address
list </wiki/Address_list>`_



    dst_address_type (optional, str, None)
      Matches destination address type:
- unicast - IP address used for point to point transmission
- local - if dst-address is assigned to one of routers interfaces
- broadcast - packet is sent to all devices in subnet
- multicast - packet is forwarded to defined group of devices



    dst_limit (optional, int, None)
      Matches packets until a given pps limit is exceeded. As opposed to the limit
matcher, every destination IP address / destination port has its own limit.
Parameters are written in following format: ``count[/time],burst,mode[/expire]``.
- count - maximum average packet rate measured in packets per ``time`` interval
- time - specifies the time interval in which the packet rate is measured
(optional)
- burst - number of packets which are not counted by packet rate
- mode - the classifier for packet rate limiting
- expire - specifies interval after which recored ip address /port will be
deleted (optional)



    dst_port (optional, int, None)
      List of destination port numbers or port number ranges



    fragment (optional, str, None)
      Matches fragmented packets. First (starting) fragment does not count. If
connection tracking is enabled there will be no fragments as system
automatically assembles every packet



    hotspot (optional, str, None)
      Matches packets received from HotSpot clients against various HotSpot matchers.
- auth - matches authenticted HotSpot client packets
- from-client - matches packets that are coming from the HotSpot client
- http - matches HTTP requests sent to the HotSpot server
- local-dst - matches packets that are destined to the HotSpot server
- to-client - matches packets that are sent to the HotSpot client



    icmp_options (optional, int, None)
      Matches ICMP type:code fileds



    in_bridge_port (optional, str, None)
      Actual interface the packet has entered the router, if incoming interface is
bridge



    in_interface (optional, str, None)
      Interface the packet has entered the router



    ingress_priority (optional, int, None)
      Matches ingress priority of the packet. Priority may be derived from VLAN, WMM
or MPLS EXP bit. ``<a class="mw-redirect" href="/wiki/WMM" title="WMM"> Read
more>></a>``



    ipsec_policy (optional, str, None)
      Matches the policy used by IpSec. Value is written in following format:
``<b>direction, policy</b>``. Direction is Used to select whether to match the
policy used for decapsulation or the policy that will be used for encapsulation.
- in - valid in the PREROUTING, INPUT and FORWARD chains
- out - valid in the POSTROUTING, OUTPUT and FORWARD chains
- ipsec - matches if the packet is subject to IpSec processing;
- none - matches packet that is not subject to IpSec processing (for example,
IpSec transport packet).
For example, if router receives Ipsec encapsulated Gre packet, then rule
``ipsec-policy=in,ipsec`` will match Gre packet, but rule ``ipsec-policy=in,none``
will match ESP packet.



    ipv4_options (optional, str, None)
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



    jump_target (optional, str, None)
      Name of the target chain to jump to. Applicable only if ``action=jump``



    layer7_protocol (optional, str, None)
      Layer7 filter name defined in ` layer7 protocol
menu </wiki/Manual:IP/Firewall/L7>`_.



    limit (optional, int, None)
      Matches packets until a given pps limit is exceeded. Parameters are written in
following format: ``count[/time],burst``.
- count - maximum average packet rate measured in packets per ``time`` interval
- time - specifies the time interval in which the packet rate is measured
(optional, 1s will be used if not specified)
- burst - number of packets which are not counted by packet rate



    log_prefix (optional, str, None)
      Adds specified text at the beginning of every log message. Applicable if
``action=log``



    nth (optional, int, None)
      Matches every nth packet. ``<a class="mw-redirect"
href="/wiki/NTH_in_RouterOS_3.x" title="NTH in RouterOS 3.x"> Read more >></a>``



    out_bridge_port (optional, str, None)
      Actual interface the packet is leaving the router, if outgoing interface is
bridge



    out_interface (optional, str, None)
      Interface the packet is leaving the router



    packet_mark (optional, str, None)
      Matches packets marked via mangle facility with particular packet mark. If
no-mark is set, rule will match any unmarked packet.



    packet_size (optional, int, None)
      Matches packets of specified size or size range in bytes.



    per_connection_classifier (optional, str, None)
      PCC matcher allows to divide traffic into equal streams with ability to keep
packets with specific set of options in one particular stream. ``<a
class="mw-redirect" href="/wiki/PCC" title="PCC"> Read more >></a>``



    port (optional, int, None)
      Matches if any (source or destination) port matches the specified list of ports
or port ranges. Applicable only if ``protocol`` is TCP or UDP



    protocol (optional, str, tcp)
      Matches particular IP protocol specified by protocol name or number



    psd (optional, int, None)
      Attempts to detect TCP and UDP scans. Parameters are in following format
``WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight``
- WeightThreshold - total weight of the latest TCP/UDP packets with different
destination ports coming from the same host to be treated as port scan sequence
- DelayThreshold - delay for the packets with different destination ports coming
from the same host to be treated as possible port scan subsequence
- LowPortWeight - weight of the packets with privileged (&lt;1024) destination
port
- HighPortWeight - weight of the packet with non-priviliged destination port



    random (optional, int, None)
      Matches packets randomly with given probability.



    routing_mark (optional, str, None)
      Matches packets marked by mangle facility with particular routing mark



    same_not_by_dst (optional, str, None)
      Specifies whether to take into account or not destination IP address when
selecting a new source IP address. Applicable if ``action=same``



    src_address (optional, str, None)
      Matches packets which source is equal to specified IP or falls into specified IP
range.



    src_address_list (optional, str, None)
      Matches source address of a packet against user-defined ` address
list </wiki/Address_list>`_



    src_address_type (optional, str, None)
      Matches source address type:
- unicast - IP address used for point to point transmission
- local - if address is assigned to one of routers interfaces
- broadcast - packet is sent to all devices in subnet
- multicast - packet is forwarded to defined group of devices



    src_port (optional, int, None)
      List of source ports and ranges of source ports. Applicable only if protocol is
TCP or UDP.



    src_mac_address (optional, str, None)
      Matches source MAC address of the packet



    tcp_mss (optional, int, None)
      Matches TCP MSS value of an IP packet



    to_addresses (optional, str, 0.0.0.0)
      Replace original address with specified one. Applicable if action is dst-nat,
netmap, same, src-nat



    to_ports (optional, int, None)
      Replace original port with specified one. Applicable if action is dst-nat,
redirect, masquerade, netmap, same, src-nat



    ttl (optional, int, None)
      Matches packets TTL value















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

