.. _ros_firewall_raw_module:


ros_firewall_raw -- Manage configuration for ``/ip firewall raw``
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_firewall_raw <ros_firewall_raw_module>` module provides management for RouterOS ``/ip firewall raw``.






Parameters
----------

  state (optional, any, merged)
    Overridden:
*  :ref:`ros_firewall_raw <ros_firewall_raw_module>` will remove any existing item in ``/ip firewall raw``
*  :ref:`ros_firewall_raw <ros_firewall_raw_module>` will create new item using value in the ``argument_spec``



  config (optional, list, None)
    A dictionary for L(ros_firewall_raw)


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
- jump - jump to the user defined chain specified by the value of ``jump-target``
parameter
- log - add a message to the system log containing following data: in-interface,
out-interface, src-mac, protocol, src-ip:port-&gt;dst-ip:port and length of the
packet. After packet is matched it is passed to next rule in the list, similar
as ``passthrough``
- notrack - do not send packet to connection tracking.
- passthrough - ignore this rule and go to next one (useful for statistics).
- return - passes control back to the chain from where the jump took place



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



    chain (optional, str, None)
      Specifies to which chain rule will be added. If the input does not match the
name of an already defined chain, a new chain will be created.



    comment (optional, str, None)
      Descriptive comment for the rule.



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

    icmp_options (optional, int, None)
      Matches ICMP type:code fileds



    in_bridge_port (optional, str, None)
      Actual interface the packet has entered the router, if incoming interface is
bridge. Works only if use-ip-firewall is enabled in bridge settings.



    in_interface (optional, str, None)
      Interface the packet has entered the router



    in_interface_list (optional, str, None)
      Set of interfaces defined in ` interface list </wiki/Manual:Interface/List>`_.
Works the same as in-interface



    ingress_priority (optional, int, None)
      Matches ingress priority of the packet. Priority may be derived from VLAN, WMM
or MPLS EXP bit. ` Read more&gt;&gt; </wiki/Manual:WMM>`_



    ipsec_policy (optional, str, None)
      Matches the policy used by IPsec. Value is written in following format:
``<b>direction, policy</b>``. Direction is Used to select whether to match the
policy used for decapsulation or the policy that will be used for encapsulation.
- in - valid in the PREROUTING chain
- out - valid in the OUTPUT chain
- ipsec - matches if the packet is subject to IPsec processing;
- none - matches packet that is not subject to IPsec processing (for example,
IpSec transport packet).
For example, if router receives IPsec encapsulated Gre packet, then rule
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



    log (optional, str, None)
      Preferred method of logging instead of ``action=log``



    log_prefix (optional, str, None)
      Adds specified text at the beginning of every log message. Applicable if
``action=log``



    nth (optional, int, None)
      Matches every nth packet. ` Read more
&gt;&gt; </wiki/Manual:NTH_in_RouterOS_3.x>`_



    out_bridge_port (optional, str, None)
      Actual interface the packet is leaving the router, if outgoing interface is
bridge. Works only if use-ip-firewall is enabled in bridge settings.



    out_interface (optional, str, None)
      Interface the packet is leaving the router



    out_interface_list (optional, str, None)
      Set of interfaces defined in ` interface list </wiki/Manual:Interface/List>`_.
Works the same as out-interface



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
      Allows to match traffic based on TLS hostname. Accepts `GLOB
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

