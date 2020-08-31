.. _ros_dns_module:


ros_dns -- Manage configuration for ``/ip dns``
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_dns <ros_dns_module>` module provides management for RouterOS ``/ip dns``.






Parameters
----------

  state (optional, any, None)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_dns <ros_dns_module>` will update existing ``/ip dns`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_dns <ros_dns_module>` will create new ``/ip dns``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_dns <ros_dns_module>` will restore related ``/ip dns`` to its default value.
   *  :ref:`ros_dns <ros_dns_module>` will update ``/ip dns`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_dns <ros_dns_module>` will create new ``/ip dns``
Overridden:
*  :ref:`ros_dns <ros_dns_module>` will remove any existing item in ``/ip dns``
*  :ref:`ros_dns <ros_dns_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_dns <ros_dns_module>` will remove that item from ``/ip dns`` configuration



  config (optional, any, None)
    A dictionary for L(ros_dns)


    allow_remote_requests (optional, str, False)
      Specifies whether to allow network requests



    cache_max_ttl (optional, str, 1w)
      Maximum time-to-live for cache records. In other words, cache records will
expire unconditionally after cache-max-ttl time. Shorter TTL received from DNS
servers are respected.



    cache_size (optional, str, 2048)
      Specifies the size of DNS cache in KiB



    max_concurrent_queries (optional, str, 100)
      Specifies how much concurrent queries are allowed



    max_concurrent_tcp_sessions (optional, str, 20)
      Specifies how much concurrent TCP sessions are allowed



    max_udp_packet_size (optional, str, 4096)
      Maximum size of allowed UDP packet.



    query_server_timeout (optional, str, 2s)
      Specifies how long to wait for query response from one server



    query_total_timeout (optional, str, 10s)
      Specifies how long to wait for query response in total. Note that this setting
must be configured taking into account query-server-timeout and number of used
DNS server.



    servers (optional, str, None)
      List of DNS server IPv4/IPv6 addresses















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

