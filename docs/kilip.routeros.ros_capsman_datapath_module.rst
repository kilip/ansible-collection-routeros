.. _kilip.routeros.ros_capsman_datapath_module

********************************
kilip.routeros.ros_capsman_datapath
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/caps-man datapath**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This modules manages CAPsMan DataPath Configuration on Mikrotik RouterOS network devices



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
  A dictionary for `/caps-man datapath` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>arp</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li><li>
                              proxy-arp
                            </li><li>
                              reply-only
                            </li></ul></td><td><p>Address Resolution Protocol setting</p><ul><li><code>disabled</code> - the interface will not use ARP</li><li><code>enabled</code> - the interface will use ARP</li><li><code>proxy-arp</code> - the interface will use the ARP proxy feature</li><li><code>reply-only</code> - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the L(IP/ARP,<a href="https://wiki.mikrotik.com/wiki/Manual:IP/ARP">https://wiki.mikrotik.com/wiki/Manual:IP/ARP</a>) table. Therefore for communications to be successful, a valid static entry must already exist.</li></ul></td></tr><tr><td><b>bridge</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Bridge to which particular interface should be automatically added as port. Required only when local-forwarding is not used.</p></td></tr><tr><td><b>bridge_cost</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>bridge port cost to use when adding as bridge port</p></td></tr><tr><td><b>bridge_horizon</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>bridge horizon to use when adding as bridge port</p></td></tr><tr><td><b>client_to_client_forwarding</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              yes
                            </li><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li></ul></td><td><p>controls if client-to-client forwarding between wireless clients connected to interface should be allowed, in local forwarding mode this function is performed by CAP, otherwise it is performed by CAPsMAN</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Short description of the datapath</p></td></tr><tr><td><b>interface_list</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td></td><td><p>interface list for this datapath</p></td></tr><tr><td><b>l2mtu</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>set Layer2 MTU size</p></td></tr><tr><td><b>local_forwarding</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              yes
                            </li><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li></ul></td><td><p>Controls forwarding mode. If disabled, all L2 and L3 data will be forwarded to CAPsMAN, and further forwarding decisions will be made only then.
Note, if disabled, make sure that each CAP interface MAC Address that participates in the same broadcast domain is unique (including local MACs, like Bridge-MAC).</p></td></tr><tr><td><b>mtu</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>set MTU size</p></td></tr><tr><td><b>name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name for datapath</p></td></tr><tr><td><b>openflow_switch</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>OpenFlow switch port (when enabled) to add interface to</p></td></tr><tr><td><b>vlan_id</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>VLAN ID to assign to interface if vlan-mode enables use of VLAN tagging</p></td></tr><tr><td><b>vlan_mode</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              use-service-tag
                            </li><li>
                              use-tag
                            </li></ul></td><td><p>Enables and specifies the type of VLAN tag to be assigned to the interface (causes all received data to get tagged with VLAN tag and allows the interface to only send out data tagged with given tag)</p></td></tr></table>



========
Examples
========




------------
Using Merged
------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /caps-man datapath export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man datapath
    add name=test



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge with device configuration
      kilip.routeros.ros_capsman_datapath:
        state: merged
        config:
          - name: test
            bridge: br-trunk
            arp: reply-only
          - name: new
            bridge: br-trunk
            arp: reply-only
        
      

**Executed Command**


.. code-block:: ssh

    /caps-man datapath set [ find name=test ] arp=reply-only bridge=br-trunk
    /caps-man datapath add arp=reply-only bridge=br-trunk name=new


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /caps-man datapath export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man datapath
    add name=test bridge=br-trunk arp=reply-only
    add name=new bridge=br-trunk arp=reply-only


