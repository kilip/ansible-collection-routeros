.. _ros_dhcp_server_module:


ros_dhcp_server -- Interface Configuration
==========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configuration for */interface*






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_dhcp_server <ros_dhcp_server_module>` will update existing ``/ip dhcp-server`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_dhcp_server <ros_dhcp_server_module>` will create new ``/ip dhcp-server``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_dhcp_server <ros_dhcp_server_module>` will restore related ``/ip dhcp-server`` to its default value.
   *  :ref:`ros_dhcp_server <ros_dhcp_server_module>` will update ``/ip dhcp-server`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_dhcp_server <ros_dhcp_server_module>` will create new ``/ip dhcp-server``
Overridden:
*  :ref:`ros_dhcp_server <ros_dhcp_server_module>` will remove any existing item in ``/ip dhcp-server``
*  :ref:`ros_dhcp_server <ros_dhcp_server_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_dhcp_server <ros_dhcp_server_module>` will remove that item from ``/ip dhcp-server`` configuration



  config (optional, list, None)
    A dictionary for L(ros_dhcp_server)


    add_arp (optional, str, False)
      Whether to add dynamic ARP entry. If set to ``no`` either ` ARP
mode </wiki/Manual:IP/ARP#ARP_Modes>`_ entries should be administratively defined
in ``/ip arp`` submenu.



    address_pool (optional, str, None)
      ` IP pool </wiki/Manual:IP/Pools>`_, from which to take IP addresses for the
clients. If set to static-only, then only the clients that have a static lease
(added in ` lease <#Leases>`_ submenu) will be allowed.



    allow_dual_stack_queue (optional, str, True)
      Creates a single simple queue entry for both IPv4 and IPv6 addresses, uses the
MAC address and DUID for identification. Requires ` IPv6 DHCP
Server </wiki/Manual:IPv6/DHCP_Server>`_ to have this option enabled as well to
work properly.



    always_broadcast (optional, str, False)
      Always send replies as broadcasts even if destination IP is known. Will add
additional load on L2 network.



    authoritative (optional, str, True)
      Option changes the way how server responds to DHCP requests:
- yes - replies to clients request for an address that is not available from
this server, dhcp server will send negative acknowledgment (DHCPNAK)
- no - dhcp server ignores clients requests for addresses that are not available
from this server
- after-10sec-delay - requests with "secs &lt; 10" will be processed as in "no"
setting case and requests with "secs &gt;= 10" will be processed as in "yes"
case.
- after-2sec-delay - requests with "secs &lt; 2" will be processed as in "no"
setting case and requests with "secs &gt;= 2" will be processed as in "yes"
case.
If all requests with "secs &lt; x" should be ignored, then delay-threshold=x
setting should be used.



    bootp_lease_time (optional, str, None)
      Accepts two predefined options or time value:
- forever - lease never expires
- lease-time - use time from lease-time parameter



    bootp_support (optional, str, static)
      Support for BOOTP clients:
- none - do not respond to BOOTP requests
- static - offer only static leases to BOOTP clients
- dynamic - offer static and dynamic leases for BOOTP clients



    client_mac_limit (optional, str, None)
      Specifies whether to limit specific number of clients per single MAC address or
leave unlimited. Note that this setting should not be used in relay setups.



    conflict_detection (optional, str, None)
      Allows to disable/enable conflict detection. If option is enabled, then whenever
server tries to assign a lease it will send ICMP and ARP messages to detect
whether such address in the network already exist. If any of above get reply
address is considered already used. Conflict detection must be disabled when any
kind of DHCP client limitation per port or per mac is used.



    delay_threshold (optional, str, None)
      If secs field in DHCP packet is smaller than delay-threshold, then this packet
is ignored. If set to none - there is no threshold (all DHCP packets are
processed)



    dhcp_option_set (optional, str, None)
      Use custom set of DHCP options defined in option sets menu.



    insert_queue_before (optional, str, None)
      Specify where to place dynamic simple queue entries for static DCHP leases with
rate-limit parameter set.



    interface (optional, str, None)
      Interface on which server will be running.



    lease_script (optional, str, None)
      Script that will be executed after lease is assigned or de-assigned. Internal
"global" variables that can be used in the script:
- leaseBound - set to "1" if bound, otherwise set to "0"
- leaseServerName - dhcp server name
- leaseActMAC - active mac address
- leaseActIP - active IP address
- lease-hostname - client hostname
- lease-options - array of received options



    lease_time (optional, str, 10m)
      The time that a client may use the assigned address. The client will try to
renew this address after a half of this time and will request a new address
after time limit expires.



    name (True, str, None)
      Reference name



    parent_queue (optional, str, None)

    relay (optional, str, 0.0.0.0)
      The IP address of the relay this DHCP server should process requests from:
- 0.0.0.0 - the DHCP server will be used only for direct requests from clients
(no DHCP relay allowed)
- 255.255.255.255 - the DHCP server should be used for any incoming request from
a DHCP relay except for those, which are processed by another DHCP server that
exists in the ``/ip dhcp-server`` submenu.



    src_address (optional, str, 0.0.0.0)
      The address which the DHCP client must send requests to in order to renew an IP
address lease. If there is only one static address on the DHCP server interface
and the source-address is left as 0.0.0.0, then the static address will be used.
If there are multiple addresses on the interface, an address in the same subnet
as the range of given addresses should be used.



    use_framed_as_classless (optional, str, True)
      Forward RADIUS Framed-Route as a DHCP Classless-Static-Route to DHCP-client.
Whenever both Framed-Route and Classless-Static-Route is received
Classless-Static-Route is preferred.



    use_radius (optional, str, False)
      Whether to use RADIUS server:
- no - do not use RADIUS;
- yes - use RADIUS for accounting and lease;
- accounting - use RADIUS for accounting only.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

