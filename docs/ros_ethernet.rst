.. _ros_ethernet_module:


ros_ethernet -- Manage configuration for ``/interface ethernet``
================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_ethernet <ros_ethernet_module>` module provides management for RouterOS ``/interface ethernet``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_ethernet <ros_ethernet_module>` will update existing ``/interface ethernet`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_ethernet <ros_ethernet_module>` will create new ``/interface ethernet``,



  config (optional, list, None)
    A dictionary for L(ros_ethernet)


    advertise (optional, list, None)
      Advertised speed and duplex modes for Ethernet interfaces over twisted pair,
only applies when auto-negotiation is enabled. Advertising higher speeds than
the actual interface supported speed will have no effect, multiple options are
allowed.



    arp (optional, str, enabled)
      Address Resolution Protocol mode:
- disabled - the interface will not use ARP
- enabled - the interface will use ARP
- local-proxy-arp - the router performs proxy ARP on the interface and sends
replies to the same interface
- proxy-arp - the router performs proxy ARP on the interface and sends replies
to other interfaces
- reply-only - the interface will only reply to requests originated from
matching IP address/MAC address combinations which are entered as static entries
in the ` ARP </wiki/Manual:IP/ARP>`_ table. No dynamic entries will be
automatically stored in the ARP table. Therefore for communications to be
successful, a valid static entry must already exist.



    auto_negotiation (optional, str, True)
      When enabled, the interface "advertises" its maximum capabilities to achieve the
best connection possible.
- Note1: Auto-negotiation should not be disabled on one end only, otherwise
Ethernet Interfaces may not work properly.
- Note2: Gigabit Ethernet and NBASE-T Ethernet links cannot work with
auto-negotiation disabled.



    bandwidth (optional, str, unlimited/unlimited)
      Sets max rx/tx bandwidth in kbps that will be handled by an interface. TX limit
is supported on all Atheros ` switch-chip </wiki/Manual:Switch_Chip_Features>`_
ports. RX limit is supported only on Atheros8327/QCA8337 switch-chip ports.



    cable_setting (optional, str, default)
      Changes the cable length setting (only applicable to NS DP83815/6 cards)



    combo_mode (optional, str, auto)
      When auto mode is selected, the port that was first connected will establish the
link. In case this link fails, the other port will try to establish a new link.
If both ports are connected at the same time (e.g. after reboot), the priority
will be the SFP/SFP+ port. When sfp mode is selected, the interface will only
work through SFP/SFP+ cage. When copper mode is selected, the interface will
only work through RJ45 Ethernet port.



    comment (optional, str, None)
      Descriptive name of an item



    disable_running_check (optional, str, True)
      Disable running check. If this value is set to no, the router automatically
detects whether the NIC is connected with a device in the network or not.
Default value is yes because older NICs do not support it. (only applicable to
x86)



    tx_flow_control (optional, str, False)
      When set to on, the port will generate pause frames to the upstream device to
temporarily stop the packet transmission. Pause frames are only generated when
some routers output interface is congested and packets cannot be transmitted
anymore. auto is the same as on except when auto-negotiation=yes flow control
status is resolved by taking into account what other end advertises.



    rx_flow_control (optional, str, False)
      When set to on, the port will process received pause frames and suspend
transmission if required. auto is the same as on except when
auto-negotiation=yes flow control status is resolved by taking into account what
other end advertises.



    full_duplex (optional, str, True)
      Defines whether the transmission of data appears in two directions
simultaneously, only applies when auto-negotiation is disabled.



    l2mtu (optional, int, None)
      Layer2 Maximum transmission unit. ` Read more&gt;&gt;
 </wiki/Maximum_Transmission_Unit_on_RouterBoards>`_



    mac_address (optional, str, None)
      Media Access Control number of an interface.



    master_port (optional, str, None)
      Outdated property, more details about this property can be found in the `
Master-port </wiki/Manual:Master-port>`_ page.



    mdix_enable (optional, str, True)
      Whether the MDI/X auto cross over cable correction feature is enabled for the
port (Hardware specific, e.g. ether1 on RB500 can be set to yes/no. Fixed to
yes on other hardware.)



    mtu (optional, str, 1500)
      Layer3 Maximum transmission unit



    name (True, str, None)
      Name of an interface



    poe_out (optional, str, False)
      Poe Out settings. ` Read more </wiki/Manual:PoE-Out>`_



    poe_priority (optional, int, None)
      Poe Out settings. ` Read more </wiki/Manual:PoE-Out>`_



    speed (optional, str, None)
      Sets interface data transmission speed which takes effect only when
auto-negotiation is disabled.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

