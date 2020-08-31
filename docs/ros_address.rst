.. _ros_address_module:


ros_address -- Manage configuration for ``/ip address``
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_address <ros_address_module>` module provides management for RouterOS ``/ip address``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_address <ros_address_module>` will update existing ``/ip address`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_address <ros_address_module>` will create new ``/ip address``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_address <ros_address_module>` will restore related ``/ip address`` to its default value.
   *  :ref:`ros_address <ros_address_module>` will update ``/ip address`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_address <ros_address_module>` will create new ``/ip address``
Overridden:
*  :ref:`ros_address <ros_address_module>` will remove any existing item in ``/ip address``
*  :ref:`ros_address <ros_address_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_address <ros_address_module>` will remove that item from ``/ip address`` configuration



  config (optional, list, None)
    A dictionary for L(ros_address)


    address (True, str, None)
      IP address



    broadcast (optional, str, 255.255.255.255)
      roadcasting IP address, calculated by default from an IP address and a network
mask. Starting from v5RC6 this parameter is removed



    interface (optional, str, None)
      Interface name the IP address is assigned to



    netmask (optional, str, 0.0.0.0)
      Delimits network address part of the IP address from the host part



    network (optional, str, 0.0.0.0)
      IP address for the network. For point-to-point links it should be the address of
the remote end. Starting from v5RC6 this parameter is configurable only for
addresses with /32 netmask (point to point links)















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

