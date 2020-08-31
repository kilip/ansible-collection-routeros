.. _ros_bridge_module:


ros_bridge -- Bridge Interface Setup
====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_bridge <ros_bridge_module>` will configure resource in ``/interface bridge``






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_bridge <ros_bridge_module>` will update existing ``/interface bridge`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_bridge <ros_bridge_module>` will create new ``/interface bridge``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_bridge <ros_bridge_module>` will restore related ``/interface bridge`` to its default value.
   *  :ref:`ros_bridge <ros_bridge_module>` will update ``/interface bridge`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_bridge <ros_bridge_module>` will create new ``/interface bridge``
Overridden:
*  :ref:`ros_bridge <ros_bridge_module>` will remove any existing item in ``/interface bridge``
*  :ref:`ros_bridge <ros_bridge_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_bridge <ros_bridge_module>` will remove that item from ``/interface bridge`` configuration



  config (optional, list, None)
    A dictionary for L(ros_bridge)


    add_dhcp_option82 (optional, str, False)
      Whether to add DHCP Option-82 information (Agent Remote ID and Agent Circuit ID)
to DHCP packets. Can be used together with Option-82 capable DHCP server to
assign IP addresses and implement policies. This property only has effect when
dhcp-snooping is set to ``yes``.



    admin_mac (optional, str, None)
      Static MAC address of the bridge. This property only has effect when auto-mac is
set to ``no``.



    ageing_time (optional, str, 00:05:00)
      How long a hosts information will be kept in the bridge database.



    arp (optional, str, enabled)
      Address Resolution Protocol setting
- ``disabled`` - the interface will not use ARP
- ``enabled`` - the interface will use ARP
- ``proxy-arp`` - the interface will use the ARP proxy feature
- ``reply-only`` - the interface will only reply to requests originated from
matching IP address/MAC address combinations which are entered as static entries
in the `IP/ARP <https://wiki.mikrotik.com/wiki/Manual:IP/ARP>`_ table. Therefore
for communications to be successful, a valid static entry must already exist.



    arp_timeout (optional, str, auto)
      ARP timeout is time how long ARP record is kept in ARP table after no packets
are received from IP. Value ``auto`` equals to the value of arp-timeout in
`IP/Settings <https://wiki.mikrotik.com/wiki/Manual:IP/Settings>`_, default is
30s.



    auto_mac (optional, str, True)
      Automatically select one MAC address of bridge ports as a bridge MAC address.



    comment (optional, str, None)
      Short description of the interface.



    dhcp_snooping (optional, str, False)
      Enables or disables DHCP Snooping on the bridge.



    disabled (optional, str, False)
      Changes whether the bridge is disabled.



    ether_type (optional, str, 33024)
      Changes the EtherType, which will be used to determine if a packet has a VLAN
tag. Packets that have a matching EtherType are considered as tagged packets.
This property only has effect when vlan-filtering is set to ``yes``.



    fast_forward (optional, str, True)
      Special and faster case of
`FastPath <https://wiki.mikrotik.com/wiki/Manual:Fast_Path>`_ section.



    forward_delay (optional, str, 00:00:15)
      Time which is spent during the initialization phase of the bridge interface
(i.e., after router startup or enabling the interface) in listening/learning
state before the bridge will start functioning normally.



    frame_types (optional, str, admit-all)
      Specifies allowed ingress frame types on a bridge port. This property only has
effect when vlan-filtering is set to ``yes``.



    igmp_snooping (optional, str, False)
      Enables multicast group and port learning to prevent multicast traffic from
flooding all interfaces in a bridge.



    igmp_version (optional, str, 2)
      Selects the IGMP version in which IGMP general membership queries will be
generated. This property only has effect when igmp-snooping is set to ``yes``.



    ingress_filtering (optional, str, False)
      Enables or disables VLAN ingress filtering, which checks if the ingress port is
a member of the received VLAN ID in the bridge VLAN table. Should be used with
frame-types to specify if the ingress traffic should be tagged or untagged. This
property only has effect when vlan-filtering is set to ``yes``.



    last_member_interval (optional, str, 1s)
      If a port has fast-leave set to ``no`` and a bridge port receives a IGMP Leave
message, then a IGMP Snooping enabled bridge will send a IGMP query to make sure
that no devices has subscribed to a certain multicast stream on a bridge port.
If a IGMP Snooping enabled bridge does not receive a IGMP membership report
after amount of last-member-interval, then the bridge considers that no one has
subscribed to a certain multicast stream and can stop forwarding it. This
property only has effect when igmp-snooping is set to ``yes``.



    last_member_query_count (optional, str, 2)
      How many times should last-member-interval pass until a IGMP Snooping bridge
will stop forwarding a certain multicast stream. This property only has effect
when igmp-snooping is set to ``yes``.



    max_hops (optional, str, 20)
      Bridge count which BPDU can pass in a MSTP enabled network in the same region
before BPDU is being ignored. This property only has effect when protocol-mode
is set to ``mstp``.



    max_message_age (optional, str, 00:00:20)
      How long to remember Hello messages received from other STP/RSTP enabled
bridges. This property only has effect when protocol-mode is set to ``stp`` or
``rstp``.



    membership_interval (optional, str, 4m20s)
      Amount of time after an entry in the Multicast Database (MDB) is removed if a
IGMP membership report is not received on a certain port. This property only has
effect when igmp-snooping is set to ``yes``.



    mld_version (optional, str, 1)
      Selects the MLD version. Version 2 adds support for source-specific multicast.
This property only has effect when RouterOS IPv6 package is enabled and
igmp-snooping is set to ``yes``.



    mtu (optional, str, 1500)
      Maximum Transmission Unit



    multicast_querier (optional, str, False)
      Multicast querier generates IGMP general membership queries to which all IGMP
capable devices respond with a IGMP membership report, usually a PIM (multicast)
router generates these queries. By using this property you can make a IGMP
Snooping enabled bridge to generate IGMP general membership queries. This
property should be used whenever there is no PIM (multicast) router in a Layer2
network or IGMP packets must be sent through multiple IGMP Snooping enabled
bridges to reach a PIM (multicast) router. Without a multicast querier in a
Layer2 network the Multicast Database (MDB) is not being updated and IGMP
Snooping will not function properly. This property only has effect when
igmp-snooping is set to ``yes``.



    multicast_router (optional, str, temporary-query)
      Changes the state of a bridge itself if IGMP membership reports are going to be
forwarded to it. This property can be used to forward IGMP membership reports to
the bridge for statistics or to analyse them.
- ``disabled`` - IGMP membership reports are not forwarded to the bridge itself
regardless what is connected to it.
- ``permanent`` - IGMP membership reports are forwarded through this the bridge
itself regardless what is connected to it.
- ``temporary-query`` - automatically detect multicast routers and IGMP Snooping
enabled bridges. This property only has effect when igmp-snooping is set to
``yes``.



    name (True, str, None)
      Name of the bridge interface



    priority (optional, int, None)
      Bridge priority, used by STP to determine root bridge, used by MSTP to determine
CIST and IST regional root bridge. This property has no effect when
protocol-mode is set to ``none``.



    protocol_mode (optional, str, rstp)
      Select Spanning tree protocol (STP) or Rapid spanning tree protocol (RSTP) to
ensure a loop-free topology for any bridged LAN. RSTP provides for faster
spanning tree convergence after a topology change. Select MSTP to ensure
loop-free topology across multiple VLANs. Since RouterOS v6.43 it is possible to
forward Reserved MAC addresses that are in 01:80:C2:XX:XX:XX range, this can be
done by setting the protocol-mode to ``none``.



    pvid (optional, str, 1)
      Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is
assigned to. It applies e.g. to frames sent from bridge IP and destined to a
bridge port. This property only has effect when vlan-filtering is set to ``yes``.



    querier_interval (optional, str, 4m15s)
      Used to change the interval how often a bridge checks if it is the active
multicast querier. This property only has effect when igmp-snooping and
multicast-querier is set to ``yes``.



    query_interval (optional, str, 2m5s)
      Used to change the interval how often IGMP general membership queries are sent
out. This property only has effect when igmp-snooping and multicast-querier is
set to ``yes``.



    query_response_interval (optional, str, 10s)
      Interval in which a IGMP capable device must reply to a IGMP query with a IGMP
membership report. This property only has effect when igmp-snooping and
multicast-querier is set to ``yes``.



    region_name (optional, str, None)
      MSTP region name. This property only has effect when protocol-mode is set to
``mstp``.



    region_revision (optional, str, None)
      MSTP configuration revision number. This property only has effect when
protocol-mode is set to ``mstp``.



    startup_query_count (optional, str, 2)
      Specifies how many times must startup-query-interval pass until the bridge
starts sending out IGMP general membership queries periodically. This property
only has effect when igmp-snooping and multicast-querier is set to ``yes``.



    startup_query_interval (optional, str, 31s250ms)
      Used to change the amount of time after a bridge starts sending out IGMP general
membership queries after the bridge is enabled. This property only has effect
when igmp-snooping and multicast-querier is set to ``yes``.



    transmit_hold_count (optional, str, 6)
      The Transmit Hold Count used by the Port Transmit state machine to limit
transmission rate.



    vlan_filtering (optional, str, False)
      Globally enables or disables VLAN functionality for bridge.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

