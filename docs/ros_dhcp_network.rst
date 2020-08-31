.. _ros_dhcp_network_module:


ros_dhcp_network -- Manage configuration for ``/ip dhcp-server network``
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_dhcp_network <ros_dhcp_network_module>` module provides management for RouterOS ``/ip dhcp-server network``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_dhcp_network <ros_dhcp_network_module>` will update existing ``/ip dhcp-server network`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_dhcp_network <ros_dhcp_network_module>` will create new ``/ip dhcp-server network``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_dhcp_network <ros_dhcp_network_module>` will restore related ``/ip dhcp-server network`` to its default value.
   *  :ref:`ros_dhcp_network <ros_dhcp_network_module>` will update ``/ip dhcp-server network`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_dhcp_network <ros_dhcp_network_module>` will create new ``/ip dhcp-server network``
Overridden:
*  :ref:`ros_dhcp_network <ros_dhcp_network_module>` will remove any existing item in ``/ip dhcp-server network``
*  :ref:`ros_dhcp_network <ros_dhcp_network_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_dhcp_network <ros_dhcp_network_module>` will remove that item from ``/ip dhcp-server network`` configuration



  config (optional, list, None)
    A dictionary for L(ros_dhcp_network)


    address (optional, str, None)
      the network DHCP server(s) will lease addresses from



    boot_file_name (optional, str, None)
      Boot file name



    caps_manager (optional, str, None)
      Comma-separated list of IP addresses for one or more CAPsMAN system managers.
DHCP Option 138 (capwap) will be used.



    dhcp_option (optional, str, None)
      Add additional DHCP options from ` option list <#Options>`_.



    dhcp_option_set (optional, str, None)
      Add additional set of DHCP options.



    dns_none (optional, str, False)
      If set, then DHCP Server will not pass dynamic DNS servers configured on the
router to the DHCP clients if no DNS Server in dns-server is set. By default if
there are no DNS Servers configured, then the dynamic DNS Servers will be passed
to DHCP clients.



    dns_server (optional, str, None)
      the DHCP client will use these as the default DNS servers. Two comma-separated
DNS servers can be specified to be used by the DHCP client as primary and
secondary DNS servers



    domain (optional, str, None)
      The DHCP client will use this as the DNS domain setting for the network
adapter.



    gateway (optional, str, 0.0.0.0)
      The default gateway to be used by `DHCP Client </wiki/DHCP_Client>`_.



    netmask (optional, str, None)
      The actual network mask to be used by DHCP client. If set to 0 - netmask from
network address will be used.



    next_server (optional, str, None)
      IP address of next server to use in bootstrap.



    ntp_server (optional, str, None)
      the DHCP client will use these as the default NTP servers. Two comma-separated
NTP servers can be specified to be used by the DHCP client as primary and
secondary NTP servers



    wins_server (optional, str, None)
      The Windows DHCP client will use these as the default WINS servers. Two
comma-separated WINS servers can be specified to be used by the DHCP client as
primary and secondary WINS servers















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

