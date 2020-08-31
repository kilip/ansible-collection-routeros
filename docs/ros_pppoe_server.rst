.. _ros_pppoe_server_module:


ros_pppoe_server -- Manage configuration for ``/interface pppoe-server``
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_pppoe_server <ros_pppoe_server_module>` module provides management for RouterOS ``/interface pppoe-server``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_pppoe_server <ros_pppoe_server_module>` will update existing ``/interface pppoe-server`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_pppoe_server <ros_pppoe_server_module>` will create new ``/interface pppoe-server``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_pppoe_server <ros_pppoe_server_module>` will restore related ``/interface pppoe-server`` to its default value.
   *  :ref:`ros_pppoe_server <ros_pppoe_server_module>` will update ``/interface pppoe-server`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_pppoe_server <ros_pppoe_server_module>` will create new ``/interface pppoe-server``
Overridden:
*  :ref:`ros_pppoe_server <ros_pppoe_server_module>` will remove any existing item in ``/interface pppoe-server``
*  :ref:`ros_pppoe_server <ros_pppoe_server_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_pppoe_server <ros_pppoe_server_module>` will remove that item from ``/interface pppoe-server`` configuration



  config (optional, list, None)
    A dictionary for L(ros_pppoe_server)


    authentication (optional, list, None)
      Authentication algorithm



    default_profile (optional, str, default)
      Default ` user profile </wiki/PPP_AAA#User_Profiles>`_ to use



    interface (optional, str, None)
      Interface that the clients are connected to



    keepalive_timeout (optional, str, 10)
      Defines the time period (in seconds) after which the router is starting to send
keepalive packets every second. If there is no traffic and no keepalive
responses arrive for that period of time (i.e. 2  keepalive-timeout), the non
responding client is proclaimed disconnected.



    max_mru (optional, str, 1480)
      Maximum Receive Unit. The optimal value is the MTU of the interface the tunnel
is working over reduced by 20 (so, for 1500-byte Ethernet link, set the MTU to
1480 to avoid fragmentation of packets)



    max_mtu (optional, str, 1480)
      Maximum Transmission Unit. The optimal value is the MTU of the interface the
tunnel is working over reduced by 20 (so, for 1500-byte Ethernet link, set the
MTU to 1480 to avoid fragmentation of packets)



    max_sessions (optional, str, None)
      Maximum number of clients that the AC can serve. 0 = no limitations.



    mrru (optional, str, disabled)
      Maximum packet size that can be received on the link. If a packet is bigger than
tunnel MTU, it will be split into multiple packets, allowing full size IP or
Ethernet packets to be sent over the tunnel. ``<a
href="/wiki/Manual:MLPPP_over_single_and_multiple_links" title="Manual:MLPPP
over single and multiple links"> Read more >></a>``



    one_session_per_host (optional, str, False)
      Allow only one session per host (determined by MAC address). If a host tries to
establish a new session, the old one will be closed.



    service_name (optional, str, None)
      The PPPoE service name. Server will accept clients which sends PADI message with
service-names that matches this setting or if service-name field in PADI message
is not set.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

