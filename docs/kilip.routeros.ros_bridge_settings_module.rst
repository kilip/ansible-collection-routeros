.. _kilip.routeros.ros_bridge_settings_module

********************************
kilip.routeros.ros_bridge_settings
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface bridge settings**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This modules manages configuration in submenu `/interface bridge settings`.



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
  A dictionary for `/interface bridge settings` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>allow_fast_path</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              no
                            </li><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li></ul></td><td><p>Whether to enable a bridge <a href="https://wiki.mikrotik.com/wiki/Manual:Fast_Path" title="Manual:Fast Path"> FastPath</a> globally.</p></td></tr><tr><td><b>use_ip_firewall</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Force bridged traffic to also be processed by prerouting, forward and postrouting sections of IP routing (<a href="https://wiki.mikrotik.com/wiki/Manual:Packet_Flow_v6" title="Manual:Packet Flow v6"> Packet Flow</a>). This does not apply to routed traffic. This property is required in case you want to assign <a href="https://wiki.mikrotik.com/wiki/Manual:Queue#Simple_Queues" title="Manual:Queue"> Simple Queues</a> or global <a href="https://wiki.mikrotik.com/wiki/Manual:Queue#Queue_Tree" title="Manual:Queue"> Queue Tree</a> to traffic in a bridge. Property use-ip-firewall-for-vlan is required in case bridge vlan-filtering is used.</p></td></tr><tr><td><b>use_ip_firewall_for_pppoe</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Send bridged un-encrypted PPPoE traffic to also be processed by <a href="https://wiki.mikrotik.com/wiki/Manual:IP/Firewall" title="Manual:IP/Firewall"> IP/Firewall</a>. This property only has effect when use-ip-firewall is set to <code>yes</code>. This property is required in case you want to assign <a href="https://wiki.mikrotik.com/wiki/Manual:Queue#Simple_Queues" title="Manual:Queue"> Simple Queues</a> or global <a href="https://wiki.mikrotik.com/wiki/Manual:Queue#Queue_Tree" title="Manual:Queue"> Queue Tree</a> to PPPoE traffic in a bridge.</p></td></tr><tr><td><b>use_ip_firewall_for_vlan</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Send bridged VLAN traffic to also be processed by <a href="https://wiki.mikrotik.com/wiki/Manual:IP/Firewall" title="Manual:IP/Firewall"> IP/Firewall</a>. This property only has effect when use-ip-firewall is set to <code>yes</code>. This property is required in case you want to assign <a href="https://wiki.mikrotik.com/wiki/Manual:Queue#Simple_Queues" title="Manual:Queue"> Simple Queues</a> or global <a href="https://wiki.mikrotik.com/wiki/Manual:Queue#Queue_Tree" title="Manual:Queue"> Queue Tree</a> to VLAN traffic in a bridge.</p></td></tr></table>



========
Examples
========




-----------------------------------
Change Bridge Setting Configuration
-----------------------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge settings export verbose
    /interface bridge settings
    set allow-fast-path=no use-ip-firewall=yes use-ip-firewall-for-pppoe=yes use-ip-firewall-for-vlan=yes
    



**Configuration**


.. code-block:: yaml+jinja

    - name: Configure Bridge Settings
      kilip.routeros.ros_bridge_settings:
        config:
          allow_fast_path: 'yes'
          use_ip_firewall: 'no'
          use_ip_firewall_for_pppoe: 'no'
          use_ip_firewall_for_vlan: 'no'
        state: present
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge settings set allow-fast-path=yes use-ip-firewall-for-pppoe=no use-ip-firewall-for-vlan=no use-ip-firewall=no


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge settings export verbose
    /interface bridge settings
    set allow-fast-path=yes use-ip-firewall=no use-ip-firewall-for-pppoe=no use-ip-firewall-for-vlan=no
    




-----------------------------------
Change Bridge Setting Configuration
-----------------------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface bridge settings export verbose
    /interface bridge settings
    set allow-fast-path=no use-ip-firewall-for-pppoe=yes use-ip-firewall-for-vlan=yes use-ip-firewall=yes
    



**Configuration**


.. code-block:: yaml+jinja

    - name: Configure Bridge Settings
      kilip.routeros.ros_bridge_settings:
        state: reset
        
      

**Executed Command**


.. code-block:: ssh

    /interface bridge settings set allow-fast-path=yes use-ip-firewall-for-pppoe=no use-ip-firewall-for-vlan=no use-ip-firewall=no


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /interface bridge settings export verbose
    /interface bridge settings
    set allow-fast-path=yes use-ip-firewall-for-pppoe=no use-ip-firewall-for-vlan=no use-ip-firewall=no


