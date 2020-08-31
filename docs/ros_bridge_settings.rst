.. _ros_bridge_settings_module:


ros_bridge_settings -- Bridge Settings
======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Globally controlled settings and statistics for all bridge interfaces.






Parameters
----------

  state (optional, any, None)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_bridge_settings <ros_bridge_settings_module>` will update existing ``/interface bridge settings`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_bridge_settings <ros_bridge_settings_module>` will create new ``/interface bridge settings``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_bridge_settings <ros_bridge_settings_module>` will restore related ``/interface bridge settings`` to its default value.
   *  :ref:`ros_bridge_settings <ros_bridge_settings_module>` will update ``/interface bridge settings`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_bridge_settings <ros_bridge_settings_module>` will create new ``/interface bridge settings``
Overridden:
*  :ref:`ros_bridge_settings <ros_bridge_settings_module>` will remove any existing item in ``/interface bridge settings``
*  :ref:`ros_bridge_settings <ros_bridge_settings_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_bridge_settings <ros_bridge_settings_module>` will remove that item from ``/interface bridge settings`` configuration



  config (optional, any, None)
    A dictionary for L(ros_bridge_settings)


    use_ip_firewall (optional, str, False)
      Force bridged traffic to also be processed by prerouting, forward and
postrouting sections of IP routing (` Packet
Flow <https://wiki.mikrotik.com/wiki/Manual:Packet_Flow_v6>`_ to traffic in a
bridge. Property use-ip-firewall-for-vlan is required in case bridge
vlan-filtering is used.



    use_ip_firewall_for_pppoe (optional, str, False)
      Send bridged un-encrypted PPPoE traffic to also be processed by
`IP/Firewall <https://wiki.mikrotik.com/wiki/Manual:IP/Firewall>`_ to PPPoE
traffic in a bridge.



    use_ip_firewall_for_vlan (optional, str, False)
      Send bridged VLAN traffic to also be processed by
`IP/Firewall <https://wiki.mikrotik.com/wiki/Manual:IP/Firewall>`_ to VLAN traffic
in a bridge.



    allow_fast_path (optional, str, True)
      Allows `FastPath <https://wiki.mikrotik.com/wiki/Manual:Fast_Path>`_.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

