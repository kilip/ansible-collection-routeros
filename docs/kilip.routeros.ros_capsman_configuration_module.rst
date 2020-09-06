.. _kilip.routeros.ros_capsman_configuration_module

********************************
kilip.routeros.ros_capsman_configuration
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/caps-man configuration**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This modules manages CAPsMan Configuration on Mikrotik RouterOS network devices



==========
Parameters
==========


state
  | **choices**: merged, replaced, overridden, deleted
  | **default**: merged
  | **required**: False
  | **type**: str
  Available state for this module

config
  | **type**: list
  | **elements**: dict
  A dictionary for `/caps-man configuration` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>channel</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>User defined list taken from Channel names (<strong>/caps-man channels</strong>)</p></td></tr><tr><td><b>channel_band</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              2ghz-b
                            </li><li>
                              2ghz-b/g
                            </li><li>
                              2ghz-b/g/n
                            </li><li>
                              2ghz-onlyg
                            </li><li>
                              2ghz-onlyn
                            </li><li>
                              5ghz-a
                            </li><li>
                              5ghz-a/n
                            </li><li>
                              5ghz-a/n/ac
                            </li><li>
                              5ghz-only-ac
                            </li><li>
                              5ghz-onlyn
                            </li></ul></td><td><p>Defines set of used channels.</p></td></tr><tr><td><b>channel_control_channel_width</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              10mhz
                            </li><li>
                              20mhz
                            </li><li>
                              40mhz-turbo
                            </li><li>
                              5mhz
                            </li></ul></td><td><p>Defines set of used channel widths.</p></td></tr><tr><td><b>channel_extension_channel</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              Ce
                            </li><li>
                              Ceee
                            </li><li>
                              disabled
                            </li><li>
                              eC
                            </li><li>
                              eCee
                            </li><li>
                              eeCe
                            </li><li>
                              eeeC
                            </li><li>
                              xx
                            </li><li>
                              xxxx
                            </li></ul></td><td><p>Extension channel configuration. (E.g. Ce = extension channel is above Control channel, eC = extension channel is below Control channel)</p></td></tr><tr><td><b>channel_frequency</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Channel frequency value in MHz on which AP will operate. If left blank, CAPsMAN will automatically determine the best frequency that is least occupied.</p></td></tr><tr><td><b>channel_reselect_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Interval after which least occupied frequency is chosen. Works only if <strong>channel.frequency</strong> is left blank.</p></td></tr><tr><td><b>channel_save_selected</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>If channel frequency is chosen automatically and <strong>channel.reselect-interval</strong> is used, then saves the last picked frequency.</p></td></tr><tr><td><b>channel_secondary_frequency</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Specifies the second frequency that will be used for 80+80MHz configuration. Set it to <strong>Disabled</strong> in order to disable 80+80MHz capability.</p></td></tr><tr><td><b>channel_skip_dfs_channels</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>If <strong>channel.frequency</strong> is left blank, the selection will skip DFS channels</p></td></tr><tr><td><b>channel_tx_power</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>TX Power for CAP interface (for the whole interface not for individual chains) in dBm. It is not possible to set higher than allowed by country regulations or interface. By default max allowed by country or interface is used.</p></td></tr><tr><td><b>channel_width</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Sets Channel Width in MHz.</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Short description of the Configuration profile</p></td></tr><tr><td><b>country</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Limits available bands, frequencies and maximum transmit power for each frequency. Also specifies default value of <strong>scan-list</strong>. Value <em>no_country_set</em> is an FCC compliant set of channels.</p></td></tr><tr><td><b>datapath</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>User defined list taken from Datapath names (<strong>/caps-man datapath</strong>)</p></td></tr><tr><td><b>datapath_bridge</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Bridge to which particular interface should be automatically added as port. Required only when local-forwarding is not used.</p></td></tr><tr><td><b>datapath_bridge_cost</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>bridge port cost to use when adding as bridge port</p></td></tr><tr><td><b>datapath_bridge_horizon</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>bridge horizon to use when adding as bridge port</p></td></tr><tr><td><b>datapath_client_to_client_forwarding</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>controls if client-to-client forwarding between wireless clients connected to interface should be allowed, in local forwarding mode this function is performed by CAP, otherwise it is performed by CAPsMAN</p></td></tr><tr><td><b>datapath_interface_list</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>datapath_l2mtu</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>set Layer2 MTU size</p></td></tr><tr><td><b>datapath_local_forwarding</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Controls forwarding mode. If disabled, all L2 and L3 data will be forwarded to CAPsMAN, and further forwarding decisions will be made only then.<br /><strong>Note</strong>, if disabled, make sure that each CAP interface MAC Address that participates in the same broadcast domain is unique (including local MAC's, like Bridge-MAC).</p></td></tr><tr><td><b>datapath_mtu</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>set MTU size</p></td></tr><tr><td><b>datapath_openflow_switch</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>OpenFlow switch port (when enabled) to add interface to</p></td></tr><tr><td><b>datapath_vlan_id</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>VLAN ID to assign to interface if vlan-mode enables use of VLAN tagging</p></td></tr><tr><td><b>datapath_vlan_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              use-service-tag
                            </li><li>
                              use-tag
                            </li></ul></td><td><p>Enables and specifies the type of VLAN tag to be assigned to the interface (causes all received data to get tagged with VLAN tag and allows the interface to only send out data tagged with given tag)</p></td></tr><tr><td><b>disconnect_timeout</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>distance</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>frame_lifetime</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>guard_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>any</b>&nbsp;&larr;</div></li><li>
                              long
                            </li></ul></td><td><p>Whether to allow the use of short guard interval (refer to 802.11n MCS specification to see how this may affect throughput). 'any' will use either short or long, depending on data rate, 'long' will use long only.</p></td></tr><tr><td><b>hide_ssid</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li>
                              yes
                            </li></ul></td><td><ul><li><em>yes</em> - AP does not include SSID in the beacon frames and does not reply to probe requests that have broadcast SSID.</li><li><em>no</em> - AP includes SSID in the beacon frames and replies to probe requests that have broadcast SSID.</li></ul><p>This property has effect only in AP mode. Setting it to <em>yes</em> can remove this network from the list of wireless networks that are shown by some client software. Changing this setting does not improve the security of the wireless network, because SSID is included in other frames sent by the AP.</p></td></tr><tr><td><b>hw_protection_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>hw_retries</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>installation</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>any</b>&nbsp;&larr;</div></li><li>
                              indoor
                            </li><li>
                              outdoor
                            </li></ul></td><td></td></tr><tr><td><b>keepalive_frames</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li></ul></td><td></td></tr><tr><td><b>load_balancing_group</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Tags the interface to the load balancing group. For a client to connect to interface in this group, the interface should have the same number of already connected clients as all other interfaces in the group or smaller. Useful in setups where ranges of CAPs mostly overlap.</p></td></tr><tr><td><b>max_sta_count</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Maximum number of associated clients.</p></td></tr><tr><td><b>mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Set operational mode. Only ap currently supported.</p></td></tr><tr><td><b>multicast_helper</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>default</b>&nbsp;&larr;</div></li><li>
                              disabled
                            </li><li>
                              full
                            </li></ul></td><td><p>When set to full multicast packets will be sent with unicast destination MAC address, resolving <a href="https://wiki.mikrotik.com/wiki/Manual:Multicast_detailed_example#Multicast_and_Wireless" title="Manual:Multicast detailed example"> multicast problem</a> on a wireless link. This option should be enabled only on the access point, clients should be configured in <strong>station-bridge</strong> mode. Available starting from v5.15.</p><ul><li>disabled - disables the helper and sends multicast packets with multicast destination MAC addresses</li><li>full - all multicast packet mac address are changed to unicast mac addresses prior sending them out</li><li>default - default choice that currently is set to <em>disabled</em>. Value can be changed in future releases.</li></ul></td></tr><tr><td><b>name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Descriptive name for the Configuration Profile</p></td></tr><tr><td><b>rates</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>User defined list taken from Rates names (<strong>/caps-man rates</strong>)</p></td></tr><tr><td><b>rates_basic</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              11Mbps
                            </li><li>
                              11Mbps
                            </li><li>
                              12Mbps
                            </li><li>
                              18Mbps
                            </li><li>
                              1Mbps
                            </li><li>
                              24Mbps
                            </li><li>
                              2Mbps
                            </li><li>
                              36Mbps
                            </li><li>
                              48Mbps
                            </li><li>
                              5.5Mbps
                            </li><li>
                              54Mbps
                            </li><li>
                              6Mbps
                            </li></ul></td><td></td></tr><tr><td><b>rates_ht_basic_mcs</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              mcs-0
                            </li><li>
                              mcs-1
                            </li><li>
                              mcs-10
                            </li><li>
                              mcs-11
                            </li><li>
                              mcs-12
                            </li><li>
                              mcs-13
                            </li><li>
                              mcs-14
                            </li><li>
                              mcs-15
                            </li><li>
                              mcs-16
                            </li><li>
                              mcs-17
                            </li><li>
                              mcs-18
                            </li><li>
                              mcs-19
                            </li><li>
                              mcs-2
                            </li><li>
                              mcs-20
                            </li><li>
                              mcs-21
                            </li><li>
                              mcs-22
                            </li><li>
                              mcs-23
                            </li><li>
                              mcs-3
                            </li><li>
                              mcs-4
                            </li><li>
                              mcs-5
                            </li><li>
                              mcs-6
                            </li><li>
                              mcs-7
                            </li><li>
                              mcs-8
                            </li><li>
                              mcs-9
                            </li></ul></td><td><p><a href="http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates">Modulation and Coding Schemes</a> that every connecting client must support. Refer to 802.11n for MCS specification.</p></td></tr><tr><td><b>rates_ht_supported_mcs</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              mcs-0
                            </li><li>
                              mcs-1
                            </li><li>
                              mcs-10
                            </li><li>
                              mcs-11
                            </li><li>
                              mcs-12
                            </li><li>
                              mcs-13
                            </li><li>
                              mcs-14
                            </li><li>
                              mcs-15
                            </li><li>
                              mcs-16
                            </li><li>
                              mcs-17
                            </li><li>
                              mcs-18
                            </li><li>
                              mcs-19
                            </li><li>
                              mcs-2
                            </li><li>
                              mcs-20
                            </li><li>
                              mcs-21
                            </li><li>
                              mcs-22
                            </li><li>
                              mcs-23
                            </li><li>
                              mcs-3
                            </li><li>
                              mcs-4
                            </li><li>
                              mcs-5
                            </li><li>
                              mcs-6
                            </li><li>
                              mcs-7
                            </li><li>
                              mcs-8
                            </li><li>
                              mcs-9
                            </li></ul></td><td><p><a href="http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates">Modulation and Coding Schemes</a> that this device advertises as supported. Refer to 802.11n for MCS specification.</p></td></tr><tr><td><b>rates_supported</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              11Mbps
                            </li><li>
                              11Mbps
                            </li><li>
                              12Mbps
                            </li><li>
                              18Mbps
                            </li><li>
                              1Mbps
                            </li><li>
                              24Mbps
                            </li><li>
                              2Mbps
                            </li><li>
                              36Mbps
                            </li><li>
                              48Mbps
                            </li><li>
                              5.5Mbps
                            </li><li>
                              54Mbps
                            </li><li>
                              6Mbps
                            </li></ul></td><td></td></tr><tr><td><b>rates_vht_basic_mcs</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              MCS 0-7
                            </li><li>
                              MCS 0-8
                            </li><li>
                              MCS 0-9
                            </li><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li></ul></td><td><p><a href="http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed">Modulation and Coding Schemes</a> that every connecting client must support. Refer to 802.11ac for MCS specification. You can set MCS interval for each of Spatial Stream</p><ul><li><em>none</em> - will not use selected Spatial Stream</li><li><em>MCS 0-7</em> - client must support MCS-0 to MCS-7</li><li><em>MCS 0-8</em> - client must support MCS-0 to MCS-8</li><li><em>MCS 0-9</em> - client must support MCS-0 to MCS-9</li></ul></td></tr><tr><td><b>rates_vht_supported_mcs</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              MCS 0-7
                            </li><li>
                              MCS 0-8
                            </li><li>
                              MCS 0-9
                            </li><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li></ul></td><td><p><a href="http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed">Modulation and Coding Schemes</a> that this device advertises as supported. Refer to 802.11ac for MCS specification. You can set MCS interval for each of Spatial Stream</p><ul><li><em>none</em> - will not use selected Spatial Stream</li><li><em>MCS 0-7</em> - devices will advertise as supported MCS-0 to MCS-7</li><li><em>MCS 0-8</em> - devices will advertise as supported MCS-0 to MCS-8</li><li><em>MCS 0-9</em> - devices will advertise as supported MCS-0 to MCS-9</li></ul></td></tr><tr><td><b>rx_chains</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              0
                            </li><li>
                              1
                            </li><li>
                              2
                            </li><li>
                              3
                            </li></ul></td><td><p>Which antennas to use for receive.</p></td></tr><tr><td><b>security</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of security configuration from <strong>/caps-man security</strong></p></td></tr><tr><td><b>security_authentication_types</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              wpa-psk
                            </li><li>
                              wpa2-psk
                            </li><li>
                              wpa-eap
                            </li><li>
                              wpa2-eap
                            </li></ul></td><td><p>Specify the type of Authentication from <strong>wpa-psk</strong>, <strong>wpa2-psk</strong>, <strong>wpa-eap</strong> or <strong>wpa2-eap</strong></p></td></tr><tr><td><b>security_disable_pmkid</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>security_eap_methods</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              eap-tls
                            </li><li>
                              passthrough
                            </li></ul></td><td><ul><li>eap-tls - Use built-in EAP TLS authentication.</li><li>passthrough - Access point will relay authentication process to the RADIUS server.</li></ul></td></tr><tr><td><b>security_eap_radius_accounting</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>specifies if RADIUS traffic accounting should be used if RADIUS authentication gets done for this client</p></td></tr><tr><td><b>security_encryption</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              aes-ccm
                            </li><li>
                              tkip
                            </li></ul></td><td><p>Set type of unicast encryption algorithm used</p></td></tr><tr><td><b>security_group_encryption</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>aes-ccm</b>&nbsp;&larr;</div></li><li>
                              tkip
                            </li></ul></td><td><p>Access Point advertises one of these ciphers, multiple values can be selected. Access Point uses it to encrypt all broadcast and multicast frames. Client attempts connection only to Access Points that use one of the specified group ciphers.</p><ul><li>tkip - Temporal Key Integrity Protocol - encryption protocol, compatible with legacy WEP equipment, but enhanced to correct some of the WEP flaws.</li><li>aes-ccm - more secure WPA encryption protocol, based on the reliable AES (Advanced Encryption Standard). Networks free of WEP legacy should use only this cipher.</li></ul></td></tr><tr><td><b>security_group_key_update</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Controls how often Access Point updates the group key. This key is used to encrypt all broadcast and multicast frames. property only has effect for Access Points.</p></td></tr><tr><td><b>security_passphrase</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>WPA or WPA2 pre-shared key</p></td></tr><tr><td><b>security_tls_certificate</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              name
                            </li><li>
                              none
                            </li></ul></td><td><p>Access Point always needs a certificate when <strong>security.tls-mode</strong> is set to value other than <strong>no-certificates</strong>.</p></td></tr><tr><td><b>security_tls_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              dont-verify-certificate
                            </li><li>
                              no-certificates
                            </li><li>
                              verify-certificate
                            </li><li>
                              verify-certificate-with-crl
                            </li></ul></td><td><p>This property has effect only when <strong>security.eap-methods</strong> contains <em>eap-tls</em>.</p><ul><li>verify-certificate - Require remote device to have valid certificate. Check that it is signed by known certificate authority. No additional identity verification is done. Certificate may include information about time period during which it is valid. If router has incorrect time and date, it may reject valid certificate because router's clock is outside that period. See also the <a href="https://wiki.mikrotik.com/wiki/Manual:System/Certificates" title="Manual:System/Certificates"> Certificates</a> configuration.</li><li>dont-verify-certificate - Do not check certificate of the remote device. Access Point will not require client to provide certificate.</li><li>no-certificates - Do not use certificates. TLS session is established using 2048 bit anonymous Diffie-Hellman key exchange.</li><li>verify-certificate-with-crl - Same as verify-certificate but also checks if the certificate is valid by checking the Certificate Revocation List.</li></ul></td></tr><tr><td><b>ssid</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>SSID (service set identifier) is a name broadcast in the beacons that identifies wireless network.</p></td></tr><tr><td><b>tx_chains</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              0
                            </li><li>
                              1
                            </li><li>
                              2
                            </li><li>
                              3
                            </li></ul></td><td><p>Which antennas to use for transmit.</p></td></tr></table>



========
Examples
========




------------
Using merged
------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /caps-man configuration export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man configuration
    add name=test



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge configuration with devie configuration
      kilip.routeros.ros_capsman_configuration:
        state: merged
        config:
          - name: test
            datapath_bridge: br-trunk
            rx_chains:
              - 0
              - 1
              - 2
          - name: new
            datapath_bridge: br-trunk
        
      

**Executed Command**


.. code-block:: ssh

    /caps-man configuration set [ find name=test ] datapath.bridge=br-trunk rx-chains=0,1,2
    /caps-man configuration add name=new datapath.bridge=br-trunk


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /caps-man configuration export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man configuration
    add name=test datapath.bridge=br-trunk rx-chains=0,1,2
    add name=new datapath.bridge=br-trunk


