#!/usr/bin/python


"""
The module file for ros_pppoe_server
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_pppoe_server
short_description: Manage configuration for C(/interface pppoe-server)
description: This M(ros_pppoe_server) module provides management for RouterOS C(/interface pppoe-server).
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
               *  M(ros_pppoe_server) will update existing C(/interface pppoe-server) configuration
            -  When Resource Not Exists:
               *  M(ros_pppoe_server) will create new C(/interface pppoe-server),
            Replaced
            -  When Resource Exists:
               *  M(ros_pppoe_server) will restore related C(/interface pppoe-server) to its default value.
               *  M(ros_pppoe_server) will update C(/interface pppoe-server) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_pppoe_server) will create new C(/interface pppoe-server)
            Overridden:
            *  M(ros_pppoe_server) will remove any existing item in C(/interface pppoe-server)
            *  M(ros_pppoe_server) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_pppoe_server) will remove that item from C(/interface pppoe-server) configuration
    config:
        description: A dictionary for L(ros_pppoe_server)
        type: list
        elements: dict
        suboptions:
            authentication:
                type: list
                elements: str
                choices:
                    - mschap2
                    - mschap1
                    - chap
                    - pap
                default: None
                description: |
                    Authentication algorithm
            default_profile:
                type: str
                default: default
                description: |
                    Default [ user profile](/wiki/PPP_AAA#User_Profiles "PPP
                    AAA") to use
            interface:
                type: str
                description: |
                    Interface that the clients are connected to
            keepalive_timeout:
                type: str
                default: 10
                description: |
                    Defines the time period (in seconds) after which the router is starting to send keepalive packets every second. If there is no traffic and no keepalive responses arrive for that period of time (i.e. 2  keepalive-timeout), the non responding client is proclaimed disconnected.
            max_mru:
                type: str
                default: 1480
                description: |
                    Maximum Receive Unit. The optimal value is the MTU of the interface the tunnel is working over reduced by 20 (so, for 1500-byte Ethernet link, set the MTU to 1480 to avoid fragmentation of packets)
            max_mtu:
                type: str
                default: 1480
                description: |
                    Maximum Transmission Unit. The optimal value is the MTU of the interface the tunnel is working over reduced by 20 (so, for 1500-byte Ethernet link, set the MTU to 1480 to avoid fragmentation of packets)
            max_sessions:
                type: str
                description: |
                    Maximum number of clients that the AC can serve. 0 = no limitations.
            mrru:
                type: str
                ignore: true
                default: disabled
                description: |
                    Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it will be split into multiple packets, allowing full size IP or Ethernet packets to be sent over the tunnel. C(<a href="/wiki/Manual:MLPPP_over_single_and_multiple_links" title="Manual:MLPPP over single and multiple links"> Read more >></a>)
            one_session_per_host:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Allow only one session per host (determined by MAC address). If a host tries to establish a new session, the old one will be closed.
            service_name:
                type: str
                description: |
                    The PPPoE service name. Server will accept clients which sends PADI message with service-names that matches this setting or if service-name field in PADI message is not set.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.interface.pppoe_server import PppoeServerResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=PppoeServerResource.argument_spec)
    result = ResourceConfig(module, PppoeServerResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
