.. _ros_capsman_configuration_module:


ros_capsman_configuration -- Manage configuration for ``/caps-man configuration``
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_capsman_configuration <ros_capsman_configuration_module>` module provides management for RouterOS ``/caps-man configuration``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_capsman_configuration <ros_capsman_configuration_module>` will update existing ``/caps-man configuration`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_capsman_configuration <ros_capsman_configuration_module>` will create new ``/caps-man configuration``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_capsman_configuration <ros_capsman_configuration_module>` will restore related ``/caps-man configuration`` to its default value.
   *  :ref:`ros_capsman_configuration <ros_capsman_configuration_module>` will update ``/caps-man configuration`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_capsman_configuration <ros_capsman_configuration_module>` will create new ``/caps-man configuration``
Overridden:
*  :ref:`ros_capsman_configuration <ros_capsman_configuration_module>` will remove any existing item in ``/caps-man configuration``
*  :ref:`ros_capsman_configuration <ros_capsman_configuration_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_capsman_configuration <ros_capsman_configuration_module>` will remove that item from ``/caps-man configuration`` configuration



  config (optional, list, None)
    A dictionary for L(ros_capsman_configuration)


    channel (optional, str, None)
      User defined list taken from Channel names (/caps-man channels)



    channel_band (optional, str, None)
      Defines set of used channels.



    channel_control_channel_width (optional, str, None)
      Defines set of used channel widths.



    channel_extension_channel (optional, str, None)
      Extension channel configuration. (E.g. Ce = extension channel is above Control
channel, eC = extension channel is below Control channel)



    channel_frequency (optional, int, None)
      Channel frequency value in MHz on which AP will operate. If left blank, CAPsMAN
will automatically determine the best frequency that is least occupied.



    channel_reselect_interval (optional, str, None)
      Interval after which least occupied frequency is chosen. Works only if
channel.frequency is left blank.



    channel_save_selected (optional, str, False)
      If channel frequency is chosen automatically and channel.reselect-interval is
used, then saves the last picked frequency.



    channel_secondary_frequency (optional, str, auto)
      Specifies the second frequency that will be used for 80+80MHz configuration. Set
it to Disabled in order to disable 80+80MHz capability.



    channel_skip_dfs_channels (optional, str, False)
      If channel.frequency is left blank, the selection will skip DFS channels



    channel_tx_power (optional, int, None)
      TX Power for CAP interface (for the whole interface not for individual chains)
in dBm. It is not possible to set higher than allowed by country regulations or
interface. By default max allowed by country or interface is used.



    channel_width (optional, str, None)
      Sets Channel Width in MHz.



    comment (optional, str, None)
      Short description of the Configuration profile



    country (optional, str, no_country_set)
      Limits available bands, frequencies and maximum transmit power for each
frequency. Also specifies default value of scan-list. Value no_country_set is
an FCC compliant set of channels.



    datapath (optional, str, None)
      User defined list taken from Datapath names (/caps-man datapath)



    datapath_bridge (optional, str, None)
      Bridge to which particular interface should be automatically added as port.
Required only when local-forwarding is not used.



    datapath_bridge_cost (optional, int, None)
      bridge port cost to use when adding as bridge port



    datapath_bridge_horizon (optional, int, None)
      bridge horizon to use when adding as bridge port



    datapath_client_to_client_forwarding (optional, str, False)
      controls if client-to-client forwarding between wireless clients connected to
interface should be allowed, in local forwarding mode this function is performed
by CAP, otherwise it is performed by CAPsMAN



    datapath_interface_list (optional, str, None)

    datapath_l2mtu (optional, str, None)
      set Layer2 MTU size



    datapath_local_forwarding (optional, str, False)
      Controls forwarding mode. If disabled, all L2 and L3 data will be forwarded to
CAPsMAN, and further forwarding decisions will be made only then.
Note, if disabled, make sure that each CAP interface MAC Address that
participates in the same broadcast domain is unique (including local MACs, like
Bridge-MAC).



    datapath_mtu (optional, str, None)
      set MTU size



    datapath_openflow_switch (optional, str, None)
      OpenFlow switch port (when enabled) to add interface to



    datapath_vlan_id (optional, int, None)
      VLAN ID to assign to interface if vlan-mode enables use of VLAN tagging



    datapath_vlan_mode (optional, str, None)
      Enables and specifies the type of VLAN tag to be assigned to the interface
(causes all received data to get tagged with VLAN tag and allows the interface
to only send out data tagged with given tag)



    disconnect_timeout (optional, str, None)

    distance (optional, str, None)

    frame_lifetime (optional, str, None)

    guard_interval (optional, str, any)
      Whether to allow the use of short guard interval (refer to 802.11n MCS
specification to see how this may affect throughput). "any" will use either
short or long, depending on data rate, "long" will use long only.



    hide_ssid (optional, str, None)
      - yes - AP does not include SSID in the beacon frames and does not reply to
probe requests that have broadcast SSID.
- no - AP includes SSID in the beacon frames and replies to probe requests that
have broadcast SSID.
This property has effect only in AP mode. Setting it to yes can remove this
network from the list of wireless networks that are shown by some client
software. Changing this setting does not improve the security of the wireless
network, because SSID is included in other frames sent by the AP.



    hw_protection_mode (optional, str, None)

    hw_retries (optional, str, None)

    installation (optional, str, any)

    keepalive_frames (optional, str, enabled)

    load_balancing_group (optional, str, None)
      Tags the interface to the load balancing group. For a client to connect to
interface in this group, the interface should have the same number of already
connected clients as all other interfaces in the group or smaller. Useful in
setups where ranges of CAPs mostly overlap.



    max_sta_count (optional, int, None)
      Maximum number of associated clients.



    mode (optional, str, ap)
      Set operational mode. Only ap currently supported.



    multicast_helper (optional, str, default)
      When set to full multicast packets will be sent with unicast destination MAC
address, resolving ` multicast
problem </wiki/Manual:Multicast_detailed_example#Multicast_and_Wireless>`_ on a
wireless link. This option should be enabled only on the access point, clients
should be configured in station-bridge mode. Available starting from v5.15.
- disabled - disables the helper and sends multicast packets with multicast
destination MAC addresses
- full - all multicast packet mac address are changed to unicast mac addresses
prior sending them out
- default - default choice that currently is set to disabled. Value can be
changed in future releases.



    name (True, str, None)
      Descriptive name for the Configuration Profile



    rates (optional, str, None)
      User defined list taken from Rates names (/caps-man rates)



    rates_basic (optional, str, None)

    rates_supported (optional, str, None)

    rates_ht_basic_mcs (optional, str, None)
      `Modulation and Coding
Schemes <http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates>`_ that every
connecting client must support. Refer to 802.11n for MCS specification.



    rates_ht_supported_mcs (optional, str, None)
      `Modulation and Coding
Schemes <http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates>`_ that this
device advertises as supported. Refer to 802.11n for MCS specification.



    rates_vht_basic_mcs (optional, str, None)
      `Modulation and Coding
Schemes <http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed>`_ that
every connecting client must support. Refer to 802.11ac for MCS specification.
You can set MCS interval for each of Spatial Stream
- none - will not use selected Spatial Stream
- MCS 0-7 - client must support MCS-0 to MCS-7
- MCS 0-8 - client must support MCS-0 to MCS-8
- MCS 0-9 - client must support MCS-0 to MCS-9



    rates_vht_supported_mcs (optional, str, None)
      `Modulation and Coding
Schemes <http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed>`_ that
this device advertises as supported. Refer to 802.11ac for MCS specification.
You can set MCS interval for each of Spatial Stream
- none - will not use selected Spatial Stream
- MCS 0-7 - devices will advertise as supported MCS-0 to MCS-7
- MCS 0-8 - devices will advertise as supported MCS-0 to MCS-8
- MCS 0-9 - devices will advertise as supported MCS-0 to MCS-9



    rx_chains (optional, str, None)
      Which antennas to use for receive.



    security (optional, str, None)
      Name of security configuration from /caps-man security



    security_authentication_types (optional, str, None)
      Specify the type of Authentication from wpa-psk, wpa2-psk, wpa-eap or wpa2-eap



    security_disable_pmkid (optional, str, None)

    security_eap_methods (optional, str, None)
      - eap-tls - Use built-in EAP TLS authentication.
- passthrough - Access point will relay authentication process to the RADIUS
server.



    security_eap_radius_accounting (optional, str, None)
      specifies if RADIUS traffic accounting should be used if RADIUS authentication
gets done for this client



    security_encryption (optional, list, None)
      Set type of unicast encryption algorithm used



    security_group_encryption (optional, str, aes-ccm)
      Access Point advertises one of these ciphers, multiple values can be selected.
Access Point uses it to encrypt all broadcast and multicast frames. Client
attempts connection only to Access Points that use one of the specified group
ciphers.
- tkip - Temporal Key Integrity Protocol - encryption protocol, compatible with
legacy WEP equipment, but enhanced to correct some of the WEP flaws.
- aes-ccm - more secure WPA encryption protocol, based on the reliable AES
(Advanced Encryption Standard). Networks free of WEP legacy should use only this
cipher.



    security_group_key_update (optional, str, 5m)
      Controls how often Access Point updates the group key. This key is used to
encrypt all broadcast and multicast frames. property only has effect for Access
Points.



    security_passphrase (optional, str, None)
      WPA or WPA2 pre-shared key



    security_tls_certificate (optional, str, None)
      Access Point always needs a certificate when security.tls-mode is set to value
other than no-certificates.



    security_tls_mode (optional, str, None)
      This property has effect only when security.eap-methods contains eap-tls.
- verify-certificate - Require remote device to have valid certificate. Check
that it is signed by known certificate authority. No additional identity
verification is done. Certificate may include information about time period
during which it is valid. If router has incorrect time and date, it may reject
valid certificate because routers clock is outside that period. See also the `
Certificates </wiki/Manual:System/Certificates>`_ configuration.
- dont-verify-certificate - Do not check certificate of the remote device.
Access Point will not require client to provide certificate.
- no-certificates - Do not use certificates. TLS session is established using
2048 bit anonymous Diffie-Hellman key exchange.
- verify-certificate-with-crl - Same as verify-certificate but also checks if
the certificate is valid by checking the Certificate Revocation List.



    ssid (optional, str, None)
      SSID (service set identifier) is a name broadcast in the beacons that identifies
wireless network.



    tx_chains (optional, str, None)
      Which antennas to use for transmit.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

