.. _ros_firewall_filter_module:


ros_firewall_filter -- Manage configuration for ``/ip firewall filter``
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_firewall_filter <ros_firewall_filter_module>` module provides management for RouterOS ``/ip firewall filter``.






Parameters
----------

  state (optional, any, merged)
    Overridden:
*  :ref:`ros_firewall_filter <ros_firewall_filter_module>` will remove any existing item in ``/ip firewall filter``
*  :ref:`ros_firewall_filter <ros_firewall_filter_module>` will create new item using value in the ``argument_spec``



  config (optional, list, None)
    A dictionary for L(ros_firewall_filter)


    action (optional, str, accept)
      Action to take if packet is matched by the rule:
- accept - accept the packet. Packet is not passed to next firewall rule.
- add-dst-to-address-list - add destination address to ` address
list </wiki/Manual:IP/Firewall/Address_list>`_ specified by ``address-list``
parameter
- add-src-to-address-list - add source address to ` address
list </wiki/Manual:IP/Firewall/Address_list>`_ specified by ``address-list``
parameter
- drop - silently drop the packet
- fasttrack-connection - process packets from a connection using FastPath by
enabling ` FastTrack </wiki/Manual:IP/Fasttrack>`_ for the connection
- jump - jump to the user defined chain specified by the value of ``jump-target``
parameter
- log - add a message to the system log containing following data: in-interface,
out-interface, src-mac, protocol, src-ip:port-&gt;dst-ip:port and length of the
packet. After packet is matched it is passed to next rule in the list, similar
as ``passthrough``
- passthrough - if packet is matched by the rule, increase counter and go to
next rule (useful for statistics)
- reject - drop the packet and send an ICMP reject message
- return - passes control back to the chain from where the jump took place
- tarpit - captures and holds TCP connections (replies with SYN/ACK to the
inbound TCP SYN packet)



    address_list (optional, str, None)
      Name of the address list to be used. Applicable if action is
``add-dst-to-address-list`` or ``add-src-to-address-list``



    address_list_timeout (optional, str, 00:00:00)
      Time interval after which the address will be removed from the address list
specified by ``address-list`` parameter. Used in conjunction with
``add-dst-to-address-list`` or ``add-src-to-address-list`` actions
Value of ``00:00:00`` will leave the address in the address list forever



    chain (optional, str, None)
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
Should be used together with connection-state=new and/or with tcp-flags=syn
because matcher is very resource intensive.



    connection_mark (optional, str, None)
      Matches packets marked via mangle facility with particular connection mark. If
no-mark is set, rule will match any unmarked connection.



    connection_nat_state (optional, str, None)
      Can match connections that are srcnatted, dstnatted or both. Note that
connection-state=related connections connection-nat-state is determined by
direction of the first packet. and if connection tracking needs to use dst-nat
to deliver this connection to same hosts as main connection it will be in
connection-nat-state=dstnat even if there are no dst-nat rules at all.



    connection_rate (optional, int, None)
      Connection Rate is a firewall matcher that allow to capture traffic based on
present speed of the connection. ` Read more
&gt;&gt; </wiki/Manual:Connection_Rate>`_



    connection_state (optional, str, None)
      Interprets the connection tracking analysis data for a particular packet:
- established - a packet which belongs to an existing connection
- invalid - a packet that does not have determined state in connection tracking
(usually - severe out-of-order packets, packets with wrong sequence/ack number,
or in case of resource overusage on router), for this reason invalid packet will
not participate in NAT (as only connection-state=new packets do), and will still
contain original source IP address when routed. We strongly suggest to drop all
connection-state=invalid packets in firewall filter forward and input chains
- new - the packet has started a new connection, or otherwise associated with a
connection which has not seen packets in both directions.
- related - a packet which is related to, but not part of an existing
connection, such as ICMP errors or a packet which begins FTP data connection
- untracked - packet which was set to bypass connection tracking in firewall `
RAW </wiki/Manual:IP/Firewall/Raw>`_ tables.



    connection_type (optional, str, None)
      Matches packets from related connections based on information from their
connection tracking helpers. A relevant connection helper must be enabled under
` /ip firewall service-port </wiki/Manual:IP/Services>`_



    content (optional, str, None)
      Match packets that contain specified text



    dscp (optional, int, None)
      Matches DSCP IP header field.



    dst_address (optional, str, None)
      Matches packets which destination is equal to specified IP or falls into
specified IP range.



    dst_address_list (optional, str, None)
      Matches destination address of a packet against user-defined ` address
list </wiki/Manual:IP/Firewall/Address_list>`_



    dst_address_type (optional, str, None)
      Matches destination address type:
- unicast - IP address used for point to point transmission
- local - if dst-address is assigned to one of routers interfaces
- broadcast - packet is sent to all devices in subnet
- multicast - packet is forwarded to defined group of devices



    dst_limit (optional, int, None)
      Matches packets until a given rate is exceeded. Rate is defined as packets per
time interval. As opposed to the limit matcher, every flow has its own limit.
Flow is defined by mode parameter. Parameters are written in following format:
``count[/time],burst,mode[/expire]``.
- count - packet count per time interval per flow to match
- time - specifies the time interval in which the packet count per flow cannot
be exceeded (optional, 1s will be used if not specified)
- burst - initial number of packets per flow to match: this number gets
recharged by one every ``time``/``count``, up to this number
- mode - this parameter specifies what unique fields define flow (src-address,
dst-address, src-and-dst-address, dst-address-and-port, addresses-and-dst-port)
- expire - specifies interval after which flow with no packets will be allowed
to be deleted (optional)



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
      Matches ICMP type:code fields



    in_bridge_port (optional, str, None)
      Actual interface the packet has entered the router, if incoming interface is
bridge. Works only if use-ip-firewall is enabled in bridge settings.



    in_bridge_port_list (optional, str, None)
      Set of interfaces defined in ` interface list </wiki/Manual:Interface/List>`_.
Works the same as in-bridge-port



    in_interface (optional, str, None)
      Interface the packet has entered the router



    in_interface_list (optional, str, None)
      Set of interfaces defined in ` interface list </wiki/Manual:Interface/List>`_.
Works the same as in-interface



    ingress_priority (optional, int, None)
      Matches the priority of an ingress packet. Priority may be derived from VLAN,
WMM, DSCP or MPLS EXP bit. ` read more» </wiki/WMM>`_



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
      Matches packets up to a limited rate (packet rate or bit rate). Rule using this
matcher will match until this limit is reached. Parameters are written in
following format: ``count[/time],burst:mode``.
- count - packet or bit count per time interval to match
- time - specifies the time interval in which the packet or bit count cannot be
exceeded (optional, 1s will be used if not specified)
- burst - initial number of packets or bits to match: this number gets recharged
every 10ms so burst should be at least 1/100 of rate per second
- mode - packet or bit mode



    log_prefix (optional, str, None)
      Adds specified text at the beginning of every log message. Applicable if
``action=log``



    nth (optional, int, None)
      Matches every nth packet. ` Read more
&gt;&gt; </wiki/Manual:NTH_in_RouterOS_3.x>`_



    out_bridge_port (optional, str, None)
      Actual interface the packet is leaving the router, if outgoing interface is
bridge. Works only if use-ip-firewall is enabled in bridge settings.



    out_bridge_port_list (optional, str, None)
      Set of interfaces defined in ` interface list </wiki/Manual:Interface/List>`_.
Works the same as out-bridge-port



    out_interface (optional, str, None)
      Interface the packet is leaving the router



    out_interface_list (optional, str, None)
      Set of interfaces defined in ` interface list </wiki/Manual:Interface/List>`_.
Works the same as out-interface



    packet_mark (optional, str, None)
      Matches packets marked via mangle facility with particular packet mark. If
no-mark is set, rule will match any unmarked packet.



    packet_size (optional, int, None)
      Matches packets of specified size or size range in bytes.



    per_connection_classifier (optional, str, None)
      PCC matcher allows to divide traffic into equal streams with ability to keep
packets with specific set of options in one particular stream. ` Read more
&gt;&gt; </wiki/Manual:PCC>`_



    port (optional, int, None)
      Matches if any (source or destination) port matches the specified list of ports
or port ranges. Applicable only if ``protocol`` is TCP or UDP



    priority (optional, int, None)
      Matches packets priority after a new priority has been set. Priority may be
derived from VLAN, WMM, DSCP, MPLS EXP bit or from priority that has been set
using the set-priority action. ` Read more &gt;&gt; </wiki/WMM>`_



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



    reject_with (optional, str, icmp-network-unreachable)
      Specifies ICMP error to be sent back if packet is rejected. Applicable if
``action=reject``



    routing_table (optional, str, None)
      Matches packets which destination address is resolved in specific a routing
table. More details can be found in the ` Routing Table
Matcher </wiki/Manual:Routing_Table_Matcher>`_ page



    routing_mark (optional, str, None)
      Matches packets marked by mangle facility with particular routing mark



    src_address (optional, str, None)
      Matches packets which source is equal to specified IP or falls into specified IP
range.



    src_address_list (optional, str, None)
      Matches source address of a packet against user-defined ` address
list </wiki/Manual:IP/Firewall/Address_list>`_



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



    tcp_flags (optional, str, None)
      Matches specified TCP flags
- ack - acknowledging data
- cwr - congestion window reduced
- ece - ECN-echo flag (explicit congestion notification)
- fin - close connection
- psh - push function
- rst - drop connection
- syn - new connection
- urg - urgent data



    tcp_mss (optional, int, None)
      Matches TCP MSS value of an IP packet



    tls_host (optional, str, None)
      Allows to match https traffic based on TLS SNI hostname. Accepts `GLOB
syntax <https://en.wikipedia.org/wiki/Glob_(programming>`_) for wildcard matching.
Note that matcher will not be able to match hostname if TLS handshake frame is
fragmented into multiple TCP segments (packets).



    ttl (optional, int, None)
      Matches packets TTL value















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

