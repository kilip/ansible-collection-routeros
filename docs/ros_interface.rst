.. _ros_interface_module:


ros_interface -- Interface Configuration
========================================

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
   *  :ref:`ros_interface <ros_interface_module>` will update existing ``/interface`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_interface <ros_interface_module>` will create new ``/interface``,



  config (optional, list, None)
    A dictionary for L(ros_interface)


    l2mtu (optional, int, None)
      Layer2 Maximum transmission unit. Note that this property can not be configured
on all interfaces. ` Read more&gt;&gt;
 </wiki/Maximum_Transmission_Unit_on_RouterBoards>`_



    mtu (optional, int, None)
      Layer3 Maximum transmission unit



    name (True, str, None)
      Name of an interface















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

