.. _kilip.routeros.ros_wireless_access_list_module

********************************
kilip.routeros.ros_wireless_access_list
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface wireless access-list**

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
  A dictionary for `/interface wireless access-list` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>ap_tx_limit</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Limit rate of data transmission to this client. Value 0 means no limit. Value is in bits per second.</p></td></tr><tr><td><b>authentication</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><ul><li><em>no</em> - Client association will always fail.</li><li><em>yes</em> - Use authentication procedure that is specified in the <a href="#Security_Profiles"><strong>security-profile</strong></a> of the interface.</li></ul></td></tr><tr><td><b>client_tx_limit</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Ask client to limit rate of data transmission. Value 0 means no limit.</p><p>This is a proprietary extension that is supported by RouterOS clients.</p><p>Value is in bits per second.</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Short description of an entry</p></td></tr><tr><td><b>disabled</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td></td></tr><tr><td><b>forwarding</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><ul><li><em>no</em> - Client cannot send frames to other station that are connected to same access point.</li><li><em>yes</em> - Client can send frames to other stations on the same access point.</li></ul></td></tr><tr><td><b>interface</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Rules with <strong>interface</strong>=<em>any</em> are used for any wireless interface and the <strong>interface</strong>=<em>all</em> defines <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/List#Lists" title="Manual:Interface/List">interface-list</a> '''all''' name. To make rule that applies only to one wireless interface, specify that interface as a value of this property.</p></td></tr><tr><td><b>mac_address</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Rule matches client with the specified MAC address. Value <em>00:00:00:00:00:00</em> matches always.</p></td></tr><tr><td><b>management_protection_key</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td></td></tr><tr><td><b>private_algo</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              104bit-wep
                            </li><li>
                              40bit-wep
                            </li><li>
                              aes-ccm
                            </li><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li><li>
                              tkip
                            </li></ul></td><td><p>Only for WEP modes.</p></td></tr><tr><td><b>private_key</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Only for WEP modes.</p></td></tr><tr><td><b>private_pre_shared_key</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Used in WPA PSK mode.</p></td></tr><tr><td><b>signal_range</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Rule matches if signal strength of the station is within the range.</p><p>If signal strength of the station will go out of the range that is specified in the rule, access point will disconnect that station.</p></td></tr><tr><td><b>time</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Rule will match only during specified time.</p><p>Station will be disconnected after specified time ends. Both start and end time is expressed as time since midnight, 00:00.</p><p>Rule will match only during specified days of the week.</p></td></tr></table>



========
Examples
========




-----------------
Using merge state
-----------------


**Before State**

.. code-block:: ssh

    /interface wireless access-list
    add comment=existing action accept signal-range=-79..120
    



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge with device configuration
      kilip.routeros.ros_wireless_access_list:
        config:
          - comment: existing
            signal_range: '-80..120'
          - comment: new
            signal_range: '-50..120'
            interface: wlan1
        state: merged
        
      

**Executed Command**


.. code-block:: ssh

    /interface wireless access-list set [ find comment=existing ] signal-range=-80..120
    /interface wireless access-list add comment=new signal-range=-50..120 interface=wlan1


**After State**


.. code-block:: ssh

    /interface wireless access-list
    add comment=existing action=accept signal-range=-80..120
    add comment=new action=accept signal-range=-50..120
    


