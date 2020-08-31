.. _ros_wireless_cap_module:


ros_wireless_cap -- Manage configuration for ``/interface wireless cap``
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_wireless_cap <ros_wireless_cap_module>` module provides management for RouterOS ``/interface wireless cap``.






Parameters
----------

  state (optional, any, None)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_wireless_cap <ros_wireless_cap_module>` will update existing ``/interface wireless cap`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_wireless_cap <ros_wireless_cap_module>` will create new ``/interface wireless cap``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_wireless_cap <ros_wireless_cap_module>` will restore related ``/interface wireless cap`` to its default value.
   *  :ref:`ros_wireless_cap <ros_wireless_cap_module>` will update ``/interface wireless cap`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_wireless_cap <ros_wireless_cap_module>` will create new ``/interface wireless cap``
Overridden:
*  :ref:`ros_wireless_cap <ros_wireless_cap_module>` will remove any existing item in ``/interface wireless cap``
*  :ref:`ros_wireless_cap <ros_wireless_cap_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_wireless_cap <ros_wireless_cap_module>` will remove that item from ``/interface wireless cap`` configuration



  config (optional, any, None)
    A dictionary for L(ros_wireless_cap)


    enabled (optional, str, False)
      Disable or enable CAP feature



    interfaces (optional, list, None)
      List of wireless interfaces to be controlled by Manager



    certificate (optional, str, None)
      Certificate to use for authenticating



    discovery_interfaces (optional, list, None)
      List of interfaces over which CAP should attempt to discover Manager



    caps_man_addresses (optional, str, empty)
      List of Manager IP addresses that CAP will attempt to contact during discovery



    caps_man_names (optional, list, None)
      An ordered list of CAPs Manager names that the CAP will connect to, if empty -
CAP does not check Manager name



    caps_man_certificate_common_names (optional, list, None)
      List of Manager certificate CommonNames that CAP will connect to, if empty - CAP
does not check Manager certificate CommonName



    bridge (optional, str, None)
      Bridge to which interfaces should be added when local forwarding mode is used



    static_virtual (optional, str, False)
      CAP will create Static Virtual Interfaces instead of Dynamic and will try to
reuse the same interface on reconnect to CAPsMAN if the MAC address will be the
same. Note if two or more interfaces will have the same MAC address the
assignment from the CAPsMAN could be random between those interfaces.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

