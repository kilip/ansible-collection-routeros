.. _kilip.routeros.ros_capsman_aaa_module

********************************
kilip.routeros.ros_capsman_aaa
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/caps-man aaa**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This modules manages CAPsMan AAA configuration on Mikrotik RouterOS network devices



==========
Parameters
==========


state
  | **choices**: present, reset
  | **default**: present
  | **required**: False
  | **type**: str
  Available state for this module

config
  | **type**: list
  | **elements**: dict
  A dictionary for `/caps-man aaa` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>called_format</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              mac
                            </li><li><div style="color: blue"><b>mac:ssid</b>&nbsp;&larr;</div></li><li>
                              ssid
                            </li></ul></td><td><p>Format of how the 'called-id' identifier will be passed to RADIUS. When configuring radius server clients, you can specify 'called-id' in order to separate multiple entires.</p></td></tr><tr><td><b>interim_update</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>When RADIUS accounting is used, Access Point periodically sends accounting information updates to the RADIUS server. This property specifies default update interval that can be overridden by the RADIUS server using the <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#RADIUS_MAC_authentication" title="Manual:Interface/Wireless"> Acct-Interim-Interval</a> attribute.</p></td></tr><tr><td><b>mac_caching</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>If this value is set to time interval, the Access Point will cache RADIUS MAC authentication responses for specified time, and will not contact RADIUS server if matching cache entry already exists. Value disabled will disable cache, Access Point will always contact RADIUS server.</p></td></tr><tr><td><b>mac_format</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Controls how MAC address of the client is encoded by Access Point in the User-Name attribute of the MAC authentication and MAC accounting RADIUS requests.</p></td></tr><tr><td><b>mac_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              as-username
                            </li><li>
                              as-username-and-password
                            </li></ul></td><td><p>By default Access Point uses an empty password, when sending Access-Request during MAC authentication. When this property is set to as-username-and-password, Access Point will use the same value for User-Password attribute as for the User-Name attribute.</p></td></tr></table>



========
Examples
========




-------------------
Using present state
-------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /caps-man aaa export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man aaa
    set called-format=mac:ssid interim-update=disabled mac-caching=disabled mac-format=XX.XX.XX.XX.XX.XX mac-mode=as-username



**Configuration**


.. code-block:: yaml+jinja

    - name: Change configuration
      kilip.routeros.ros_capsman_aaa:
        config:
          called_format: mac
          interim_update: 10s
          mac_caching: 10m
          mac_format: XX-XX-XX-XX-XX-XX
          mac_mode: as-username-and-password
        state: present
        
      

**Executed Command**


.. code-block:: ssh

    /caps-man aaa set called-format=mac interim-update=10s mac-caching=10m mac-format=XX-XX-XX-XX-XX-XX mac-mode=as-username-and-password


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /caps-man aaa export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man aaa
    set called-format=mac interim-update=10s mac-caching=10m mac-format=XX-XX-XX-XX-XX-XX mac-mode=as-username-and-password




-----------------
Using reset state
-----------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /caps-man aaa export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man aaa
    set called-format=mac:ssid interim-update=disabled mac-caching=disabled mac-format=XX.XX.XX.XX.XX.XX mac-mode=as-username



**Configuration**


.. code-block:: yaml+jinja

    - name: Reset to default value
      kilip.routeros.ros_capsman_aaa:
        state: reset
        
      

**Executed Command**


.. code-block:: ssh

    /caps-man aaa set mac-format=XX:XX:XX:XX:XX:XX


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /caps-man aaa export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man aaa
    set called-format=mac:ssid interim-update=disabled mac-caching=disabled mac-format=XX:XX:XX:XX:XX:XX mac-mode=as-username


