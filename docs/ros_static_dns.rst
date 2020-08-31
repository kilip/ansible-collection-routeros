.. _ros_static_dns_module:


ros_static_dns -- Manage configuration for ``/ip dns static``
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_static_dns <ros_static_dns_module>` module provides management for RouterOS ``/ip dns static``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_static_dns <ros_static_dns_module>` will update existing ``/ip dns static`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_static_dns <ros_static_dns_module>` will create new ``/ip dns static``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_static_dns <ros_static_dns_module>` will restore related ``/ip dns static`` to its default value.
   *  :ref:`ros_static_dns <ros_static_dns_module>` will update ``/ip dns static`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_static_dns <ros_static_dns_module>` will create new ``/ip dns static``
Overridden:
*  :ref:`ros_static_dns <ros_static_dns_module>` will remove any existing item in ``/ip dns static``
*  :ref:`ros_static_dns <ros_static_dns_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_static_dns <ros_static_dns_module>` will remove that item from ``/ip dns static`` configuration



  config (optional, list, None)
    A dictionary for L(ros_static_dns)


    address (optional, str, None)
      IP address to resolve domain name with



    name (True, str, None)
      DNS name to be resolved to a given IP address.



    regex (optional, str, None)
      DNS regex



    ttl (optional, str, None)
      time-to-live of the DNS record



    type (optional, str, None)
      type of the DNS record. Available values are: A, AAAA, CNAME, FWD, MX, NS,
NXDOMAIN, SRV, TXT















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

