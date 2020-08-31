.. _ros_dhcp_lease_module:


ros_dhcp_lease -- Manage configuration for ``/ip dhcp-server lease``
====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_dhcp_lease <ros_dhcp_lease_module>` module provides management for RouterOS ``/ip dhcp-server lease``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_dhcp_lease <ros_dhcp_lease_module>` will update existing ``/ip dhcp-server lease`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_dhcp_lease <ros_dhcp_lease_module>` will create new ``/ip dhcp-server lease``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_dhcp_lease <ros_dhcp_lease_module>` will restore related ``/ip dhcp-server lease`` to its default value.
   *  :ref:`ros_dhcp_lease <ros_dhcp_lease_module>` will update ``/ip dhcp-server lease`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_dhcp_lease <ros_dhcp_lease_module>` will create new ``/ip dhcp-server lease``
Overridden:
*  :ref:`ros_dhcp_lease <ros_dhcp_lease_module>` will remove any existing item in ``/ip dhcp-server lease``
*  :ref:`ros_dhcp_lease <ros_dhcp_lease_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_dhcp_lease <ros_dhcp_lease_module>` will remove that item from ``/ip dhcp-server lease`` configuration



  config (optional, list, None)
    A dictionary for L(ros_dhcp_lease)


    address (optional, str, None)
      Specify IP address (or ip pool) for static lease. If set to 0.0.0.0 - pool from
server will be used



    address_list (optional, str, None)
      Address list to which address will be added if lease is bound.



    allow_dual_stack_queue (optional, str, True)
      Creates a single simple queue entry for both IPv4 and IPv6 addresses, uses the
MAC address and DUID for identification. Requires ` IPv6 DHCP
Server </wiki/Manual:IPv6/DHCP_Server>`_ to have this option enabled as well to
work properly.



    always_broadcast (optional, str, None)
      Send all replies as broadcasts



    block_access (optional, str, False)
      Block access for this client



    client_id (optional, str, None)
      If specified, must match DHCP client identifier option of the request



    dhcp_option (optional, str, None)
      Add additional DHCP options from ` option list <#Options>`_.



    dhcp_option_set (optional, str, None)
      Add additional set of DHCP options.



    insert_queue_before (optional, str, None)
      Specify where to place dynamic simple queue entries for static DCHP leases with
rate-limit parameter set.



    lease_time (optional, str, 0s)
      Time that the client may use the address. If set to 0s lease will never expire.



    mac_address (optional, str, 00:00:00:00:00:00)
      If specified, must match the MAC address of the client



    rate_limit (optional, int, None)
      Adds a dynamic simple queue to limit IPs bandwidth to a specified rate.
Requires the lease to be static. Format is: rx-rate[/tx-rate]
[rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold]
[rx-burst-time[/tx-burst-time]]]]. All rates should be numbers with
optional k (1,000s) or M (1,000,000s). If tx-rate is not specified, rx-rate
is as tx-rate too. Same goes for tx-burst-rate and tx-burst-threshold and
tx-burst-time. If both rx-burst-threshold and tx-burst-threshold are not
specified (but burst-rate is specified), rx-rate and tx-rate is used as burst
thresholds. If both rx-burst-time and tx-burst-time are not specified, 1s is
used as default.



    server (optional, str, None)
      Server name which serves this client



    use_src_mac (optional, str, False)
      When this option is set server uses source MAC address instead of received
CHADDR to assign address.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

