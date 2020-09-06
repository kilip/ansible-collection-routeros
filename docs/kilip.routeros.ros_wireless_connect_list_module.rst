.. _kilip.routeros.ros_wireless_connect_list_module

********************************
kilip.routeros.ros_wireless_connect_list
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface wireless connect-list**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This module manages the Wireless Access List configuration of Mikrotik RouterOS network devices.



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
  A dictionary for `/interface wireless connect-list` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>area_prefix</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Rule matches if area value of AP (a proprietary extension) begins with specified value.<strong>area</strong> value is a proprietary extension.</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Short description of an entry</p></td></tr><tr><td><b>connect</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>Available options:</p><ul><li><em>yes</em> - Connect to access point that matches this rule.</li><li><em>no</em> - Do not connect to any access point that matches this rule.</li></ul></td></tr><tr><td><b>disabled</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td></td></tr><tr><td><b>interface</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Each rule in connect list applies only to one wireless interface that is specified by this setting.</p></td></tr><tr><td><b>mac_address</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Rule matches only AP with the specified MAC address. Value <em>00:00:00:00:00:00</em> matches always.</p></td></tr><tr><td><b>security_profile</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of <a href="#Security_Profiles"> security profile</a> that is used when connecting to matching access points, If value of this property is <em>none</em>, then security profile specified in the interface configuration will be used. In station mode, rule will match only access points that can support specified security profile. Value <em>none</em> will match access point that supports security profile that is specified in the interface configuration. In access point mode value of this property will not be used to match remote devices.</p></td></tr><tr><td><b>signal_range</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Rule matches if signal strength of the access point is within the range. If station establishes connection to access point that is matched by this rule, it will disconnect from that access point when signal strength goes out of the specified range.</p></td></tr><tr><td><b>ssid</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Rule matches access points that have this SSID. Empty value matches any SSID. This property has effect only when station mode interface <strong>ssid</strong> is empty, or when access point mode interface has <strong>wds-ignore-ssid</strong>=<em>yes</em></p></td></tr><tr><td><b>wireless_protocol</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              802.11
                            </li><li><div style="color: blue"><b>any</b>&nbsp;&larr;</div></li><li>
                              nstreme
                            </li><li>
                              tdma
                            </li></ul></td><td></td></tr></table>



========
Examples
========




------------------
Using merged state
------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface wireless connect-list export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface wireless connect-list
    add comment=existing interfce=wlan1 signal-range=-79..120



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge device configuration
      kilip.routeros.ros_wireless_connect_list:
        config:
          - comment: existing
            interface: wlan1
            signal_range: '-50..120'
            wireless_protocol: 802.11
        state: merged
        
      

**Executed Command**


.. code-block:: ssh

    /interface wireless connect-list set [ find comment=existing ] interface=wlan1 signal-range=-50..120 wireless-protocol=802.11


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface wireless connect-list export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface wireless connect-list
    add comment=existing interfce=wlan1 signal-range=-50..120


