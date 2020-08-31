.. _ros_capsman_datapath_module:


ros_capsman_datapath -- Manage configuration for ``/caps-man datapath``
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_capsman_datapath <ros_capsman_datapath_module>` module provides management for RouterOS ``/caps-man datapath``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_capsman_datapath <ros_capsman_datapath_module>` will update existing ``/caps-man datapath`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_capsman_datapath <ros_capsman_datapath_module>` will create new ``/caps-man datapath``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_capsman_datapath <ros_capsman_datapath_module>` will restore related ``/caps-man datapath`` to its default value.
   *  :ref:`ros_capsman_datapath <ros_capsman_datapath_module>` will update ``/caps-man datapath`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_capsman_datapath <ros_capsman_datapath_module>` will create new ``/caps-man datapath``
Overridden:
*  :ref:`ros_capsman_datapath <ros_capsman_datapath_module>` will remove any existing item in ``/caps-man datapath``
*  :ref:`ros_capsman_datapath <ros_capsman_datapath_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_capsman_datapath <ros_capsman_datapath_module>` will remove that item from ``/caps-man datapath`` configuration



  config (optional, list, None)
    A dictionary for L(ros_capsman_datapath)













Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

