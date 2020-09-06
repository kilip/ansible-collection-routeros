.. _kilip.routeros.ros_bridge_port_module

********************************
kilip.routeros.ros_bridge_port
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface bridge port**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This module manages RouterOS sub menu `/interface bridge port`



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
  A dictionary for `/interface bridge port` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>auto_isolate</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>When enabled, prevents a port moving from discarding into forwarding state if no BPDUs are received from the neighboring bridge. The port will change into a forwarding state only when a BPDU is received. This property only has an effect when protocol-mode is set to <code>rstp</code> or <code>mstp</code> and edge is set to <code>no</code>.</p></td></tr><tr><td><b>bpdu_guard</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Enables or disables BPDU Guard feature on a port. This feature puts the port in a disabled role if it receives a BPDU and requires the port to be manually disabled and enabled if a BPDU was received. Should be used to prevent a bridge from BPDU related attacks. This property has no effect when protocol-mode is set to <code>none</code>.</p></td></tr><tr><td><b>bridge</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>The bridge interface the respective interface is grouped in.</p></td></tr><tr><td><b>broadcast_flood</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>When enabled, bridge floods broadcast traffic to all bridge egress ports. When disabled, drops broadcast traffic on egress ports. Can be used to filter all broadcast traffic on an egress port. Broadcast traffic is considered as traffic that uses <strong>FF:FF:FF:FF:FF:FF</strong> as destination MAC address, such traffic is crucial for many protocols such as DHCP, ARP, NDP, BOOTP (Netinstall) and others. This option does not limit traffic flood to the CPU.</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Give notes for this resource</p></td></tr><tr><td><b>disabled</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              yes
                            </li><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li></ul></td><td><p>Set bridge port disability</p></td></tr><tr><td><b>edge</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>auto</b>&nbsp;&larr;</div></li><li>
                              no
                            </li><li>
                              no-discover
                            </li><li>
                              yes
                            </li><li>
                              yes-discover
                            </li></ul></td><td><p>Set port as edge port or non-edge port, or enable edge discovery. Edge ports are connected to a LAN that has no other bridges attached. An edge port will skip the learning and the listening states in STP and will transition directly to the forwarding state, this reduces the STP initialization time. If the port is configured to discover edge port then as soon as the bridge detects a BPDU coming to an edge port, the port becomes a non-edge port. This property has no effect when protocol-mode is set to <code>none</code>.</p><ul><li><code>no</code> - non-edge port, will participate in learning and listening states in STP.</li><li><code>no-discover</code> - non-edge port with enabled discovery, will participate in learning and listening states in STP, a port can become edge port if no BPDU is received.</li><li><code>yes</code> - edge port without discovery, will transit directly to forwarding state.</li><li><code>yes-discover</code> - edge port with enabled discovery, will transit directly to forwarding state.</li><li><code>auto</code> - same as <code>no-discover</code>, but will additionally detect if bridge port is a Wireless interface with disabled bridge-mode, such interface will be automatically set as an edge port without discovery.</li></ul></td></tr><tr><td><b>external_fdb</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>auto</b>&nbsp;&larr;</div></li><li>
                              no
                            </li><li>
                              yes
                            </li></ul></td><td><p>Whether to use wireless registration table to speed up bridge host learning. If there are no Wireless interfaces in a bridge, then setting external-fdb to <code>yes</code> will disable MAC learning and the bridge will act as a hub (disables hardware offloading). Replaced with learn parameter in RouterOS v6.42</p></td></tr><tr><td><b>fast_leave</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Enables IGMP Fast leave feature on the port. Bridge will stop forwarding traffic to a bridge port whenever a IGMP Leave message is received for appropriate multicast stream. This property only has effect when igmp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>frame_types</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>admit-all</b>&nbsp;&larr;</div></li><li>
                              admit-only-untagged-and-priority-tagged
                            </li><li>
                              admit-only-vlan-tagged
                            </li></ul></td><td><p>Specifies allowed ingress frame types on a bridge port. This property only has effect when vlan-filtering is set to <code>yes</code>.</p></td></tr><tr><td><b>horizon</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Use split horizon bridging to prevent bridging loops. Set the same value for group of ports, to prevent them from sending data to ports with the same horizon value. Split horizon is a software feature that disables hardware offloading. Read more about <a href="https://wiki.mikrotik.com/wiki/MPLSVPLS#Split_horizon_bridging" title="MPLSVPLS"> Bridge split horizon</a>.</p></td></tr><tr><td><b>ingress_filtering</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. Should be used with frame-types to specify if the ingress traffic should be tagged or untagged. This property only has effect when vlan-filtering is set to <code>yes</code>.</p></td></tr><tr><td><b>interface</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of the interface.</p></td></tr><tr><td><b>internal_path_cost</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Path cost to the interface for MSTI0 inside a region. This property only has effect when protocol-mode is set to <code>mstp</code>.</p></td></tr><tr><td><b>learn</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>auto</b>&nbsp;&larr;</div></li><li>
                              no
                            </li><li>
                              yes
                            </li></ul></td><td><p>Changes MAC learning behaviour on a bridge port</p><ul><li><code>yes</code> - enables MAC learning</li><li><code>no</code> - disables MAC learning</li><li><code>auto</code> - detects if bridge port is a Wireless interface and uses Wireless registration table instead of MAC learning, will use Wireless registration table if the <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless" title="Manual:Interface/Wireless"> Wireless interface</a> is set to one of ap-bridge,bridge,wds-slave mode and bridge mode for the <a href="https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless" title="Manual:Interface/Wireless"> Wireless interface</a> is disabled.</li></ul></td></tr><tr><td><b>multicast_router</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li>
                              permanent
                            </li><li><div style="color: blue"><b>temporary-query</b>&nbsp;&larr;</div></li></ul></td><td><p>Changes the state of a bridge port whether IGMP membership reports are going to be forwarded to this port. By default IGMP membership reports (most importantly IGMP Join messages) are only forwarded to ports that have a multicast router or a IGMP Snooping enabled bridge connected to. Without at least one port marked as a <code>multicast-router</code> IPTV might not work properly, it can be either detected automatically or forced manually.</p><ul><li><code>disabled</code> - IGMP membership reports are not forwarded through this port regardless what is connected to it.</li><li><code>permanent</code> - IGMP membership reports are forwarded through this port regardless what is connected to it.</li><li><code>temporary-query</code> - automatically detect multicast routers and IGMP Snooping enabled bridges.</li></ul><p>You can improve security by forcing ports that have IPTV boxes connected to never become ports marked as <code>multicast-router</code>. This property only has effect when igmp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>path_cost</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Path cost to the interface, used by STP to determine the 'best' path, used by MSTP to determine 'best' path between regions. This property has no effect when protocol-mode is set to <code>none</code>.</p></td></tr><tr><td><b>point_to_point</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>auto</b>&nbsp;&larr;</div></li><li>
                              no
                            </li><li>
                              yes
                            </li></ul></td><td><p>Specifies if a bridge port is connected to a bridge using a point-to-point link for faster convergence in case of failure. By setting this property to <code>yes</code>, you are forcing the link to be a point-to-point link, which will skip the checking mechanism, which detects and waits BPDUs from other devices from this single link, by setting this property to <code>no</code>, you are expecting that a link can receive BPDUs from multiple devices. By setting the property to <code>yes</code>, you are significantly improving (R/M)STP convergence time. In general, you should only set this property to <code>no</code> if it is possible that another device can be connected between a link, this is mostly relevant to Wireless mediums and Ethernet hubs. If the Ethernet link is full-duplex, <code>auto</code> enables point-to-point functionality. And this property has no effect when protocol-mode is set to <code>none</code>.</p></td></tr><tr><td><b>priority</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>The priority of the interface, used by STP to determine the root port, used by MSTP to determine root port between regions.</p></td></tr><tr><td><b>pvid</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. This property only has effect when vlan-filtering is set to <code>yes</code>.</p></td></tr><tr><td><b>restricted_role</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Enable the restricted role on a port, used by STP to forbid a port becoming a root port. This property only has effect when protocol-mode is set to <code>mstp</code>.</p></td></tr><tr><td><b>restricted_tcn</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Disable topology change notification (TCN) sending on a port, used by STP to forbid network topology changes to propagate. This property only has effect when protocol-mode is set to <code>mstp</code>.</p></td></tr><tr><td><b>tag_stacking</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Forces all packets to be treated as untagged packets. Packets on ingress port will be tagged with another VLAN tag regardless if a VLAN tag already exists, packets will be tagged with a VLAN ID that matches the pvid value and will use EtherType that is specified in ether-type. This property only has effect when vlan-filtering is set to <code>yes</code>.</p></td></tr><tr><td><b>trusted</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>When enabled, it allows to forward DHCP packets towards DHCP server through this port. Mainly used to limit unauthorized servers to provide malicious information for users. This property only has effect when dhcp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>unknown_multicast_flood</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>When enabled, bridge floods unknown multicast traffic to all bridge egress ports. When disabled, drops unknown multicast traffic on egress ports. Multicast addresses that are in <code>/interface bridge mdb</code> are considered as learned multicasts and therefore will not be flooded to all ports. Without IGMP Snooping all multicast traffic will be dropped on egress ports. Has effect only on an egress port. This option does not limit traffic flood to the CPU. Note that local multicast addresses (224.0.0.0/24) are not flooded when unknown-multicast-flood is disabled, as a result some protocols that rely on local multicast addresses might not work properly, such protocols are RIPv2m OSPF, mDNS, VRRP and others. Some protocols do send a IGMP join request and therefore are compatible with IGMP Snooping, some OSPF implementations are compatible with RFC1584, RouterOS OSPF implementation is not compatible with IGMP Snooping. This property should only be used when igmp-snooping is set to <code>yes</code>.</p></td></tr><tr><td><b>unknown_unicast_flood</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>When enabled, bridge floods unknown unicast traffic to all bridge egress ports. When disabled, drops unknown unicast traffic on egress ports. If a MAC address is not learned in <code>/interface bridge host</code>, then the traffic is considered as unknown unicast traffic and will be flooded to all ports. MAC address is learnt as soon as a packet on a bridge port is received, then the source MAC address is added to the bridge host table. Since it is required for the bridge to receive at least one packet on the bridge port to learn the MAC address, it is recommended to use static bridge host entries to avoid packets being dropped until the MAC address has been learnt. Has effect only on an egress port. This option does not limit traffic flood to the CPU.</p></td></tr></table>



========
Examples
========




--------------------
Merged Configuration
--------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge port export
    /interface bridge port
    add bridge=br-wan interface=ether1
    add bridge=br-trunk interface=ether2 disabled=yes
    



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge configuration with device configuration
      kilip.routeros.ros_bridge_port:
        config:
          - bridge: br-wan
            interface: ether1
            comment: 'new comment'
          - bridge: br-trunk
            interface: ether2
            comment: 'new comment'
        state: merged
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge port set [ find bridge=br-wan and interface=ether1 ] comment="new comment"
    /interface bridge port set [ find bridge=br-trunk and interface=ether2 ] comment="new comment" disabled=no


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge port export
    /interface bridge port
    add bridge=br-wan interface=ether1 comment="new comment"
    add bridge=br-trunk interface=ether2 comment="new comment"
    




--------------------
Using replaced state
--------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge port export
    /interface bridge port
    add bridge=br-wan interface=ether1
    add bridge=br-trunk interface=ether2 disabled=yes
    



**Configuration**


.. code-block:: yaml+jinja

    - name: Replace device configuration
      kilip.routeros.ros_bridge_port:
        config:
          - bridge: br-wan
            interface: ether1
            comment: 'new comment'
          - bridge: br-trunk
            interface: ether2
            comment: 'new comment'
        state: replaced
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge port set [ find bridge=br-wan and interface=ether1 ] comment="new comment"
    /interface bridge port set [ find bridge=br-trunk and interface=ether2 ] disabled=no
    /interface bridge port set [ find bridge=br-trunk and interface=ether2 ] comment="new comment"


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge port export
    /interfce bridge port
    add bridge=br-wan interface=ether1 comment="new comment"
    add bridge=br-trunk interface=ether2 comment="new comment"
    




----------------------
Using overridden state
----------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge port export
    /interface bridge port
    add bridge=br-wan interface=ether1
    add bridge=br-trunk interface=ether2 disabled=yes
    



**Configuration**


.. code-block:: yaml+jinja

    - name: Override device configuration
      kilip.routeros.ros_bridge_port:
        config:
          - bridge: br-new
            interface: ether2
            comment: 'new comment'
        state: overridden
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge port remove [ find bridge=br-wan and interface=ether1 ]
    /interface bridge port remove [ find bridge=br-trunk and interface=ether2 ]
    /interface bridge port add bridge=br-new interface=ether2 comment="new comment"
    /system script run ansible-remove-invalid


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge port export
    /interfce bridge port
    add bridge=br-new interface=ether2 comment="new comment"
    




-------------------
Using deleted state
-------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge port export
    /interface bridge port
    add bridge=br-wan interface=ether1
    add bridge=br-trunk interface=ether2 disabled=yes
    



**Configuration**


.. code-block:: yaml+jinja

    - name: Delete bridge port
      kilip.routeros.ros_bridge_port:
        config:
          - bridge: br-trunk
            interface: ether2
        state: deleted
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge port remove [ find bridge=br-trunk and interface=ether2 ]
    /system script run ansible-remove-invalid


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge port export
    /interfce bridge port
    add bridge=br-wan interface=ether1
    


