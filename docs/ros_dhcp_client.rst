.. _ros_dhcp_client_module:


ros_dhcp_client -- Manage configuration for ``/ip dhcp-client``
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_dhcp_client <ros_dhcp_client_module>` module provides management for RouterOS ``/ip dhcp-client``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_dhcp_client <ros_dhcp_client_module>` will update existing ``/ip dhcp-client`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_dhcp_client <ros_dhcp_client_module>` will create new ``/ip dhcp-client``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_dhcp_client <ros_dhcp_client_module>` will restore related ``/ip dhcp-client`` to its default value.
   *  :ref:`ros_dhcp_client <ros_dhcp_client_module>` will update ``/ip dhcp-client`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_dhcp_client <ros_dhcp_client_module>` will create new ``/ip dhcp-client``
Overridden:
*  :ref:`ros_dhcp_client <ros_dhcp_client_module>` will remove any existing item in ``/ip dhcp-client``
*  :ref:`ros_dhcp_client <ros_dhcp_client_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_dhcp_client <ros_dhcp_client_module>` will remove that item from ``/ip dhcp-client`` configuration



  config (optional, list, None)
    A dictionary for L(ros_dhcp_client)


    add_default_route (optional, str, True)
      Whether to install default route in routing table received from dhcp server. By
default RouterOS client complies to RFC and ignores option 3 if classless option
121 is received. To force client not to ignore option 3 set special-classless.
This parameter is available in v6rc12+
- yes - adds classless route if received, if not then add default route (old
behavior)
- special-classless - adds both classless route if received and default route
(MS style)



    client_id (optional, str, None)
      Corresponds to the settings suggested by the network administrator or ISP. If
not specified, clients MAC address will be sent



    comment (optional, str, None)
      Short description of the client



    default_route_distance (optional, int, None)
      Distance of default route. Applicable if ``add-default-route`` is set to ``yes``.



    disabled (optional, str, True)

    host_name (optional, str, None)
      Host name of the client sent to a DHCP server. If not specified, clients system
identity will be used.



    interface (optional, str, None)
      Interface on which DHCP client will be running.



    script (optional, str, None)
      Execute script on status change. This parameter is available in v6.39rc33+ These
are available variables that are accessible for the event script:
- bound - 1 - lease is added/changed; 0 - lease is removed
- server-address - server address
- lease-address - lease address provided by server
- interface - name of interface on which client is configured
- gateway-address - gateway address provided by server
- vendor-specific - stores value of option 43 received from DHCP server
- lease-options - array of received options
L( ``Example >>``,/wiki/Manual:IP/DHCP_Client#Lease_script_example)



    use_peer_dns (optional, str, True)
      Whether to accept the ` DNS </wiki/Manual:IP/DNS>`_. (Will override the settings
put in the ``/ip dns`` submenu.



    use_peer_ntp (optional, str, True)
      Whether to accept the ` NTP </wiki/Manual:System/Time#NTP_client_and_server>`_.
(Will override the settings put in the ``/system ntp client`` submenu)















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

