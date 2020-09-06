.. _kilip.routeros.ros_vlan_module

********************************
kilip.routeros.ros_vlan
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface vlan**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This module manages the vlan configuration of Mikrotik RouterOS network devices.



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
  A dictionary for `/interface vlan` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>arp</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              disabled
                            </li><li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li><li>
                              proxy-arp
                            </li><li>
                              reply-only
                            </li></ul></td><td><p>Address Resolution Protocol mode</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Give notes for this resource</p></td></tr><tr><td><b>interface</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of physical interface on top of which VLAN will work</p></td></tr><tr><td><b>l2mtu</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Layer2 MTU. For VLANS this value is not configurable. <a href="https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards" title="Maximum Transmission Unit on RouterBoards"> Read more&gt;&gt;</a></p></td></tr><tr><td><b>mtu</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Layer3 Maximum transmission unit</p></td></tr><tr><td><b>name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Interface name</p></td></tr><tr><td><b>use_service_tag</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li>
                              yes
                            </li></ul></td><td><p>802.1ad compatible Service Tag</p></td></tr><tr><td><b>vlan_id</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Virtual LAN identifier or tag that is used to distinguish VLANs. Must be equal for all computers that belong to the same VLAN.</p></td></tr></table>



========
Examples
========




------------------
Using merged state
------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface vlan export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface vlan
    add interface=br-trunk name=vlan-100 vlan-id=100 arp=reply-only



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge configuration with device configuration
      kilip.routeros.ros_vlan:
        config:
          - name: vlan-100
            interface: br-trunk
            vlan_id: 100
            comment: 'new comment'
          - name: vlan-200
            interface: br-trunk
            vlan_id: 200
            comment: 'new comment'
        state: merged
        
      

**Executed Command**


.. code-block:: ssh

    /interface vlan set [ find name=vlan-100 ] comment="new comment" arp=enabled
    /interface vlan add name=vlan-200 interface=br-trunk vlan-id=200 comment="new comment"


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface vlan export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface vlan
    add interface=br-trunk name=vlan-100 vlan-id=100 comment="new comment"
    add interface=br-trunk name=vlan-200 vlan-id=200 comment="new comment"




--------------------
Using replaced state
--------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface vlan export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface vlan
    add interface=br-trunk name=vlan-100 vlan-id=100 arp=reply-only



**Configuration**


.. code-block:: yaml+jinja

    - name: Replace device configuration
      kilip.routeros.ros_vlan:
        config:
          - name: vlan-100
            interface: br-trunk
            vlan_id: 100
            comment: 'new comment'
        state: replaced
        
      

**Executed Command**


.. code-block:: ssh

    /interface vlan set [ find name=vlan-100 ] arp=enabled
    /interface vlan set [ find name=vlan-100 ] interface=br-trunk vlan-id=100 comment="new comment"


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface vlan export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface vlan
    add interface=br-trunk name=vlan-100 vlan-id=100 comment="new comment"
    add interface=br-trunk name=vlan-200 vlan-id=200 comment="new comment"




----------------------
Using overridden state
----------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface vlan export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface vlan
    add interface=br-trunk name=vlan-100 vlan-id=100 arp=reply-only



**Configuration**


.. code-block:: yaml+jinja

    - name: Override device configuration
      kilip.routeros.ros_vlan:
        config:
          - name: vlan-new
            interface: br-trunk
            vlan_id: 100
            comment: 'new comment'
        state: overridden
        
      

**Executed Command**


.. code-block:: ssh

    /interface vlan remove [ find name=vlan-100 ]
    /interface vlan add name=vlan-new interface=br-trunk vlan-id=100 comment="new comment"
    /system script run ansible-remove-invalid


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface vlan export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface vlan
    add name=vlan-new interface=br-trunk vlan-id=100 comment="new comment"




-------------------
Using deleted state
-------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface vlan export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface vlan
    add interface=br-trunk name=vlan-100 vlan-id=100 arp=reply-only



**Configuration**


.. code-block:: yaml+jinja

    - name: Delete VLAN Interface
      kilip.routeros.ros_vlan:
        config:
          - name: vlan-100
            interface: br-trunk
            vlan_id: 100
        state: deleted
        
      

**Executed Command**


.. code-block:: ssh

    /interface vlan remove [ find name=vlan-100 ]
    /system script run ansible-remove-invalid


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface vlan export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =



