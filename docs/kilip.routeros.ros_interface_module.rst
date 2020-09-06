.. _kilip.routeros.ros_interface_module

********************************
kilip.routeros.ros_interface
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This module manages the interface configuration of Mikrotik RouterOS network devices.



==========
Parameters
==========


state
  | **choices**: merged
  | **default**: merged
  | **required**: False
  | **type**: str
  Available state for this module

config
  | **type**: list
  | **elements**: dict
  A dictionary for `/interface` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Give notes for this resource</p></td></tr><tr><td><b>disabled</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              yes
                            </li><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li></ul></td><td><p>Set interface disability.</p></td></tr><tr><td><b>l2mtu</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Layer2 Maximum transmission unit. Note that this property can not be configured on all interfaces. <a href="https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards" title="Maximum Transmission Unit on RouterBoards"> Read more&gt;&gt; </a></p></td></tr><tr><td><b>mtu</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Layer3 Maximum transmission unit</p></td></tr><tr><td><b>name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Name of an interface</p></td></tr></table>



========
Examples
========




------------
Using Merged
------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface ethernet
    set [ find default-name=ether1 ] comment="ether1 comment" mtu=1500
    set [ find default-name=ether2 ] comment="ether2 comment" disabled=yes
    /interface bridge
    add name=br-wan comment="wan bridge"



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge configuration with device configuration
      kilip.routeros.ros_interface:
        config:
          - name: ether1
            comment: 'ether1 updated'
            mtu: 1000
          - name: ether2
            comment: 'ether2 updated'
            mtu: 2000
            disabled: false
          - name: br-wan
            disabled: true
            mtu: 3000
            comment: 'br-wan updated'
        state: merged
        
      

**Executed Command**


.. code-block:: ssh

    /interface set [ find name=ether1 ] comment="ether1 updated" mtu=1000
    /interface set [ find name=ether2 ] comment="ether2 updated" mtu=2000 disabled=no
    /interface set [ find name=br-wan ] disabled=yes mtu=3000 comment="br-wan updated"


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface ethernet
    set [ find default-name=ether1 ] comment="ether1 updated" mtu=1000
    set [ find default-name=ether2 ] comment="ether2 updated" mtu=2000
    /interface bridge
    add name=br-wan comment="br-wan updated" mtu=3000 disabled=yes


