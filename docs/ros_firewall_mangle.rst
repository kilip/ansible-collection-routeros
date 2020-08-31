.. _ros_firewall_mangle_module:


ros_firewall_mangle -- Manage configuration for ``/ip firewall mangle``
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_firewall_mangle <ros_firewall_mangle_module>` module provides management for RouterOS ``/ip firewall mangle``.






Parameters
----------

  state (optional, any, merged)
    Overridden:
*  :ref:`ros_firewall_mangle <ros_firewall_mangle_module>` will remove any existing item in ``/ip firewall mangle``
*  :ref:`ros_firewall_mangle <ros_firewall_mangle_module>` will create new item using value in the ``argument_spec``



  config (optional, list, None)
    A dictionary for L(ros_firewall_mangle)


    action (optional, str, accept)
      Action to take if packet is matched by the rule:
- accept - accept the packet. Packet is not passed to next firewall rule.
- add-dst-to-address-list - add destination address to `Address
list </wiki/Address_list>`_ specified by ``address-list`` parameter
- add-src-to-address-list - add source address to `Address
list </wiki/Address_list>`_ specified by ``address-list`` parameter
- change-dscp - change Differentiated Services Code Point (DSCP) field value
specified by the new-dscp parameter
- change-mss - change Maximum Segment Size field value of the packet to a value
specified by the new-mss parameter
- change-ttl - change Time to Live field value of the packet to a value
specified by the new-ttl parameter
- clear-df - clear Do Not Fragment Flag
- fasttrack-connection - shows fasttrack counters, useful for statistics
- jump - jump to the user defined chain specified by the value of ``jump-target``
parameter
- log - add a message to the system log containing following data: in-interface,
out-interface, src-mac, protocol, src-ip:port-&gt;dst-ip:port and length of the
packet. After packet is matched it is passed to next rule in the list, similar
as ``passthrough``
- mark-connection - place a mark specified by the new-connection-mark parameter
on the entire connection that matches the rule
- mark-packet - place a mark specified by the new-packet-mark parameter on a
packet that matches the rule
- mark-routing - place a mark specified by the new-routing-mark parameter on a
packet. This kind of marks is used for policy routing purposes only
- passthrough - if packet is matched by the rule, increase counter and go to
next rule (useful for statistics).
- return - pass control back to the chain from where the jump took place
- route - forces packets to a specific gateway IP by ignoring normal routing
decision (prerouting chain only)
- set-priority - set priority specified by the new-priority parameter on the
packets sent out through a link that is capable of transporting priority (VLAN
or WMM-enabled wireless interface). ` Read
more&gt; </wiki/WMM#How_to_set_priority>`_
- sniff-pc - send a packet to a remote ` RouterOS CALEA </wiki/CALEA>`_ server.
- sniff-tzsp - send packet to a remote TZSP compatible system (such as
Wireshark). Set remote target with ``sniff-target`` and ``sniff-target-port``
parameters (Wireshark recommends port 37008)
- strip-ipv4-options - strip IPv4 option fields from IP header, action does not
actually remove IPv4 options but rather replaces all option octets with NOP,
further matcher with ipv4-options=any will still match the packet.



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
      Specifies to which chain the rule will be added. If the input does not match the
name of an already defined chain, a new chain will be created.



    comment (optional, str, None)
      Descriptive comment for the rule.



    connection_bytes (optional, int, None)
      Matches packets only if a given amount of bytes has been transfered through the
particular connection. 0 - means infinity, for example
``connection-bytes=2000000-0`` means that the rule matches if more than 2MB
(upload and download) has been transfered through the relevant connection



    connection_limit (optional, int, None)
      Matches connections per address or address block after given value is reached.



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
      Connection Rate is a firewall matcher that allows the capture of traffic based
on the present speed of the connection. ``<a class="mw-redirect"
href="/wiki/Connection_Rate" title="Connection Rate"> Read more >></a>``



    connection_state (optional, str, None)
      Interprets the connection tracking analysis data for a particular packet:
- established - a packet which belongs to an existing connection
- invalid - a packet that does not have determined state in connection tracking
(ussualy - sevear out-of-order packets, packets with wrong sequence/ack number,
or in case of resource overusage on router), for this reason invalid packet will
not participate in NAT (as only connection-state=new packets do), and will still
contain original source IP address when routed. We strongly suggest to drop all
connection-state=invalid packets in firewall filter forward and input chains
- new - the packet has started a new connection, or otherwise associated with a
connection which has not seen packets in both directions
- related - a packet which is related to, but not part of an existing
connection, such as ICMP errors or a packet which begins FTP data connection
- untracked packet which was set to bypass connection tracking in `Firewall
RAW <https://wiki.mikrotik.com/wiki/Manual:IP/Firewall/Raw>`_ tables.



    connection_type (optional, str, None)
      Matches packets from related connections based on information from their
connection tracking helpers. A relevant connection helper must be enabled under
` /ip firewall service-port </wiki/IP/Services>`_



    content (optional, str, None)
      Match packets that contain specified text



    dscp (optional, int, None)
      Matches DSCP IP header field.



    dst_address (optional, str, None)
      Matches packets where destination is equal to specified IP or falls into
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



    dst_limit (optional, str, None)
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
      Matches ICMP "type:code" fields



    in_bridge_port (optional, str, None)
      Actual interface the packet has entered the router, if incoming interface is
bridge



    in_interface (optional, str, None)
      Interface the packet has entered the router



    ingress_priority (optional, int, None)
      Matches ingress priority of the packet. Priority may be derived from VLAN, WMM
or MPLS EXP bit. ``<a class="mw-redirect" href="/wiki/WMM" title="WMM"> Read
more >></a>``



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



    new_connection_mark (optional, str, None)

    new_dscp (optional, int, None)
      Sets a new DSCP value for a packet.



    new_mss (optional, int, None)
      Sets a new MSS for a packet. clamp-to-pmtu option dynamically sets the MSS size
acordingly to the Path MTU.



    new_packet_mark (optional, str, None)

    new_priority (optional, str, None)
      Sets a new priority for a packet. This can be the VLAN, WMM, DSCP or MPLS EXP
priority ` Read more &gt;&gt; </wiki/WMM>`_. This property can also be used to set
an internal priority.



    new_routing_mark (optional, str, None)

    new_ttl (optional, string, None)
      New TTL value. Example value:
- decrement:5
- increment:5
- set:10



    nth (optional, int, None)
      Matches every nth packet. `Read more
 <https://wiki.mikrotik.com/wiki/NTH_load_balancing_with_masquerade>`_



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



    passthrough (optional, str, True)
      whether to let the packet to pass further (like action passthrough) into
firewall or not (property only valid some actions).



    per_connection_classifier (optional, str, None)
      PCC matcher allows division of traffic into equal streams with ability to keep
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



    priority (optional, int, None)
      Matches packets priority after a new priority has been set. Priority may be
derived from VLAN, WMM, DSCP, MPLS EXP bit or from internal priority that has
been set using the set-priority action. ``<a class="mw-redirect"
href="/wiki/WMM" title="WMM"> Read more >></a>``



    src_address (optional, str, None)
      Matches packets where source is equal to specified IP or falls into specified IP
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
      Allows to match traffic based on TLS hostname. Accepts `GLOB
syntax <https://en.wikipedia.org/wiki/Glob_(programming>`_) for wildcard matching.
Note that matcher will not be able to match hostname if TLS handshake frame is
fragmented into multiple TCP segments (packets).



    ttl (optional, str, None)
      Matches packets TTL value.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

