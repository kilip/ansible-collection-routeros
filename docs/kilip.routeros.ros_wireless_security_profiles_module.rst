.. _kilip.routeros.ros_wireless_security_profiles_module

********************************
kilip.routeros.ros_wireless_security_profiles
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface wireless security-profiles**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This module manages the Wireless Security Profiles of Mikrotik RouterOS network devices.



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
  A dictionary for `/interface wireless security-profiles` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>authentication_types</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              wpa-eap
                            </li><li>
                              wpa-psk
                            </li><li>
                              wpa2-eap
                            </li><li>
                              wpa2-psk
                            </li></ul></td><td><p>Set of supported authentication types, multiple values can be selected. Access Point will advertise supported authentication types, and client will connect to Access Point only if it supports any of the advertised authentication types.</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Give notes for this resource</p></td></tr><tr><td><b>disable_pmkid</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Whether to include PMKID into the EAPOL frame sent out by the Access Point. Disabling PMKID can cause compatibility issues with devices that use the PMKID to connect to an Access Point.</p><ul><li>yes - removes PMKID from EAPOL frames (improves security, reduces compatibility).</li><li>no - includes PMKID into EAPOL frames (reduces security, improves compatibility).</li></ul><p>This property only has effect on Access Points.</p></td></tr><tr><td><b>eap_methods</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              eap-tls
                            </li><li>
                              eap-ttls-mschapv2
                            </li><li><div style="color: blue"><b>passthrough</b>&nbsp;&larr;</div></li><li>
                              peap
                            </li></ul></td><td><p>Allowed types of authentication methods, multiple values can be selected. This property only has effect on Access Points.</p><ul><li>eap-tls - Use built-in EAP TLS authentication. Both client and server certificates are supported. See description of <strong>tls-mode</strong> and <strong>tls-certificate</strong> properties.</li><li>eap-ttls-mschapv2 - Use EAP-TTLS with MS-CHAPv2 authentication.</li><li>passthrough - Access Point will relay authentication process to the RADIUS server.</li><li>peap - Use Protected EAP authentication.</li></ul></td></tr><tr><td><b>group_ciphers</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>aes-ccm</b>&nbsp;&larr;</div></li><li>
                              tkip
                            </li></ul></td><td><p>Access Point advertises one of these ciphers, multiple values can be selected. Access Point uses it to encrypt all broadcast and multicast frames. Client attempts connection only to Access Points that use one of the specified group ciphers.</p><ul><li>tkip - Temporal Key Integrity Protocol - encryption protocol, compatible with legacy WEP equipment, but enhanced to correct some of the WEP flaws.</li><li>aes-ccm - more secure WPA encryption protocol, based on the reliable AES (Advanced Encryption Standard). Networks free of WEP legacy should use only this cipher.</li></ul></td></tr><tr><td><b>group_key_update</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Controls how often Access Point updates the group key. This key is used to encrypt all broadcast and multicast frames. property only has effect for Access Points.</p></td></tr><tr><td><b>interim_update</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>When RADIUS accounting is used, Access Point periodically sends accounting information updates to the RADIUS server. This property specifies default update interval that can be overridden by the RADIUS server using <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#RADIUS_MAC_authentication" title="Manual:Interface/Wireless"> Acct-Interim-Interval</a> attribute.</p></td></tr><tr><td><b>mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              dynamic-keys
                            </li><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li><li>
                              static-keys-optional
                            </li><li>
                              static-keys-required
                            </li></ul></td><td><p>Encryption mode for the security profile.</p><ul><li>none - Encryption is not used. Encrypted frames are not accepted.</li><li>static-keys-required - WEP mode. Do not accept and do not send unencrypted frames. Station in <em>static-keys-required</em> mode will not connect to an Access Point in <em>static-keys-optional</em> mode.</li><li>static-keys-optional - WEP mode. Support encryption and decryption, but allow also to receive and send unencrypted frames. Device will send unencrypted frames if encryption algorithm is specified as <em>none</em>. Station in <em>static-keys-optional</em> mode will not connect to an Access Point in <em>static-keys-required</em> mode. See also: <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#WEP_properties" title="Manual:Interface/Wireless"> static-sta-private-algo</a>, <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#WEP_properties" title="Manual:Interface/Wireless"> static-transmit-key</a>.</li><li>dynamic-keys - WPA mode.</li></ul></td></tr><tr><td><b>mschapv2_password</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Password to use for authentication when <em>eap-ttls-mschapv2</em> authentication method is being used. This property only has effect on Stations.</p></td></tr><tr><td><b>mschapv2_username</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Username to use for authentication when <em>eap-ttls-mschapv2</em> authentication method is being used. This property only has effect on Stations.</p></td></tr><tr><td><b>name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of the security profile</p></td></tr><tr><td><b>radius_called_format</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              mac
                            </li><li><div style="color: blue"><b>mac:ssid</b>&nbsp;&larr;</div></li><li>
                              ssid
                            </li></ul></td><td><p>Format of how the 'called-id' identifier will be passed to RADIUS. When configuring radius server clients, you can specify 'called-id' in order to separate multiple entires.</p></td></tr><tr><td><b>radius_eap_accounting</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Explicitly enable accouting packets for radius-eap authentication</p></td></tr><tr><td><b>radius_mac_accounting</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Explicitly enable accouting packets for radius-mac authentication</p></td></tr><tr><td><b>radius_mac_authentication</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>This property affects the way how Access Point processes clients that are not found in the <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#Access_List" title="Manual:Interface/Wireless"> Access List</a>.</p><ul><li>no - allow or reject client authentication based on the value of <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#General_interface_properties" title="Manual:Interface/Wireless"> default-authentication</a> property of the Wireless interface.</li><li>yes - Query RADIUS server using MAC address of client as user name. With this setting the value of <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#General_interface_properties" title="Manual:Interface/Wireless"> default-authentication</a> has no effect.</li></ul></td></tr><tr><td><b>radius_mac_caching</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>disabled</b>&nbsp;&larr;</div></li><li>
                              time
                            </li></ul></td><td><p>If this value is set to time interval, the Access Point will cache RADIUS MAC authentication responses for specified time, and will not contact RADIUS server if matching cache entry already exists. Value <em>disabled</em> will disable cache, Access Point will always contact RADIUS server.</p></td></tr><tr><td><b>radius_mac_format</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              XX XX XX XX XX XX
                            </li><li>
                              XX-XX-XX-XX-XX-XX
                            </li><li><div style="color: blue"><b>XX:XX:XX:XX:XX:XX</b>&nbsp;&larr;</div></li><li>
                              XXXX:XXXX:XXXX
                            </li><li>
                              XXXXXX-XXXXXX
                            </li><li>
                              XXXXXX:XXXXXX
                            </li><li>
                              XXXXXXXXXXXX
                            </li></ul></td><td><p>Controls how MAC address of the client is encoded by Access Point in the User-Name attribute of the MAC authentication and MAC accounting RADIUS requests.</p></td></tr><tr><td><b>radius_mac_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>as-username</b>&nbsp;&larr;</div></li><li>
                              as-username-and-password
                            </li></ul></td><td><p>By default Access Point uses an empty password, when sending Access-Request during MAC authentication. When this property is set to <em>as-username-and-password</em>, Access Point will use the same value for User-Password attribute as for the User-Name attribute.</p></td></tr><tr><td><b>supplicant_identity</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>EAP identity that is sent by client at the beginning of EAP authentication. This value is used as a value for User-Name attribute in RADIUS messages sent by RADIUS EAP accounting and RADIUS EAP pass-through authentication.</p></td></tr><tr><td><b>tls_certificate</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              name
                            </li><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li></ul></td><td><p>Access Point always needs a certificate when configured when <strong>tls-mode</strong> is set to <em>verify-certificate</em>, or is set to <em>dont-verify-certificate</em>. Client needs a certificate only if Access Point is configured with <strong>tls-mode</strong> set to <em>verify-certificate</em>. In this case client needs a valid certificate that is signed by a CA known to the Access Point. This property only has effect when <strong>tls-mode</strong> is not set to <em>no-certificates</em> and <strong>eap-methods</strong> contains <em>eap-tls</em>.</p></td></tr><tr><td><b>tls_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              dont-verify-certificate
                            </li><li><div style="color: blue"><b>no-certificates</b>&nbsp;&larr;</div></li><li>
                              verify-certificate
                            </li><li>
                              verify-certificate-with-crl
                            </li></ul></td><td><p>This property has effect only when <strong>eap-methods</strong> contains <em>eap-tls</em>.</p><ul><li>verify-certificate - Require remote device to have valid certificate. Check that it is signed by known certificate authority. No additional identity verification is done. Certificate may include information about time period during which it is valid. If router has incorrect time and date, it may reject valid certificate because router's clock is outside that period. See also the <a href="https://wiki.mikrotik.com/wiki/Manual:System/Certificates" title="Manual:System/Certificates"> Certificates</a> configuration.</li><li>dont-verify-certificate - Do not check certificate of the remote device. Access Point will not require client to provide certificate.</li><li>no-certificates - Do not use certificates. TLS session is established using 2048 bit anonymous Diffie-Hellman key exchange.</li><li>verify-certificate-with-crl - Same as <em>verify-certificate</em> but also checks if the certificate is valid by checking the Certificate Revocation List.</li></ul></td></tr><tr><td><b>unicast_ciphers</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>aes-ccm</b>&nbsp;&larr;</div></li><li>
                              tkip
                            </li></ul></td><td><p>Access Point advertises that it supports specified ciphers, multiple values can be selected. Client attempts connection only to Access Points that supports at least one of the specified ciphers. One of the ciphers will be used to encrypt unicast frames that are sent between Access Point and Station.</p></td></tr><tr><td><b>wpa2_pre_shared_key</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>WPA2 pre-shared key mode requires all devices in a BSS to have common secret key. Value of this key can be an arbitrary text. Commonly referred to as the network password for WPA2 mode. property only has effect when <em>wpa2-psk</em> is added to <strong>authentication-types</strong>.</p></td></tr><tr><td><b>wpa_pre_shared_key</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>WPA pre-shared key mode requires all devices in a BSS to have common secret key. Value of this key can be an arbitrary text. Commonly referred to as the network password for WPA mode. property only has effect when <em>wpa-psk</em> is added to <strong>authentication-types</strong>.</p></td></tr></table>



========
Examples
========




------------------
Using merged state
------------------


**Before State**

.. code-block:: ssh

    /interface wireless security-profiles
    add name=test supplicant-identity=MikroTik
    



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge with device configuration
      kilip.routeros.ros_wireless_security_profiles:
        config:
          - name: test
            supplicant_identity: test
          - name: new
            supplicant_identity: new
        
      

**Executed Command**


.. code-block:: ssh

    /interface wireless security-profiles set [ find name=test ] supplicant-identity=test
    /interface wireless security-profiles add name=new supplicant-identity=new


**After State**


.. code-block:: ssh

    /interface wireless security-profiles
    add name=test supplicant-identity=test
    add name=foo supplicant-identity=foo
    


