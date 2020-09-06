.. _kilip.routeros.ros_ethernet_module

********************************
kilip.routeros.ros_ethernet
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface ethernet**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This module manages the ethernet configuration of Mikrotik RouterOS network devices.



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
  A dictionary for `/interface ethernet` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>advertise</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              10000M-full
                            </li><li>
                              1000M-full
                            </li><li>
                              1000M-half
                            </li><li>
                              100M-full
                            </li><li>
                              100M-half
                            </li><li>
                              10M-full
                            </li><li>
                              10M-half
                            </li><li>
                              2500M-full
                            </li><li>
                              5000M-full
                            </li></ul></td><td><p>Advertised speed and duplex modes for Ethernet interfaces over twisted pair, only applies when auto-negotiation is enabled. Advertising higher speeds than the actual interface supported speed will have no effect, multiple options are allowed.</p></td></tr><tr><td><b>arp</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li><li>
                              local-proxy-arp
                            </li><li>
                              proxy-arp
                            </li><li>
                              reply-only
                            </li></ul></td><td><p>Address Resolution Protocol mode:</p><ul><li>disabled - the interface will not use ARP</li><li>enabled - the interface will use ARP</li><li>local-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interface</li><li>proxy-arp - the router performs proxy ARP on the interface and sends replies to other interfaces</li><li>reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the <a href="https://wiki.mikrotik.com/wiki/Manual:IP/ARP" title="Manual:IP/ARP"> ARP</a> table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.</li></ul></td></tr><tr><td><b>auto_negotiation</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>When enabled, the interface 'advertises' its maximum capabilities to achieve the best connection possible.</p><ul><li><strong>Note1:</strong> Auto-negotiation should not be disabled on one end only, otherwise Ethernet Interfaces may not work properly.</li><li><strong>Note2:</strong> Gigabit Ethernet and NBASE-T Ethernet links cannot work with auto-negotiation disabled.</li></ul></td></tr><tr><td><b>bandwidth</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Sets max rx/tx bandwidth in kbps that will be handled by an interface. TX limit is supported on all Atheros <a href="https://wiki.mikrotik.com/wiki/Manual:Switch_Chip_Features" title="Manual:Switch Chip Features"> switch-chip</a> ports. RX limit is supported only on Atheros8327/QCA8337 switch-chip ports.</p></td></tr><tr><td><b>cable_setting</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>default</b>&nbsp;&larr;</div></li><li>
                              short
                            </li><li>
                              standard
                            </li></ul></td><td><p>Changes the cable length setting (only applicable to NS DP83815/6 cards)</p></td></tr><tr><td><b>combo_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>auto</b>&nbsp;&larr;</div></li><li>
                              copper
                            </li><li>
                              sfp
                            </li></ul></td><td><p>When auto mode is selected, the port that was first connected will establish the link. In case this link fails, the other port will try to establish a new link. If both ports are connected at the same time (e.g. after reboot), the priority will be the SFP/SFP+ port. When sfp mode is selected, the interface will only work through SFP/SFP+ cage. When copper mode is selected, the interface will only work through RJ45 Ethernet port.</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Descriptive name of an item</p></td></tr><tr><td><b>disable_running_check</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>Disable running check. If this value is set to 'no', the router automatically detects whether the NIC is connected with a device in the network or not. Default value is 'yes' because older NICs do not support it. (only applicable to x86)</p></td></tr><tr><td><b>disabled</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              yes
                            </li><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li></ul></td><td><p>Set interface disability.</p></td></tr><tr><td><b>full_duplex</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>Defines whether the transmission of data appears in two directions simultaneously, only applies when auto-negotiation is disabled.</p></td></tr><tr><td><b>l2mtu</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Layer2 Maximum transmission unit. <a href="https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards" title="Maximum Transmission Unit on RouterBoards"> Read more&gt;&gt; </a></p></td></tr><tr><td><b>mac_address</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Media Access Control number of an interface.</p></td></tr><tr><td><b>master_port</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Outdated property, more details about this property can be found in the <a href="https://wiki.mikrotik.com/wiki/Manual:Master-port" title="Manual:Master-port"> Master-port</a> page.</p></td></tr><tr><td><b>mdix_enable</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>Whether the MDI/X auto cross over cable correction feature is enabled for the port (Hardware specific, e.g. ether1 on RB500 can be set to yes/no. Fixed to 'yes' on other hardware.)</p></td></tr><tr><td><b>mtu</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Layer3 Maximum transmission unit</p></td></tr><tr><td><b>name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of an interface</p></td></tr><tr><td><b>poe_out</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              auto-on
                            </li><li>
                              forced-on
                            </li><li><div style="color: blue"><b>off</b>&nbsp;&larr;</div></li></ul></td><td><p>Poe Out settings. <a href="https://wiki.mikrotik.com/wiki/Manual:PoE-Out" title="Manual:PoE-Out"><code>Read more &gt;&gt;</code></a></p></td></tr><tr><td><b>poe_priority</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Poe Out settings. <a href="https://wiki.mikrotik.com/wiki/Manual:PoE-Out" title="Manual:PoE-Out"><code>Read more &gt;&gt;</code></a></p></td></tr><tr><td><b>rx_flow_control</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              auto
                            </li><li><div style="color: blue"><b>off</b>&nbsp;&larr;</div></li><li>
                              on
                            </li></ul></td><td><p>When set to on, the port will process received pause frames and suspend transmission if required. <strong>auto</strong> is the same as <strong>on</strong> except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises.</p></td></tr><tr><td><b>speed</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              100Mbps
                            </li><li>
                              10Gbps
                            </li><li>
                              10Mbps
                            </li><li>
                              1Gbps
                            </li></ul></td><td><p>Sets interface data transmission speed which takes effect only when auto-negotiation is disabled.</p></td></tr><tr><td><b>tx_flow_control</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              auto
                            </li><li><div style="color: blue"><b>off</b>&nbsp;&larr;</div></li><li>
                              on
                            </li></ul></td><td><p>When set to on, the port will generate pause frames to the upstream device to temporarily stop the packet transmission. Pause frames are only generated when some routers output interface is congested and packets cannot be transmitted anymore. <strong>auto</strong> is the same as <strong>on</strong> except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises.</p></td></tr></table>



========
Examples
========




------------------
Using merged state
------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface ethernet export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface ethernet
    set [ find default-name=ether1 ] comment="ether1 comment"



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge configuration with device configuration
      kilip.routeros.ros_ethernet:
        config:
          - name: ether1
            advertise:
              - 10M-full
              - 100M-full
              - 1000M-full
            comment: 'updated comment'
        state: merged
        
      

**Executed Command**


.. code-block:: ssh

    /interface ethernet set [ find name=ether1 ] advertise=10M-full,100M-full,1000M-full comment="updated comment"


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface ethernet export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface ethernet
    set [ find default-name=ether1 ] comment="updated comment"


