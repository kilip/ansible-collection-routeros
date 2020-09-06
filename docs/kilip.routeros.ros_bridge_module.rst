.. _kilip.routeros.ros_bridge_module

********************************
kilip.routeros.ros_bridge
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface bridge**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This modules manages configuration in submenu `/interface bridge`.



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
  A dictionary for `/interface bridge` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>add_dhcp_option82</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Whether to add DHCP Option-82 information (Agent Remote ID and Agent Circuit ID) to DHCP packets. Can be used together with Option-82 capable DHCP server to assign IP addresses and implement policies. This property only has effect when dhcp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>admin_mac</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Static MAC address of the bridge. This property only has effect when auto-mac is set to <code>no</code>.</p></td></tr><tr><td><b>ageing_time</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>How long a host's information will be kept in the bridge database.</p></td></tr><tr><td><b>arp</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li><li>
                              proxy-arp
                            </li><li>
                              reply-only
                            </li></ul></td><td><p>Address Resolution Protocol setting</p><ul><li><code>disabled</code> - the interface will not use ARP</li><li><code>enabled</code> - the interface will use ARP</li><li><code>proxy-arp</code> - the interface will use the ARP proxy feature</li><li><code>reply-only</code> - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the <a href="https://wiki.mikrotik.com/wiki/Manual:IP/ARP" title="Manual:IP/ARP"> IP/ARP</a> table. No dynamic entries will be automatically stored in the <a href="https://wiki.mikrotik.com/wiki/Manual:IP/ARP" title="Manual:IP/ARP"> IP/ARP</a> table. Therefore for communications to be successful, a valid static entry must already exist.</li></ul></td></tr><tr><td><b>arp_timeout</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value <code>auto</code> equals to the value of arp-timeout in <a href="https://wiki.mikrotik.com/wiki/Manual:IP/Settings" title="Manual:IP/Settings"> IP/Settings</a>, default is 30s.</p></td></tr><tr><td><b>auto_mac</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>Automatically select one MAC address of bridge ports as a bridge MAC address, bridge MAC will be chosen from the first added bridge port. After a device reboot, the bridge MAC can change depending on the port-number.</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Short description of the interface.</p></td></tr><tr><td><b>dhcp_snooping</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Enables or disables DHCP Snooping on the bridge.</p></td></tr><tr><td><b>disabled</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Changes whether the bridge is disabled.</p></td></tr><tr><td><b>ether_type</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>0x8100</b>&nbsp;&larr;</div></li><li>
                              0x88a8
                            </li><li>
                              0x9100
                            </li></ul></td><td><p>Changes the EtherType, which will be used to determine if a packet has a VLAN tag. Packets that have a matching EtherType are considered as tagged packets. This property only has effect when vlan-filtering is set to <code>yes</code>.</p></td></tr><tr><td><b>fast_forward</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>Special and faster case of <a href="https://wiki.mikrotik.com/wiki/Manual:Fast_Path" title="Manual:Fast Path"> FastPath</a> which works only on bridges with 2 interfaces (enabled by default only for new bridges). More details can be found in the <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Bridge#Fast_Forward" title="Manual:Interface/Bridge"> Fast Forward</a> section.</p></td></tr><tr><td><b>forward_delay</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Time which is spent during the initialization phase of the bridge interface (i.e., after router startup or enabling the interface) in listening/learning state before the bridge will start functioning normally.</p></td></tr><tr><td><b>frame_types</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>admit-all</b>&nbsp;&larr;</div></li><li>
                              admit-only-untagged-and-priority-tagged
                            </li><li>
                              admit-only-vlan-tagged
                            </li></ul></td><td><p>Specifies allowed frame types on a bridge port. This property only has effect when vlan-filtering is set to <code>yes</code>.</p></td></tr><tr><td><b>igmp_snooping</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Enables multicast group and port learning to prevent multicast traffic from flooding all interfaces in a bridge.</p></td></tr><tr><td><b>igmp_version</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>2</b>&nbsp;&larr;</div></li><li>
                              3
                            </li></ul></td><td><p>Selects the IGMP version in which IGMP general membership queries will be generated. This property only has effect when igmp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>ingress_filtering</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. By default, VLANs that don't exist in the bridge VLAN table are dropped before they are sent out (egress), but this property allows you to drop the packets when they are received (ingress). Should be used with frame-types to specify if the ingress traffic should be tagged or untagged. This property only has effect when vlan-filtering is set to <code>yes</code>.</p></td></tr><tr><td><b>last_member_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>If a port has fast-leave set to <code>no</code> and a bridge port receives a IGMP Leave message, then a IGMP Snooping enabled bridge will send a IGMP query to make sure that no devices has subscribed to a certain multicast stream on a bridge port. If a IGMP Snooping enabled bridge does not receive a IGMP membership report after amount of last-member-interval, then the bridge considers that no one has subscribed to a certain multicast stream and can stop forwarding it. This property only has effect when igmp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>last_member_query_count</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>How many times should last-member-interval pass until a IGMP Snooping bridge will stop forwarding a certain multicast stream. This property only has effect when igmp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>max_hops</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Bridge count which BPDU can pass in a MSTP enabled network in the same region before BPDU is being ignored. This property only has effect when protocol-mode is set to <code>mstp</code>.</p></td></tr><tr><td><b>max_message_age</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>How long to remember Hello messages received from other STP/RSTP enabled bridges. This property only has effect when protocol-mode is set to <code>stp</code> or <code>rstp</code>.</p></td></tr><tr><td><b>membership_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Amount of time after an entry in the Multicast Database (MDB) is removed if a IGMP membership report is not received on a certain port. This property only has effect when igmp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>mld_version</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>1</b>&nbsp;&larr;</div></li><li>
                              2
                            </li></ul></td><td><p>Selects the MLD version. Version 2 adds support for source-specific multicast. This property only has effect when RouterOS IPv6 package is enabled and igmp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>mtu</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Maximum transmission unit, by default, the bridge will set MTU automatically and it will use the lowest MTU value of any associated bridge port. The default bridge MTU value without any bridge ports added is 1500. The MTU value can be set manually, but it cannot exceed the bridge L2MTU or the lowest bridge port L2MTU. If a new bridge port is added with L2MTU which is smaller than the actual-mtu of the bridge (set by the mtu property), then manually set value will be ignored and the bridge will act as if <code>mtu=auto</code> is set.</p></td></tr><tr><td><b>multicast_querier</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Multicast querier generates IGMP general membership queries to which all IGMP capable devices respond with a IGMP membership report, usually a PIM (multicast) router generates these queries. By using this property you can make a IGMP Snooping enabled bridge to generate IGMP general membership queries. This property should be used whenever there is no PIM (multicast) router in a Layer2 network or IGMP packets must be sent through multiple IGMP Snooping enabled bridges to reach a PIM (multicast) router. Without a multicast querier in a Layer2 network the Multicast Database (MDB) is not being updated and IGMP Snooping will not function properly. Only untagged IGMP general membership queries are generated. This property only has effect when igmp-snooping is set to <code>yes</code>. Additionally, the igmp-snooping should be disabled/enabled after changing multicast-querier property.</p></td></tr><tr><td><b>multicast_router</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li>
                              permanent
                            </li><li><div style="color: blue"><b>temporary-query</b>&nbsp;&larr;</div></li></ul></td><td><p>Changes the state of a bridge itself if IGMP membership reports are going to be forwarded to it. This property can be used to forward IGMP membership reports to the bridge for statistics or to analyse them.</p><ul><li><code>disabled</code> - IGMP membership reports are not forwarded to the bridge itself regardless what is connected to it.</li><li><code>permanent</code> - IGMP membership reports are forwarded through this the bridge itself regardless what is connected to it.</li><li><code>temporary-query</code> - automatically detect multicast routers and IGMP Snooping enabled bridges. This property only has effect when igmp-snooping is set to <code>yes</code>.</li></ul></td></tr><tr><td><b>name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of the bridge interface</p></td></tr><tr><td><b>priority</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Bridge priority, used by STP to determine root bridge, used by MSTP to determine CIST and IST regional root bridge. This property has no effect when protocol-mode is set to <code>none</code>.</p></td></tr><tr><td><b>protocol_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              mstp
                            </li><li>
                              none
                            </li><li><div style="color: blue"><b>rstp</b>&nbsp;&larr;</div></li><li>
                              stp
                            </li></ul></td><td><p>Select Spanning tree protocol (STP) or Rapid spanning tree protocol (RSTP) to ensure a loop-free topology for any bridged LAN. RSTP provides for faster spanning tree convergence after a topology change. Select MSTP to ensure loop-free topology across multiple VLANs. Since RouterOS v6.43 it is possible to forward Reserved MAC addresses that are in <strong>01:80:C2:00:00:0X</strong> range, this can be done by setting the protocol-mode to <code>none</code>.</p></td></tr><tr><td><b>pvid</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. It applies e.g. to frames sent from bridge IP and destined to a bridge port. This property only has effect when vlan-filtering is set to <code>yes</code>.</p></td></tr><tr><td><b>querier_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Used to change the interval how often a bridge checks if it is the active multicast querier. This property only has effect when igmp-snooping and multicast-querier is set to <code>yes</code>.</p></td></tr><tr><td><b>query_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Used to change the interval how often IGMP general membership queries are sent out. This property only has effect when igmp-snooping and multicast-querier is set to <code>yes</code>.</p></td></tr><tr><td><b>query_response_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Interval in which a IGMP capable device must reply to a IGMP query with a IGMP membership report. This property only has effect when igmp-snooping and multicast-querier is set to <code>yes</code>.</p></td></tr><tr><td><b>region_name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>MSTP region name. This property only has effect when protocol-mode is set to <code>mstp</code>.</p></td></tr><tr><td><b>region_revision</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>MSTP configuration revision number. This property only has effect when protocol-mode is set to <code>mstp</code>.</p></td></tr><tr><td><b>startup_query_count</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Specifies how many times must startup-query-interval pass until the bridge starts sending out IGMP general membership queries periodically. This property only has effect when igmp-snooping and multicast-querier is set to <code>yes</code>.</p></td></tr><tr><td><b>startup_query_interval</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Used to change the amount of time after a bridge starts sending out IGMP general membership queries after the bridge is enabled. This property only has effect when igmp-snooping and multicast-querier is set to <code>yes</code>.</p></td></tr><tr><td><b>transmit_hold_count</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>The Transmit Hold Count used by the Port Transmit state machine to limit transmission rate.</p></td></tr><tr><td><b>vlan_filtering</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Globally enables or disables VLAN functionality for bridge.</p></td></tr></table>



========
Examples
========




------------
Using Merged
------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface bridge
    add comment="trunk bridge" name=br-trunk arp=reply-only
    add comment="wan bridge" name=br-wan arp=reply-only



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge configuration with device configuration
      kilip.routeros.ros_bridge:
        config:
          - name: br-wan
            comment: 'updated comment'
            arp: enabled
          - name: br-trunk
            comment: 'updated comment'
            arp: enabled
            vlan_filtering: 'yes'
        state: merged
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge set [ find name=br-wan ] comment="updated comment" arp=enabled
    /interface bridge set [ find name=br-trunk ] comment="updated comment" arp=enabled vlan-filtering=yes


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface bridge
    add comment="trunk bridge" name=br-trunk vlan-filtering=yes arp=enabled
    add comment="wan bridge" name=br-wan arp=enabled




--------------
Using Replaced
--------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface bridge
    add comment="trunk bridge" name=br-trunk arp=reply-only
    add comment="wan bridge" name=br-wan arp=reply-only



**Configuration**


.. code-block:: yaml+jinja

    - name: Replace device configuration
      kilip.routeros.ros_bridge:
        config:
          - name: br-wan
            comment: 'replaced comment'
          - name: br-trunk
            comment: 'replaced comment'
        state: replaced
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge set [ find name=br-wan ] comment="replaced comment" arp=enabled
    /interface bridge set [ find name=br-trunk ] comment="replaced comment" arp=enabled


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface bridge
    add comment="replaced comment" name=br-trunk arp=enabled
    add comment="replaced comment" name=br-wan arp=enabled




----------------
Using Overridden
----------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface bridge
    add comment="trunk bridge" name=br-trunk arp=reply-only
    add comment="wan bridge" name=br-wan arp=reply-only



**Configuration**


.. code-block:: yaml+jinja

    - name: Override bridge configuration
      kilip.routeros.ros_bridge:
        config:
          - comment: 'new bridge'
            name: br-new
        state: overridden
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge remove [ find name=br-trunk ]
    /interface bridge remove [ find name=br-wan ]
    /interface bridge add comment="new bridge" name=br-new
    /system script run ansible-remove-invalid


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    # All existing bridge will be removed and replaced with the new configuration.
    /interface bridge
    add comment="new bridge" name=br-new




-------------------
Using deleted state
-------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface bridge
    add comment="trunk bridge" name=br-trunk arp=reply-only
    add comment="wan bridge" name=br-wan arp=reply-only



**Configuration**


.. code-block:: yaml+jinja

    - name: Delete bridge
      kilip.routeros.ros_bridge:
        config:
          - name: br-trunk
          - name: br-wan
        state: deleted
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge remove [ find name=br-trunk ]
    /interface bridge remove [ find name=br-wan ]
    /system script run ansible-remove-invalid


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    # All existing bridge will be removed and replaced with the new configuration.
    # empty bridge config


