.. _ros_route_module:


ros_route -- Manage configuration for ``/ip route``
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_route <ros_route_module>` module provides management for RouterOS ``/ip route``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_route <ros_route_module>` will update existing ``/ip route`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_route <ros_route_module>` will create new ``/ip route``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_route <ros_route_module>` will restore related ``/ip route`` to its default value.
   *  :ref:`ros_route <ros_route_module>` will update ``/ip route`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_route <ros_route_module>` will create new ``/ip route``
Overridden:
*  :ref:`ros_route <ros_route_module>` will remove any existing item in ``/ip route``
*  :ref:`ros_route <ros_route_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_route <ros_route_module>` will remove that item from ``/ip route`` configuration



  config (optional, list, None)
    A dictionary for L(ros_route)


    check_gateway (optional, str, None)
      Periodically (every 10 seconds) check gateway by sending either ICMP echo
request (ping) or ARP request (arp). If no response from gateway is received for
10 seconds, request times out. After two timeouts gateway is considered
unreachable. After receiving reply from gateway it is considered reachable and
timeout counter is reset.



    comment (optional, str, None)
      Description of particular route



    distance (optional, str, 1)
      Value used in `route selection <#Route_selection>`_. Routes with smaller distance
value are given preference. If value of this property is not set, then the
default depends on route protocol:
- connected routes: 0
- static routes: 1
- eBGP: 20
- OSPF: 110
- RIP: 120
- MME: 130
- iBGP: 200



    dst_address (optional, str, 0.0.0.0/0)
      IP prefix of route, specifies destination addresses that this route can be used
for. Netmask part of this property specifies how many of the most significant
bits in packet destination address must match this value. If there are several
active routes that match destination address of packet, then the most specific
one (with largest netmask value) is used.



    gateway (optional, str, None)
      Array of IP addresses or interface names. Specifies which host or interface
packets should be sent to. `Connected routes <#Connected_routes>`_ and routes with
blackhole, unreachable or prohibit type do not have this property. Usually value
of this property is a single IP address of a gateway that can be directly
reached through one of routers interfaces (but see `nexthop
lookup <#Nexthop_lookup>`_). `ECMP <#ECMP>`_ routes have more than one gateway value.
Value can be repeated several times.



    pref_src (optional, str, None)
      Which of the local IP addresses to use for locally originated packets that are
sent via this route. Value of this property has no effect on forwarded packets.
If value of this property is set to IP address that is not local address of this
router then the route will be inactive. If pref-src value is not set, then for
locally originated packets that are sent using this route router will choose one
of local addresses attached to the output interface that match destination
prefix of the route (`an example <#Route_lookup_example>`_).



    route_tag (optional, int, None)
      Value of route tag attribute for RIP or OSPF. For RIP only values 0..4294967295
are valid.



    routing_mark (optional, str, None)
      Name of routing table that contains this route. Not set by default which is the
same as main. Packets that are marked by `firewall </wiki/Manual:IP/Firewall>`_.
Not more than 251 routing marks can be added per router.



    scope (optional, str, 30)
      Used in nexthop resolution. Route can resolve nexthop only through routes that
have scope less than or equal to the target-scope of this route. Default value
depends on route protocol:
- connected routes: 10 (if interface is running)
- OSPF, RIP, MME routes: 20
- static routes: 30
- BGP routes: 40
- connected routes: 200 (if interface is not running)



    target_scope (optional, str, 10)
      Used in nexthop resolution. This is the maximum value of scope for a route
through which a nexthop of this route can be resolved. See `nexthop
lookup <#Nexthop_lookup>`_. For iBGP value is set to 30 by default.



    type (optional, str, unicast)
      Routes that do not specify nexthop for packets, but instead perform some other
action on packets have type different from the usual unicast. blackhole route
silently discards packets, while unreachable and prohibit routes send ICMP
Destination Unreachable message (code 1 and 13 respectively) to the source
address of the packet.



    vrf_interface (optional, str, 10)
      VRF interface name















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

