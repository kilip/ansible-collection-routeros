.. _kilip.routeros.kilip.routeros.ros_wireless_cap_module

********************************
kilip.routeros.kilip.routeros.ros_wireless_cap
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/interface wireless cap**

.. contents::
   :local:
   :depth: 2

========
Synopsis
========

-  This module manages the Wireless CAP setting of Mikrotik RouterOS network devices.

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
  A dictionary for `/interface wireless cap` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>bridge</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Bridge to which interfaces should be added when local forwarding mode is used</p></td></tr><tr><td><b>caps_man_addresses</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td></td><td><p>List of Manager IP addresses that CAP will attempt to contact during discovery</p></td></tr><tr><td><b>caps_man_certificate_common_names</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td></td><td><p>List of Manager certificate CommonNames that CAP will connect to, if empty - CAP does not check Manager certificate CommonName</p></td></tr><tr><td><b>caps_man_names</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td></td><td><p>An ordered list of CAPs Manager names that the CAP will connect to, if empty - CAP does not check Manager name</p></td></tr><tr><td><b>certificate</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Certificate to use for authenticating</p></td></tr><tr><td><b>discovery_interfaces</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td></td><td><p>List of interfaces over which CAP should attempt to discover Manager</p></td></tr><tr><td><b>enabled</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Disable or enable CAP feature</p></td></tr><tr><td><b>interfaces</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td></td><td><p>List of wireless interfaces to be controlled by Manager</p></td></tr><tr><td><b>static_virtual</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              yes
                            </li><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li></ul></td><td><p>CAP will create Static Virtual Interfaces instead of Dynamic and will try to reuse the same interface on reconnect to CAPsMAN if the MAC address will be the same. Note if two or more interfaces will have the same MAC address the assignment from the CAPsMAN could be random between those interfaces.</p></td></tr></table>

========
Examples
========

---------------------------
Change Wireless CAP Setting
---------------------------

**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /interface wireless cap export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface wireless cap
    set bridge=none caps-man-addresses="" caps-man-certificate-common-names="" caps-man-names="" \
        certificate=none discovery-interfaces="" \
        enabled=no interfaces="" lock-to-caps-man=no static-virtual=no

**Configuration**

.. code-block:: yaml+jinja

    - name: Configure Wireless CAP
      kilip.routeros.kilip.routeros.ros_wireless_cap:
        config:
          interfaces:
            - wlan1
            - wlan2
        state: present

**Executed Command**

.. code-block:: ssh

    /interface wireless cap set interfaces=wlan1,wlan2

**After State**

.. code-block:: ssh

    [admin@MikroTik] > /interface wireless cap export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /interface wireless cap
    set interface=wlan-new
