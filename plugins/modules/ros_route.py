#!/usr/bin/python


"""
The module file for ros_route
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_route
short_description: Manage configuration for C(/ip route)
description: This M(ros_route) module provides management for RouterOS C(/ip route).
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
               *  M(ros_route) will update existing C(/ip route) configuration
            -  When Resource Not Exists:
               *  M(ros_route) will create new C(/ip route),
            Replaced
            -  When Resource Exists:
               *  M(ros_route) will restore related C(/ip route) to its default value.
               *  M(ros_route) will update C(/ip route) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_route) will create new C(/ip route)
            Overridden:
            *  M(ros_route) will remove any existing item in C(/ip route)
            *  M(ros_route) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_route) will remove that item from C(/ip route) configuration
    config:
        description: A dictionary for L(ros_route)
        type: list
        elements: dict
        suboptions:
            check_gateway:
                type: str
                choices:
                    - arp
                    - ping
                default: None
                description: |
                    Periodically (every 10 seconds) check gateway by sending either ICMP echo request (ping) or ARP request (arp). If no response from gateway is received for 10 seconds, request times out. After two timeouts gateway is considered unreachable. After receiving reply from gateway it is considered reachable and timeout counter is reset.
            comment:
                type: str
                description: |
                    Description of particular route
            distance:
                type: str
                default: 1
                description: |
                    Value used in L(route selection,#Route_selection). Routes with smaller distance value are given preference. If value of this property is not set, then the default depends on route protocol:
                    - connected routes: 0
                    - static routes: 1
                    - eBGP: 20
                    - OSPF: 110
                    - RIP: 120
                    - MME: 130
                    - iBGP: 200
            dst_address:
                type: str
                default: 0.0.0.0/0
                description: |
                    IP prefix of route, specifies destination addresses that this route can be used for. Netmask part of this property specifies how many of the most significant bits in packet destination address must match this value. If there are several active routes that match destination address of packet, then the most specific one (with largest netmask value) is used.
            gateway:
                type: str
                ignore: true
                description: |
                    Array of IP addresses or interface names. Specifies which host or interface packets should be sent to. L(Connected routes,#Connected_routes) and routes with blackhole, unreachable or prohibit type do not have this property. Usually value of this property is a single IP address of a gateway that can be directly reached through one of routers interfaces (but see L(nexthop lookup,#Nexthop_lookup)). L(ECMP,#ECMP) routes have more than one gateway value. Value can be repeated several times.
            pref_src:
                type: str
                description: |
                    Which of the local IP addresses to use for locally originated packets that are sent via this route. Value of this property has no effect on forwarded packets. If value of this property is set to IP address that is not local address of this router then the route will be inactive. If pref-src value is not set, then for locally originated packets that are sent using this route router will choose one of local addresses attached to the output interface that match destination prefix of the route (L(an example,#Route_lookup_example)).
            route_tag:
                type: int
                description: |
                    Value of route tag attribute for RIP or OSPF. For RIP only values 0..4294967295 are valid.
            routing_mark:
                type: str
                description: |
                    Name of routing table that contains this route. Not set by default which is the same as main. Packets that are marked by L(firewall,/wiki/Manual:IP/Firewall). Not more than 251 routing marks can be added per router.
            scope:
                type: str
                default: 30
                description: |
                    Used in nexthop resolution. Route can resolve nexthop only through routes that have scope less than or equal to the target-scope of this route. Default value depends on route protocol:
                    - connected routes: 10 (if interface is running)
                    - OSPF, RIP, MME routes: 20
                    - static routes: 30
                    - BGP routes: 40
                    - connected routes: 200 (if interface is not running)
            target_scope:
                type: str
                default: 10
                description: |
                    Used in nexthop resolution. This is the maximum value of scope for a route through which a nexthop of this route can be resolved. See L(nexthop lookup,#Nexthop_lookup). For iBGP value is set to 30 by default.
            type:
                type: str
                default: unicast
                choices:
                    - unicast
                    - blackhole
                    - prohibit
                    - unreachable
                description: |
                    Routes that do not specify nexthop for packets, but instead perform some other action on packets have type different from the usual unicast. blackhole route silently discards packets, while unreachable and prohibit routes send ICMP Destination Unreachable message (code 1 and 13 respectively) to the source address of the packet.
            vrf_interface:
                type: str
                default: 10
                description: |
                    VRF interface name

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.ip.route import RouteResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=RouteResource.argument_spec)
    result = ResourceConfig(module, RouteResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
