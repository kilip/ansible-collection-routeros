#!/usr/bin/python


"""
The module file for ros_ethernet
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_ethernet
short_description: Manage configuration for C(/interface ethernet)
description: This M(ros_ethernet) module provides management for RouterOS C(/interface ethernet).
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
    state:
        choices:
            - merged
            - replaced
            - overridden
            - deleted
        default: merged
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_ethernet) will update existing C(/interface ethernet) configuration
            -  When Resource Not Exists:
               *  M(ros_ethernet) will create new C(/interface ethernet),
    config:
        description: A dictionary for L(ros_ethernet)
        type: list
        elements: dict
        suboptions:
            advertise:
                type: list
                elements: str
                choices:
                    - 10m-full
                    - 10m-half
                    - 100m-full
                    - 100m-half
                    - 1000m-full
                    - 1000m-half
                    - 2500m-full
                    - 5000m-full
                    - 10000m-full
                default: None
                description: |
                    Advertised speed and duplex modes for Ethernet interfaces over twisted pair, only applies when auto-negotiation is enabled. Advertising higher speeds than the actual interface supported speed will have no effect, multiple options are allowed.
            arp:
                type: str
                default: enabled
                choices:
                    - disabled
                    - enabled
                    - local-proxy-arp
                    - proxy-arp
                    - reply-only
                description: |
                    Address Resolution Protocol mode:
                    - disabled - the interface will not use ARP
                    - enabled - the interface will use ARP
                    - local-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interface
                    - proxy-arp - the router performs proxy ARP on the interface and sends replies to other interfaces
                    - reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the L( ARP,/wiki/Manual:IP/ARP) table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
            auto_negotiation:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    When enabled, the interface "advertises" its maximum capabilities to achieve the best connection possible.
                    - Note1: Auto-negotiation should not be disabled on one end only, otherwise Ethernet Interfaces may not work properly.
                    - Note2: Gigabit Ethernet and NBASE-T Ethernet links cannot work with auto-negotiation disabled.
            bandwidth:
                type: str
                default: unlimited/unlimited
                description: |
                    Sets max rx/tx bandwidth in kbps that will be handled by an interface. TX limit is supported on all Atheros L( switch-chip,/wiki/Manual:Switch_Chip_Features) ports. RX limit is supported only on Atheros8327/QCA8337 switch-chip ports.
            cable_setting:
                type: str
                default: default
                choices:
                    - default
                    - short
                    - standard
                description: |
                    Changes the cable length setting (only applicable to NS DP83815/6 cards)
            combo_mode:
                type: str
                default: auto
                choices:
                    - auto
                    - copper
                    - sfp
                description: |
                    When auto mode is selected, the port that was first connected will establish the link. In case this link fails, the other port will try to establish a new link. If both ports are connected at the same time (e.g. after reboot), the priority will be the SFP/SFP+ port. When sfp mode is selected, the interface will only work through SFP/SFP+ cage. When copper mode is selected, the interface will only work through RJ45 Ethernet port.
            comment:
                type: str
                description: |
                    Descriptive name of an item
            disable_running_check:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Disable running check. If this value is set to no, the router automatically detects whether the NIC is connected with a device in the network or not. Default value is yes because older NICs do not support it. (only applicable to x86)
            tx_flow_control:
                type: str
                default: off
                choices:
                    - on
                    - off
                    - auto
                description: |
                    When set to on, the port will generate pause frames to the upstream device to temporarily stop the packet transmission. Pause frames are only generated when some routers output interface is congested and packets cannot be transmitted anymore. auto is the same as on except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises.
            rx_flow_control:
                type: str
                default: off
                choices:
                    - on
                    - off
                    - auto
                description: |
                    When set to on, the port will process received pause frames and suspend transmission if required. auto is the same as on except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises.
            full_duplex:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Defines whether the transmission of data appears in two directions simultaneously, only applies when auto-negotiation is disabled.
            l2mtu:
                type: int
                description: |
                    Layer2 Maximum transmission unit. L( Read more&gt;&gt; ,/wiki/Maximum_Transmission_Unit_on_RouterBoards)
            mac_address:
                type: str
                description: |
                    Media Access Control number of an interface.
            master_port:
                type: str
                description: |
                    Outdated property, more details about this property can be found in the L( Master-port,/wiki/Manual:Master-port) page.
            mdix_enable:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Whether the MDI/X auto cross over cable correction feature is enabled for the port (Hardware specific, e.g. ether1 on RB500 can be set to yes/no. Fixed to yes on other hardware.)
            mtu:
                type: str
                default: 1500
                description: |
                    Layer3 Maximum transmission unit
            name:
                type: str
                required: True
                description: |
                    Name of an interface
            poe_out:
                type: str
                default: off
                choices:
                    - auto-on
                    - forced-on
                    - off
                description: |
                    Poe Out settings. L( Read more,/wiki/Manual:PoE-Out)
            poe_priority:
                type: int
                description: |
                    Poe Out settings. L( Read more,/wiki/Manual:PoE-Out)
            speed:
                type: str
                choices:
                    - 10mbps
                    - 10gbps
                    - 100mbps
                    - 1gbps
                default: None
                description: |
                    Sets interface data transmission speed which takes effect only when auto-negotiation is disabled.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.interface.ethernet import EthernetResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=EthernetResource.argument_spec)
    result = ResourceConfig(module, EthernetResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
