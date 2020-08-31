.. _ros_firewall_address_list_module:


ros_firewall_address_list -- Manage configuration for ``/ip firewall address-list``
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_firewall_address_list <ros_firewall_address_list_module>` module provides management for RouterOS ``/ip firewall address-list``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_firewall_address_list <ros_firewall_address_list_module>` will update existing ``/ip firewall address-list`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_firewall_address_list <ros_firewall_address_list_module>` will create new ``/ip firewall address-list``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_firewall_address_list <ros_firewall_address_list_module>` will restore related ``/ip firewall address-list`` to its default value.
   *  :ref:`ros_firewall_address_list <ros_firewall_address_list_module>` will update ``/ip firewall address-list`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_firewall_address_list <ros_firewall_address_list_module>` will create new ``/ip firewall address-list``
Overridden:
*  :ref:`ros_firewall_address_list <ros_firewall_address_list_module>` will remove any existing item in ``/ip firewall address-list``
*  :ref:`ros_firewall_address_list <ros_firewall_address_list_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_firewall_address_list <ros_firewall_address_list_module>` will remove that item from ``/ip firewall address-list`` configuration



  config (optional, list, None)
    A dictionary for L(ros_firewall_address_list)


    address (True, str, None)
      A single IP address or range of IPs to add to address list or DNS name. You can
input for example, 192.168.0.0-192.168.1.255 and it will auto modify the typed
entry to 192.168.0.0/23 on saving.



    list (True, str, None)
      Name for the address list of the added IP address



    timeout (optional, str, None)
      Time after address will be removed from address list. If timeout is not
specified, the address will be stored into the address list permanently.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

