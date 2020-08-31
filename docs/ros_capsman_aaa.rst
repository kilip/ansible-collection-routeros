.. _ros_capsman_aaa_module:


ros_capsman_aaa -- Manage configuration for ``/caps-man aaa``
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_capsman_aaa <ros_capsman_aaa_module>` module provides management for RouterOS ``/caps-man aaa``.






Parameters
----------

  state (optional, any, None)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_capsman_aaa <ros_capsman_aaa_module>` will update existing ``/caps-man aaa`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_capsman_aaa <ros_capsman_aaa_module>` will create new ``/caps-man aaa``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_capsman_aaa <ros_capsman_aaa_module>` will restore related ``/caps-man aaa`` to its default value.
   *  :ref:`ros_capsman_aaa <ros_capsman_aaa_module>` will update ``/caps-man aaa`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_capsman_aaa <ros_capsman_aaa_module>` will create new ``/caps-man aaa``
Overridden:
*  :ref:`ros_capsman_aaa <ros_capsman_aaa_module>` will remove any existing item in ``/caps-man aaa``
*  :ref:`ros_capsman_aaa <ros_capsman_aaa_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_capsman_aaa <ros_capsman_aaa_module>` will remove that item from ``/caps-man aaa`` configuration



  config (optional, any, None)
    A dictionary for L(ros_capsman_aaa)


    mac_format (optional, str, xx:xx:xx:xx:xx:xx)
      Controls how MAC address of the client is encoded by Access Point in the
User-Name attribute of the MAC authentication and MAC accounting RADIUS
requests.



    mac_mode (optional, str, None)
      By default Access Point uses an empty password, when sending Access-Request
during MAC authentication. When this property is set to
as-username-and-password, Access Point will use the same value for User-Password
attribute as for the User-Name attribute.



    mac_caching (optional, str, disabled)
      If this value is set to time interval, the Access Point will cache RADIUS MAC
authentication responses for specified time, and will not contact RADIUS server
if matching cache entry already exists. Value disabled will disable cache,
Access Point will always contact RADIUS server.



    interim_update (optional, str, disabled)
      When RADIUS accounting is used, Access Point periodically sends accounting
information updates to the RADIUS server. This property specifies default update
interval that can be overridden by the RADIUS server using the `
Acct-Interim-Interval </wiki/Manual:Interface/Wireless#RADIUS_MAC_authentication>`_
attribute.



    called_format (optional, str, mac:ssid)
      Format of how the "called-id" identifier will be passed to RADIUS. When
configuring radius server clients, you can specify "called-id" in order to
separate multiple entires.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

