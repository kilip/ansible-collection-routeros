.. _ros_capsman_channels_module:


ros_capsman_channels -- Manage configuration for ``/caps-man channels``
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_capsman_channels <ros_capsman_channels_module>` module provides management for RouterOS ``/caps-man channels``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_capsman_channels <ros_capsman_channels_module>` will update existing ``/caps-man channels`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_capsman_channels <ros_capsman_channels_module>` will create new ``/caps-man channels``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_capsman_channels <ros_capsman_channels_module>` will restore related ``/caps-man channels`` to its default value.
   *  :ref:`ros_capsman_channels <ros_capsman_channels_module>` will update ``/caps-man channels`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_capsman_channels <ros_capsman_channels_module>` will create new ``/caps-man channels``
Overridden:
*  :ref:`ros_capsman_channels <ros_capsman_channels_module>` will remove any existing item in ``/caps-man channels``
*  :ref:`ros_capsman_channels <ros_capsman_channels_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_capsman_channels <ros_capsman_channels_module>` will remove that item from ``/caps-man channels`` configuration



  config (optional, list, None)
    A dictionary for L(ros_capsman_channels)


    band (optional, str, None)
      Define operational radio frequency band and mode taken from hardware capability
of wireless card



    comment (optional, str, None)
      Short description of the Channel Group profile



    extension_channel (optional, str, None)
      Extension channel configuration. (E.g. Ce = extension channel is above Control
channel, eC = extension channel is below Control channel)



    frequency (optional, int, None)
      Channel frequency value in MHz on which AP will operate.



    name (True, str, None)
      Descriptive name for the Channel Group Profile



    tx_power (optional, int, None)
      TX Power for CAP interface (for the whole interface not for individual chains)
in dBm. It is not possible to set higher than allowed by country regulations or
interface. By default max allowed by country or interface is used.



    width (optional, str, None)
      Sets Channel Width in MHz. (E.g. 20, 40)



    save_selected (optional, str, True)
      Saves selected channel for the CAP Radio - will select this channel after the
CAP reconnects to CAPsMAN and use it till the channel Re-optimize is done for
this CAP.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

