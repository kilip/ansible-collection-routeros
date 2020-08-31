.. _ros_vlan_module:


ros_vlan -- VLAN Interface Configuration
========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Virtual Local Area Network (VLAN) is a Layer 2 method
that allows multiple Virtual LANs on a single physical interface (ethernet, wireless, etc.),
giving the ability to segregate LANs efficiently.







Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_vlan <ros_vlan_module>` will update existing ``/interface vlan`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_vlan <ros_vlan_module>` will create new ``/interface vlan``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_vlan <ros_vlan_module>` will restore related ``/interface vlan`` to its default value.
   *  :ref:`ros_vlan <ros_vlan_module>` will update ``/interface vlan`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_vlan <ros_vlan_module>` will create new ``/interface vlan``
Overridden:
*  :ref:`ros_vlan <ros_vlan_module>` will remove any existing item in ``/interface vlan``
*  :ref:`ros_vlan <ros_vlan_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_vlan <ros_vlan_module>` will remove that item from ``/interface vlan`` configuration



  config (optional, list, None)
    A dictionary for L(ros_vlan)


    arp (optional, str, enabled)
      Address Resolution Protocol mode



    interface (True, str, None)
      Name of physical interface on top of which VLAN will work



    l2mtu (optional, int, None)
      Layer2 MTU. For VLANS this value is not configurable. ` Read
more&gt;&gt; </wiki/Maximum_Transmission_Unit_on_RouterBoards>`_



    mtu (optional, str, 1500)
      Layer3 Maximum transmission unit



    name (True, str, None)
      Interface name



    use_service_tag (optional, str, None)
      802.1ad compatible Service Tag



    vlan_id (optional, str, 1)
      Virtual LAN identifier or tag that is used to distinguish VLANs. Must be equal
for all computers that belong to the same VLAN.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

