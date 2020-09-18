.. _kilip.routeros.kilip.routeros.ros_wireless_module

********************************
kilip.routeros.kilip.routeros.ros_wireless
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface wireless**

.. contents::
   :local:
   :depth: 2

========
Synopsis
========

-  This module manages the Wireless configuration of Mikrotik RouterOS network devices.

==========
Parameters
==========

state
  | **choices**: merged, replaced
  | **default**: merged
  | **required**: False
  | **type**: str
  Available state for this module

config
  | **type**: list
  | **elements**: dict
  A dictionary for `/interface wireless` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>adaptive_noise_immunity</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              ap-and-client-mode
                            </li><li>
                              client-mode
                            </li><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li></ul></td><td><p>This property is only effective for cards based on Atheros chipset.</p></td></tr><tr><td><b>allow_sharedkey</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Allow WEP Shared Key clients to connect. Note that no authentication is done for these clients (WEP Shared keys are not compared to anything) - they are just accepted at once (if access list allows that)</p></td></tr><tr><td><b>ampdu_priorities</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              0
                            </li><li>
                              1
                            </li><li>
                              2
                            </li><li>
                              3
                            </li><li>
                              4
                            </li><li>
                              5
                            </li><li>
                              6
                            </li><li>
                              7
                            </li></ul></td><td><p>Frame priorities for which AMPDU sending (aggregating frames and sending using block acknowledgment) should get negotiated and used. Using AMPDUs will increase throughput, but may increase latency, therefore, may not be desirable for real-time traffic (voice, video). Due to this, by default AMPDUs are enabled only for best-effort traffic.</p></td></tr><tr><td><b>amsdu_limit</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Max AMSDU that device is allowed to prepare when negotiated. AMSDU aggregation may significantly increase throughput especially for small frames, but may increase latency in case of packet loss due to retransmission of aggregated frame. Sending and receiving AMSDUs will also increase CPU usage.</p></td></tr><tr><td><b>amsdu_threshold</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Max frame size to allow including in AMSDU.</p></td></tr><tr><td><b>antenna_gain</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Antenna gain in dBi, used to calculate maximum transmit power according to <strong>country</strong> regulations.</p></td></tr><tr><td><b>antenna_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              ant-a
                            </li><li>
                              ant-b
                            </li><li>
                              rxa-txb
                            </li><li>
                              txa-rxb
                            </li></ul></td><td><p>Select antenna to use for transmitting and for receiving</p><ul><li><em>ant-a</em> - use only 'a' antenna</li><li><em>ant-b</em> - use only 'b' antenna</li><li><em>txa-rxb</em> - use antenna 'a' for transmitting, antenna 'b' for receiving</li><li><em>rxa-txb</em> - use antenna 'b' for transmitting, antenna 'a' for receiving</li></ul></td></tr><tr><td><b>area</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Identifies group of wireless networks. This value is announced by AP, and can be matched in <a href="#Connect_List"> connect-list</a> by <strong>area-prefix</strong>. This is a proprietary extension.</p></td></tr><tr><td><b>arp</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li><li>
                              proxy-arp
                            </li><li>
                              reply-only
                            </li></ul></td><td><p><a href="https://wiki.mikrotik.com/wiki/Manual:IP/ARP#ARP_Modes" title="Manual:IP/ARP"><code>Read more &gt;&gt;</code></a></p></td></tr><tr><td><b>arp_timeout</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value <strong>auto</strong> equals to the value of <strong>arp-timeout</strong> in <strong>/ip settings</strong>, default is 30s</p></td></tr><tr><td><b>band</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
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
                              5ghz-n/ac
                            </li><li>
                              5ghz-onlyac
                            </li><li>
                              5ghz-onlyn
                            </li></ul></td><td><p>Defines set of used data rates, channel frequencies and widths.</p></td></tr><tr><td><b>basic_rates_ag</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              12Mbps
                            </li><li>
                              18Mbps
                            </li><li>
                              24Mbps
                            </li><li>
                              36Mbps
                            </li><li>
                              48Mbps
                            </li><li>
                              54Mbps
                            </li><li><div style="color: blue"><b>6Mbps</b>&nbsp;&larr;</div></li><li>
                              9Mbps
                            </li></ul></td><td><p>Similar to the <strong>basic-rates-b</strong> property, but used for 5ghz, 5ghz-10mhz, 5ghz-5mhz, 5ghz-turbo, 2.4ghz-b/g, 2.4ghz-onlyg, 2ghz-10mhz, 2ghz-5mhz and 2.4ghz-g-turbo bands.</p></td></tr><tr><td><b>basic_rates_b</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              11Mbps
                            </li><li><div style="color: blue"><b>1Mbps</b>&nbsp;&larr;</div></li><li>
                              2Mbps
                            </li><li>
                              5.5Mbps
                            </li></ul></td><td><p>List of basic rates, used for 2.4ghz-b, 2.4ghz-b/g and 2.4ghz-onlyg bands.</p><p>Client will connect to AP only if it supports all basic rates announced by the AP. AP will establish WDS link only if it supports all basic rates of the other AP.</p><p>This property has effect only in AP modes, and when value of <strong>rate-set</strong> is configured.</p></td></tr><tr><td><b>bridge_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li></ul></td><td><p>Allows to use station-bridge mode. <a href="https://wiki.mikrotik.com/wiki/Manual:Wireless_Station_Modes#Mode_station-bridge" title="Manual:Wireless Station Modes"><code>Read more &gt;&gt;</code></a></p></td></tr><tr><td><b>burst_time</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Time in microseconds which will be used to send data without stopping. Note that no other wireless cards in that network will be able to transmit data during burst-time microseconds. This setting is available only for AR5000, AR5001X, and AR5001X+ chipset based cards.</p></td></tr><tr><td><b>channel_width</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              10mhz
                            </li><li>
                              20/40/80/160mhz-Ceeeeeee
                            </li><li>
                              20/40/80/160mhz-XXXXXXXX
                            </li><li>
                              20/40/80/160mhz-eCeeeeee
                            </li><li>
                              20/40/80/160mhz-eeCeeeee
                            </li><li>
                              20/40/80/160mhz-eeeCeeee
                            </li><li>
                              20/40/80/160mhz-eeeeCeee
                            </li><li>
                              20/40/80/160mhz-eeeeeCee
                            </li><li>
                              20/40/80/160mhz-eeeeeeCe
                            </li><li>
                              20/40/80/160mhz-eeeeeeeC
                            </li><li>
                              20/40/80mhz-Ceee
                            </li><li>
                              20/40/80mhz-XXXX
                            </li><li>
                              20/40/80mhz-eCee
                            </li><li>
                              20/40/80mhz-eeCe
                            </li><li>
                              20/40/80mhz-eeeC
                            </li><li>
                              20/40mhz-Ce
                            </li><li>
                              20/40mhz-XX
                            </li><li>
                              20/40mhz-eC
                            </li><li><div style="color: blue"><b>20mhz</b>&nbsp;&larr;</div></li><li>
                              40mhz-turbo
                            </li><li>
                              5mhz
                            </li></ul></td><td><p>Use of extension channels (e.g. Ce, eC etc) allows additional 20MHz extension channels and if it should be located below or above the control (main) channel. Extension channel allows 802.11n devices to use up to 40MHz (802.11ac up to 160MHz) of spectrum in total thus increasing max throughput. Channel widths with XX and XXXX extensions automatically scan for a less crowded control channel frequency based on the number of concurrent devices running in every frequency and chooses the '''C''' - Control channel frequency automatically.</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Short description of the interface</p></td></tr><tr><td><b>compression</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Setting this property to <em>yes</em> will allow the use of the hardware compression. Wireless interface must have support for hardware compression. Connections with devices that do not use compression will still work.</p></td></tr><tr><td><b>country</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Limits available bands, frequencies and maximum transmit power for each frequency. Also specifies default value of <strong>scan-list</strong>. Value <em>no_country_set</em> is an FCC compliant set of channels.</p></td></tr><tr><td><b>default_ap_tx_limit</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>This is the value of <strong>ap-tx-limit</strong> for clients that do not match any entry in the <a href="#Access_List"> access-list</a>. 0 means no limit.</p></td></tr><tr><td><b>default_authentication</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>For AP mode, this is the value of <strong>authentication</strong> for clients that do not match any entry in the <a href="#Access_List"> access-list</a>. For station mode, this is the value of <strong>connect</strong> for APs that do not match any entry in the <a href="#Connect_List"> connect-list</a></p></td></tr><tr><td><b>default_client_tx_limit</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>This is the value of <strong>client-tx-limit</strong> for clients that do not match any entry in the <a href="#Access_List"> access-list</a>. 0 means no limit</p></td></tr><tr><td><b>default_forwarding</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>This is the value of <strong>forwarding</strong> for clients that do not match any entry in the <a href="#Access_List"> access-list</a></p></td></tr><tr><td><b>disable_running_check</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>When set to <strong>yes</strong> interface will always have running flag. If value is set to <strong>no'</strong>, the router determines whether the card is up and running - for AP one or more clients have to be registered to it, for station, it should be connected to an AP.</p></td></tr><tr><td><b>disabled</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>Whether interface is disabled</p></td></tr><tr><td><b>disconnect_timeout</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>This interval is measured from third sending failure on the lowest data rate. At this point 3 * (<strong>hw-retries</strong> + 1) frame transmits on the lowest data rate had failed. During <strong>disconnect-timeout</strong> packet transmission will be retried with <strong>on-fail-retry-time</strong> interval. If no frame can be transmitted successfully during <strong>disconnect-timeout</strong>, the connection is closed, and this event is logged as 'extensive data loss'. Successful frame transmission resets this timer.</p></td></tr><tr><td><b>distance</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>How long to wait for confirmation of unicast frames (<strong>ACKs</strong>) before considering transmission unsuccessful, or in short <strong>ACK-Timeout</strong>. Distance value has these behaviors:</p><ul><li><em>Dynamic</em> - causes AP to detect and use the smallest timeout that works with all connected clients.</li><li><em>Indoor</em> - uses the default ACK timeout value that the hardware chip manufacturer has set.</li><li><em>Number</em> - uses the input value in formula: ACK-timeout = ((<strong>distance</strong> * 1000) + 299) / 300 us;</li></ul><p>Acknowledgments are not used in Nstreme/NV2 protocols.</p></td></tr><tr><td><b>frame_lifetime</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Discard frames that have been queued for sending longer than <strong>frame-lifetime</strong>. By default, when value of this property is 0, frames are discarded only after connection is closed.</p></td></tr><tr><td><b>frequency</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Channel frequency value in MHz on which AP will operate.</p><p>Allowed values depend on the selected band, and are restricted by <strong>country</strong> setting and wireless card capabilities. This setting has <strong>no effect</strong> if interface is in any of <strong>station</strong> modes, or in <em>wds-slave</em> mode, or if DFS is active.</p><p><em>Note</em>: If using mode 'superchannel', any frequency supported by the card will be accepted, but on the RouterOS client, any non-standard frequency must be configured in the <a href="#scan-list"> scan-list</a>, otherwise it will not be scanning in non-standard range. In Winbox, scanlist frequencies are in <em>bold</em>, any other frequency means the clients will need scan-list configured.</p></td></tr><tr><td><b>frequency_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              manual-txpower
                            </li><li><div style="color: blue"><b>regulatory-domain</b>&nbsp;&larr;</div></li><li>
                              superchannel
                            </li></ul></td><td><p>Three frequency modes are available:</p><ul><li><em>regulatory-domain</em> - Limit available channels and maximum transmit power for each channel according to the value of <strong>country</strong></li><li><em>manual-txpower</em> - Same as above, but do not limit maximum transmit power.</li><li><em>superchannel</em> - Conformance Testing Mode. Allow all channels supported by the card.</li></ul><p>List of available channels for each band can be seen in <strong>/interface wireless info allowed-channels</strong>. This mode allows you to test wireless channels outside the default scan-list and/or regulatory domain. This mode should only be used in controlled environments, or if you have special permission to use it in your region. Before v4.3 this was called Custom Frequency Upgrade, or Superchannel. Since RouterOS v4.3 this mode is available without special key upgrades to all installations.</p></td></tr><tr><td><b>frequency_offset</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Allows to specify offset if the used wireless card operates at a different frequency than is shown in RouterOS, in case a frequency converter is used in the card. So if your card works at 4000MHz but RouterOS shows 5000MHz, set offset to 1000MHz and it will be displayed correctly. The value is in MHz and can be positive or negative.</p></td></tr><tr><td><b>guard_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>any</b>&nbsp;&larr;</div></li><li>
                              long
                            </li></ul></td><td><p>Whether to allow use of short guard interval (refer to 802.11n MCS specification to see how this may affect throughput). 'any' will use either short or long, depending on data rate, 'long' will use long.</p></td></tr><tr><td><b>hide_ssid</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><ul><li><em>yes</em> - AP does not include SSID in the beacon frames, and does not reply to probe requests that have broadcast SSID.</li><li><em>no</em> - AP includes SSID in the beacon frames, and replies to probe requests that have broadcast SSID.</li></ul><p>This property has an effect only in AP mode. Setting it to <em>yes</em> can remove this network from the list of wireless networks that are shown by some client software. Changing this setting does not improve the security of the wireless network, because SSID is included in other frames sent by the AP.</p></td></tr><tr><td><b>ht_basic_mcs</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
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
                            </li></ul></td><td><p><a href="http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates">Modulation and Coding Schemes</a> that every connecting client must support. Refer to 802.11n for MCS specification.</p></td></tr><tr><td><b>ht_supported_mcs</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
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
                            </li></ul></td><td><p><a href="http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates">Modulation and Coding Schemes</a> that this device advertises as supported. Refer to 802.11n for MCS specification.</p></td></tr><tr><td><b>hw_fragmentation_threshold</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Specifies maximum fragment size in bytes when transmitted over the wireless medium. 802.11 standard packet (MSDU in 802.11 terminologies) fragmentation allows packets to be fragmented before transmitting over a wireless medium to increase the probability of successful transmission (only fragments that did not transmit correctly are retransmitted). Note that transmission of a fragmented packet is less efficient than transmitting unfragmented packet because of protocol overhead and increased resource usage at both - transmitting and receiving party.</p></td></tr><tr><td><b>hw_protection_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              cts-to-self
                            </li><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li><li>
                              rts-cts
                            </li></ul></td><td><p>Frame protection support property <a href="#Frame_protection_support_.28RTS.2FCTS.29"><code>read more &gt;&gt;</code></a></p></td></tr><tr><td><b>hw_protection_threshold</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Frame protection support property<a href="#Frame_protection_support_.28RTS.2FCTS.29"><code>read more &gt;&gt;</code></a></p></td></tr><tr><td><b>hw_retries</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Number of times sending frame is retried without considering it a transmission failure. Data-rate is decreased upon failure and the frame is sent again. Three sequential failures on the lowest supported rate suspend transmission to this destination for the duration of <strong>on-fail-retry-time</strong>. After that, the frame is sent again. The frame is being retransmitted until transmission success, or until the client is disconnected after <strong>disconnect-timeout</strong>. The frame can be discarded during this time if <strong>frame-lifetime</strong> is exceeded.</p></td></tr><tr><td><b>installation</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>any</b>&nbsp;&larr;</div></li><li>
                              indoor
                            </li><li>
                              outdoor
                            </li></ul></td><td><p>Adjusts scan-list to use indoor, outdoor or all frequencies for the country that is set.</p></td></tr><tr><td><b>interworking_profile</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>disabled</b>&nbsp;&larr;</div></li><li>
                              enabled
                            </li></ul></td><td></td></tr><tr><td><b>keepalive_frames</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li></ul></td><td><p>Applies only if wireless interface is in mode=<strong>ap-bridge</strong>. If a client has not communicated for around 20 seconds, AP sends a 'keepalive-frame'.<br /><strong>Note</strong>, disabling the feature can lead to 'ghost' clients in registration-table.</p></td></tr><tr><td><b>l2mtu</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td></td></tr><tr><td><b>mac_address</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>master_interface</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of wireless interface that has <em>virtual-ap</em> capability. <a href="/index.php?title=Virtual_AP&amp;action=edit&amp;redlink=1" title="Virtual AP (page does not exist)">Virtual AP</a> interface will only work if master interface is in <em>ap-bridge</em>, <em>bridge</em>, <em>station</em> or <em>wds-slave</em> mode. This property is only for virtual AP interfaces.</p></td></tr><tr><td><b>max_station_count</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Maximum number of associated clients. WDS links also count toward this limit.</p></td></tr><tr><td><b>mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              alignment-only
                            </li><li>
                              ap-bridge
                            </li><li>
                              bridge
                            </li><li>
                              nstreme-dual-slave
                            </li><li><div style="color: blue"><b>station</b>&nbsp;&larr;</div></li><li>
                              station-bridge
                            </li><li>
                              station-pseudobridge
                            </li><li>
                              station-pseudobridge-clone
                            </li><li>
                              station-wds
                            </li><li>
                              wds-slave
                            </li></ul></td><td><p>Selection between different station and access point (AP) modes.</p><p><a href="https://wiki.mikrotik.com/wiki/Manual:Wireless_Station_Modes" title="Manual:Wireless Station Modes">Station modes</a>:</p><ul><li><em>station</em> - Basic station mode. Find and connect to acceptable AP.</li><li><em>station-wds</em> - Same as <em>station</em>, but create WDS link with AP, using proprietary extension. AP configuration has to allow WDS links with this device. Note that this mode does not use entries in <a href="/index.php?title=Wds&amp;action=edit&amp;redlink=1" title="Wds (page does not exist)">wds</a>.</li><li><em>station-pseudobridge</em> - Same as <em>station</em>, but additionally perform MAC address translation of all traffic. Allows interface to be bridged.</li><li><em>station-pseudobridge-clone</em> - Same as <em>station-pseudobridge</em>, but use <strong>station-bridge-clone-mac</strong> address to connect to AP.</li></ul><p>AP modes:</p><ul><li><em>ap-bridge</em> - Basic access point mode.</li><li><em>bridge</em> - Same as <em>ap-bridge</em>, but limited to one associated client.</li><li><em>wds-slave</em> - Same as <em>ap-bridge</em>, but scan for AP with the same <strong>ssid</strong> and establishes WDS link. If this link is lost or cannot be established, then continue scanning. If <strong>dfs-mode</strong> is <em>radar-detect</em>, then APs with enabled <strong>hide-ssid</strong> will not be found during scanning.</li></ul><p>Special modes:</p><ul><li><em>alignment-only</em> - Put the interface in a continuous transmit mode that is used for aiming the remote antenna.</li><li><em>nstreme-dual-slave</em> - allow this interface to be used in nstreme-dual setup.</li></ul><p>MAC address translation in <strong>pseudobridge</strong> modes works by inspecting packets and building a table of corresponding IP and MAC addresses. All packets are sent to AP with the MAC address used by pseudobridge, and MAC addresses of received packets are restored from the address translation table. There is a single entry in the address translation table for all non-IP packets, hence more than one host in the bridged network cannot reliably use non-IP protocols. Note: Currently IPv6 doesn't work over Pseudobridge</p></td></tr><tr><td><b>mtu</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td></td></tr><tr><td><b>multicast_buffering</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li></ul></td><td><p>For a client that has power saving, buffer multicast packets until next beacon time. A client should wake up to receive a beacon, by receiving beacon it sees that there are multicast packets pending, and it should wait for multicast packets to be sent.</p></td></tr><tr><td><b>multicast_helper</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>default</b>&nbsp;&larr;</div></li><li>
                              disabled
                            </li><li>
                              full
                            </li></ul></td><td><p>When set to <strong>full</strong>, multicast packets will be sent with a unicast destination MAC address, resolving <a href="https://wiki.mikrotik.com/wiki/Manual:Multicast_detailed_example#Multicast_and_Wireless" title="Manual:Multicast detailed example"> multicast problem</a> on the wireless link. This option should be enabled only on the access point, clients should be configured in <strong>station-bridge</strong> mode. Available starting from v5.15.</p><ul><li>disabled - disables the helper and sends multicast packets with multicast destination MAC addresses</li><li>full - all multicast packet mac address are changed to unicast mac addresses prior sending them out</li><li>default - default choice that currently is set to <em>disabled</em>. Value can be changed in future releases.</li></ul></td></tr><tr><td><b>name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>name of the interface</p></td></tr><tr><td><b>noise_floor_threshold</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>For advanced use only, as it can badly affect the performance of the interface. It is possible to manually set noise floor threshold value. By default, it is dynamically calculated. This property also affects received signal strength. This property is only effective on non-AC chips.</p></td></tr><tr><td><b>nv2_cell_radius</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Setting affects the size of contention time slot that AP allocates for clients to initiate connection and also size of time slots used for estimating distance to client. When setting is too small, clients that are farther away may have trouble connecting and/or disconnect with 'ranging timeout' error. Although during normal operation the effect of this setting should be negligible, in order to maintain maximum performance, it is advised to not increase this setting if not necessary, so AP is not reserving time that is actually never used, but instead allocates it for actual data transfer.</p><ul><li>on AP: distance to farthest client in km</li><li>on station: no effect</li></ul></td></tr><tr><td><b>nv2_noise_floor_offset</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>nv2_preshared_key</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>nv2_qos</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>default</b>&nbsp;&larr;</div></li><li>
                              frame-priority
                            </li></ul></td><td><p>Sets the packet priority mechanism, firstly data from high priority queue is sent, then lower queue priority data until 0 queue priority is reached. When link is full with high priority queue data, lower priority data is not sent. Use it very carefully, setting works on AP</p><ul><li><strong>frame-priority</strong> - manual setting that can be tuned with Mangle rules.</li><li><strong>default</strong> - default setting where small packets receive priority for best latency</li></ul></td></tr><tr><td><b>nv2_queue_count</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td></td></tr><tr><td><b>nv2_security</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>disabled</b>&nbsp;&larr;</div></li><li>
                              enabled
                            </li></ul></td><td></td></tr><tr><td><b>on_fail_retry_time</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>After third sending failure on the lowest data rate, wait for specified time interval before retrying.</p></td></tr><tr><td><b>periodic_calibration</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>default</b>&nbsp;&larr;</div></li><li>
                              disabled
                            </li><li>
                              enabled
                            </li></ul></td><td><p>Setting <em>default</em> enables periodic calibration if <a href="#Info"> info</a><strong>default-periodic-calibration</strong> property is <em>enabled</em>. Value of that property depends on the type of wireless card. This property is only effective for cards based on Atheros chipset.</p></td></tr><tr><td><b>periodic_calibration_interval</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>This property is only effective for cards based on Atheros chipset.</p></td></tr><tr><td><b>preamble_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>both</b>&nbsp;&larr;</div></li><li>
                              long
                            </li><li>
                              short
                            </li></ul></td><td><p>Short preamble mode is an option of 802.11b standard that reduces per-frame overhead.</p><ul><li>On AP:
<ul><li><em>long</em> - Do not use short preamble.</li><li><em>short</em> - Announce short preamble capability. Do not accept connections from clients that do not have this capability.</li><li><em>both</em> - Announce short preamble capability.</li></ul></li><li>On station:
<ul><li><em>long</em> - do not use short preamble.</li><li><em>short</em> - do not connect to AP if it does not support short preamble.</li><li><em>both</em> - Use short preamble if AP supports it.</li></ul></li></ul></td></tr><tr><td><b>prism_cardtype</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              100mW
                            </li><li>
                              200mW
                            </li><li>
                              30mW
                            </li></ul></td><td><p>Specify type of the installed Prism wireless card.</p></td></tr><tr><td><b>proprietary_extensions</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>post-2.9.25</b>&nbsp;&larr;</div></li><li>
                              pre-2.9.25
                            </li></ul></td><td><p>RouterOS includes proprietary information in an information element of management frames. This parameter controls how this information is included.</p><ul><li><em>pre-2.9.25</em> - This is older method. It can interoperate with newer versions of RouterOS. This method is incompatible with some clients, for example, Centrino based ones.</li><li><em>post-2.9.25</em> - This uses standardized way of including vendor specific information, that is compatible with newer wireless clients.</li></ul></td></tr><tr><td><b>radio_name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Descriptive name of the device, that is shown in registration table entries on the remote devices. This is a proprietary extension.</p></td></tr><tr><td><b>rate_selection</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>advanced</b>&nbsp;&larr;</div></li><li>
                              legacy
                            </li></ul></td><td><p>Starting from v5.9 default value is advanced since legacy mode was inefficient.</p></td></tr><tr><td><b>rate_set</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              configured
                            </li><li><div style="color: blue"><b>default</b>&nbsp;&larr;</div></li></ul></td><td><p>Two options are available:</p><ul><li><em>default</em> - default basic and supported rate sets are used. Values from <strong>basic-rates</strong> and <strong>supported-rates</strong> parameters have no effect.</li><li><em>configured</em> - use values from <strong>basic-rates</strong>, <strong>supported-rates</strong>, <strong>basic-mcs</strong>, <strong>mcs</strong>. <a href="#Basic_and_MCS_Rate_table"><code>Read more &gt;&gt;</code></a>.</li></ul></td></tr><tr><td><b>rx_chains</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              0
                            </li><li>
                              1
                            </li><li>
                              2
                            </li><li>
                              3
                            </li></ul></td><td><p>Which antennas to use for receive. In current MikroTik routers, both RX and TX chain must be enabled, for the chain to be enabled.</p></td></tr><tr><td><b>scan_list</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td></td><td><p>The <em>default</em> value is all channels from selected band that are supported by card and allowed by the <strong>country</strong> and <strong>frequency-mode</strong> settings (this list can be seen in <a href="#Info"> info</a>). For default scan list in <em>5ghz</em> band channels are taken with 20MHz step, in <em>5ghz-turbo</em> band - with 40MHz step, for all other bands - with 5MHz step. If <strong>scan-list</strong> is specified manually, then all matching channels are taken. (Example: <strong>scan-list</strong>=<em>default,5200-5245,2412-2427</em> - This will use the default value of scan list for current band, and add to it supported frequencies from 5200-5245 or 2412-2427 range.)</p><p>Since RouterOS v6.0 with Winbox or Webfig, for inputting of multiple frequencies, add each frequency or range of frequencies into separate multiple scan-lists. Using a comma to separate frequencies is no longer supported in Winbox/Webfig since v6.0.</p><p>Since RouterOS v6.35 (wireless-rep) scan-list support step feature where it is possible to manually specify the scan step. Example: <strong>scan-list</strong>=<em>5500-5600:20</em> will generate such scan-list values <em>5500,5520,5540,5560,5580,5600</em></p></td></tr><tr><td><b>secondary_channel</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Specifies secondary channel, required to enable 80+80MHz transmission. To disable 80+80MHz functionality, set secondary-channel to '' or unset the value via CLI/GUI.</p></td></tr><tr><td><b>security_profile</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of profile from <a href="#Security_Profiles"> security-profiles</a></p></td></tr><tr><td><b>skip_dfs_channels</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>These values are used to skip all DFS channels or specifically skip DFS CAC channels in range 5600-5650MHz which detection could go up to 10min.</p></td></tr><tr><td><b>ssid</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>SSID (service set identifier) is a name that identifies wireless network.</p></td></tr><tr><td><b>station_bridge_clone_mac</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>This property has effect only in the <em>station-pseudobridge-clone</em> mode.</p><p>Use this MAC address when connection to AP. If this value is <em>00:00:00:00:00:00</em>, station will initially use MAC address of the wireless interface.</p><p>As soon as packet with MAC address of another device needs to be transmitted, station will reconnect to AP using that address.</p></td></tr><tr><td><b>station_roaming</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>disabled</b>&nbsp;&larr;</div></li><li>
                              enabled
                            </li></ul></td><td><p>Station Roaming feature is available only for 802.11 wireless protocol and only for station modes. <a href="#Station-Roaming"><code>Read more &gt;&gt;</code></a></p></td></tr><tr><td><b>supported_rates_ag</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              12Mbps
                            </li><li>
                              18Mbps
                            </li><li>
                              24Mbps
                            </li><li>
                              36Mbps
                            </li><li>
                              48Mbps
                            </li><li>
                              54Mbps
                            </li><li>
                              6Mbps
                            </li><li>
                              9Mbps
                            </li></ul></td><td><p>List of supported rates, used for all bands except <em>2ghz-b</em>.</p></td></tr><tr><td><b>supported_rates_b</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              11Mbps
                            </li><li>
                              1Mbps
                            </li><li>
                              2Mbps
                            </li><li>
                              5.5Mbps
                            </li></ul></td><td><p>List of supported rates, used for <em>2ghz-b</em>, <em>2ghz-b/g</em> and <em>2ghz-b/g/n</em> bands. Two devices will communicate only using rates that are supported by both devices. This property has effect only when value of <strong>rate-set</strong> is <em>configured</em>.</p></td></tr><tr><td><b>tdma_period_size</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Specifies TDMA period in milliseconds. It could help on the longer distance links, it could slightly increase bandwidth, while latency is increased too.</p></td></tr><tr><td><b>tx_chains</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              0
                            </li><li>
                              1
                            </li><li>
                              2
                            </li><li>
                              3
                            </li></ul></td><td><p>Which antennas to use for transmitting. In current MikroTik routers, both RX and TX chain must be enabled, for the chain to be enabled.</p></td></tr><tr><td><b>tx_power</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>For 802.11ac wireless interface it's total power but for 802.11a/b/g/n it's power per chain.</p></td></tr><tr><td><b>tx_power_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              all-rates-fixed
                            </li><li>
                              card-rates
                            </li><li><div style="color: blue"><b>default</b>&nbsp;&larr;</div></li><li>
                              manual-table
                            </li></ul></td><td><p>sets up tx-power mode for wireless card</p><ul><li>default - use values stored in the card</li><li>all-rates-fixed - use same transmit power for all data rates. Can damage the card if transmit power is set above rated value of the card for used rate.</li><li>manual-table - define transmit power for each rate separately. Can damage the card if transmit power is set above rated value of the card for used rate.</li><li>card-rates - use transmit power calculated for each rate based on value of <strong>tx-power</strong> parameter. Legacy mode only compatible with currently discontinued products.</li></ul></td></tr><tr><td><b>update_stats_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>How often to request update of signals strength and ccq values from clients.</p><p>Access to <a href="#Registration_Table"> registration-table</a> also triggers update of these values.</p><p>This is proprietary extension.</p></td></tr><tr><td><b>vht_basic_mcs</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>MCS 0-7</b>&nbsp;&larr;</div></li><li>
                              MCS 0-8
                            </li><li>
                              MCS 0-9
                            </li><li>
                              none
                            </li></ul></td><td><p><a href="http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed">Modulation and Coding Schemes</a> that every connecting client must support. Refer to 802.11ac for MCS specification. You can set MCS interval for each of Spatial Stream</p><ul><li><em>none</em> - will not use selected Spatial Stream</li><li><em>MCS 0-7</em> - client must support MCS-0 to MCS-7</li><li><em>MCS 0-8</em> - client must support MCS-0 to MCS-8</li><li><em>MCS 0-9</em> - client must support MCS-0 to MCS-9</li></ul></td></tr><tr><td><b>vht_supported_mcs</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              MCS 0-7
                            </li><li>
                              MCS 0-8
                            </li><li><div style="color: blue"><b>MCS 0-9</b>&nbsp;&larr;</div></li><li>
                              none
                            </li></ul></td><td><p><a href="http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed">Modulation and Coding Schemes</a> that this device advertises as supported. Refer to 802.11ac for MCS specification. You can set MCS interval for each of Spatial Stream</p><ul><li><em>none</em> - will not use selected Spatial Stream</li><li><em>MCS 0-7</em> - devices will advertise as supported MCS-0 to MCS-7</li><li><em>MCS 0-8</em> - devices will advertise as supported MCS-0 to MCS-8</li><li><em>MCS 0-9</em> - devices will advertise as supported MCS-0 to MCS-9</li></ul></td></tr><tr><td><b>wds_cost_range</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Bridge port cost of WDS links are automatically adjusted, depending on measured link throughput. Port cost is recalculated and adjusted every 5 seconds if it has changed by more than 10%, or if more than 20 seconds have passed since the last adjustment.</p><p>Setting this property to 0 disables automatic cost adjustment.</p><p>Automatic adjustment does not work for WDS links that are manually configured as a bridge port.</p></td></tr><tr><td><b>wds_default_bridge</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>When WDS link is established and status of the wds interface becomes <em>running</em>, it will be added as a bridge port to the bridge interface specified by this property. When WDS link is lost, wds interface is removed from the bridge. If wds interface is already included in a bridge setup when WDS link becomes active, it will not be added to bridge specified by , and will (needs editing)</p></td></tr><tr><td><b>wds_default_cost</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Initial bridge port cost of the WDS links.</p></td></tr><tr><td><b>wds_ignore_ssid</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>By default, WDS link between two APs can be created only when they work on the same frequency and have the same SSID value. If this property is set to <em>yes</em>, then SSID of the remote AP will not be checked. This property has no effect on connections from clients in <em>station-wds</em> mode. It also does not work if <strong>wds-mode</strong> is <em>static-mesh</em> or <em>dynamic-mesh</em>.</p></td></tr><tr><td><b>wds_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>disabled</b>&nbsp;&larr;</div></li><li>
                              dynamic
                            </li><li>
                              dynamic-mesh
                            </li><li>
                              static
                            </li><li>
                              static-mesh
                            </li></ul></td><td><p>Controls how WDS links with other devices (APs and clients in <em>station-wds</em> mode) are established.</p><ul><li><em>disabled</em> does not allow WDS links.</li><li><em>static</em> only allows WDS links that are manually configured in <a href="/index.php?title=Wds&amp;action=edit&amp;redlink=1" title="Wds (page does not exist)">wds</a></li><li><em>dynamic</em> also allows WDS links with devices that are not configured in <a href="/index.php?title=Wds&amp;action=edit&amp;redlink=1" title="Wds (page does not exist)">wds</a>, by creating required entries dynamically. Such dynamic WDS entries are removed automatically after the connection with the other AP is lost.</li></ul><p><em>-mesh</em> modes use different (better) method for establishing link between AP, that is not compatible with APs in non-mesh mode. This method avoids one-sided WDS links that are created only by one of the two APs. Such links cannot pass any data.When AP or station is establishing WDS connection with another AP, it uses <a href="#Connect_List"> connect-list</a> to check whether this connection is allowed. If station in <em>station-wds</em> mode is establishing connection with AP, AP uses <a href="#Access_List"> access-list</a> to check whether this connection is allowed.If <strong>mode</strong> is <em>station-wds</em>, then this property has no effect.</p></td></tr><tr><td><b>wireless_protocol</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              802.11
                            </li><li><div style="color: blue"><b>any</b>&nbsp;&larr;</div></li><li>
                              nstreme
                            </li><li>
                              nv2
                            </li><li>
                              nv2-nstreme
                            </li><li>
                              nv2-nstreme-802.11
                            </li><li>
                              unspecified
                            </li></ul></td><td><p>Specifies protocol used on wireless interface;</p><ul><li><em>unspecified</em> - protocol mode used on previous RouterOS versions (v3.x, v4.x). Nstreme is enabled by old enable-nstreme setting, Nv2 configuration is not possible.</li><li><em>any</em> : on AP - regular 802.11 Access Point or Nstreme Access Point; on station - selects Access Point without specific sequence, it could be changed by connect-list rules.</li><li><em>nstreme</em> - enables Nstreme protocol (the same as old enable-nstreme setting).</li><li><em>nv2</em> - enables Nv2 protocol.</li><li><em>nv2 nstreme</em> : on AP - uses first wireless-protocol setting, always Nv2; on station - searches for Nv2 Access Point, then for Nstreme Access Point.</li><li><em>nv2 nstreme 802.11</em> - on AP - uses first wireless-protocol setting, always Nv2; on station - searches for Nv2 Access Point, then for Nstreme Access Point, then for regular 802.11 Access Point.</li></ul><p><strong>Warning!</strong> Nv2 doesn't have support for Virtual AP</p></td></tr><tr><td><b>wmm_support</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>disabled</b>&nbsp;&larr;</div></li><li>
                              enabled
                            </li><li>
                              required
                            </li></ul></td><td><p>Specifies whether to enable <a href="https://wiki.mikrotik.com/wiki/Manual:WMM" title="Manual:WMM"> WMM</a>.</p></td></tr><tr><td><b>wps_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li>
                              push-button
                            </li><li>
                              push-button-virtual-only
                            </li></ul></td><td><p><a href="#WPS_Server"><code>Read more &gt;&gt;</code></a></p></td></tr></table>

========
Examples
========

------------------
Using merged state
------------------

**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface wireless export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface wireless
    set [ find default-name=wlan1 ] comment="wlan1 comment" security-profile=to-olympus

**Configuration**

.. code-block:: yaml+jinja

    - name: Merge device configuration
      kilip.routeros.kilip.routeros.ros_wireless:
        config:
          - name: wlan1
            comment: 'updated comment'
            ampdu_priorities:
              - 0
              - 1
              - 2
            supported_rates_ag:
              - 6Mbps
              - 24Mbps
        state: merged

**Executed Command**

.. code-block:: ssh

    /interface wireless set [ find name=wlan1 ] ampdu-priorities=0,1,2 comment="updated comment" security-profile=default supported-rates-a/g=6Mbps,24Mbps

**After State**

.. code-block:: ssh

    [admin@MikroTik] > /interface wireless export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface wireless
    set [ find default-name=wlan1 ] ampdu-priorities=0,1,2 comment="updated comment" security-profile=default supported-rates-a/g=6Mbps,24Mbps

--------------------
Using replaced state
--------------------

**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface wireless export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface wireless
    set [ find default-name=wlan1 ] comment="wlan1 comment" security-profile=to-olympus

**Configuration**

.. code-block:: yaml+jinja

    - name: Replace device wireless configuration
      kilip.routeros.kilip.routeros.ros_wireless:
        config:
          - name: wlan1
            comment: 'new olympus'
            ssid: Olympus
            security_profile: new-olympus
        state: replaced

**Executed Command**

.. code-block:: ssh

    /interface wireless set [ find name=wlan1 ] comment="new olympus" security-profile=new-olympus ssid=Olympus

**After State**

.. code-block:: ssh

    [admin@MikroTik] > /interface wireless export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface wireless
    set [ find default-name=wlan1 ] comment="new olympus" ssid=Olympus security-profile=new-olympus
