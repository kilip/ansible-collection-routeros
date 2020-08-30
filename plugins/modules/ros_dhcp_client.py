#!/usr/bin/python


"""
The module file for ros_dhcp_client
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_dhcp_client
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
        description:
            - I(merged) M(ros_dhcp_client) will update existing C(/ip dhcp-client) configuration, or create new C(/ip dhcp-client) when resource not found
            - I(replaced) M(ros_dhcp_client) will restore existing C(/ip dhcp-client) configuration to its default value, then update existing resource with the new configuration. If the resource C(/ip dhcp-client) not found, M(ros_dhcp_client) will create resource in C(/ip dhcp-client)
            - I(overridden) M(ros_dhcp_client) will remove any resource in C(/ip dhcp-client) first, and then create new C(/ip dhcp-client) resources.
            - I(deleted) M({module}) when found module will delete C(/ip dhcp-client)
    config:
        description: A dictionary for L(ros_dhcp_client)
        type: list
        elements: dict
        suboptions:
            add_default_route:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                    - special-classless
                description: |
                    Whether to install default route in routing table received from dhcp server. By default RouterOS client complies to RFC and ignores option 3 if classless option 121 is received. To force client not to ignore option 3 set special-classless. This parameter is available in v6rc12+
                    - yes - adds classless route if received, if not then add default route (old behavior)
                    - special-classless - adds both classless route if received and default route (MS style)
            client_id:
                type: str
                description: |
                    Corresponds to the settings suggested by the network administrator or ISP. If not specified, clients MAC address will be sent
            comment:
                type: str
                description: |
                    Short description of the client
            default_route_distance:
                type: int
                description: |
                    Distance of default route. Applicable if C(add-default-route) is set to C(yes).
            disabled:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
            host_name:
                type: str
                description: |
                    Host name of the client sent to a DHCP server. If not specified, clients system identity will be used.
            interface:
                type: str
                description: |
                    Interface on which DHCP client will be running.
            script:
                type: str
                description: |
                    Execute script on status change. This parameter is available in v6.39rc33+ These are available variables that are accessible for the event script:
                    - bound - 1 - lease is added/changed; 0 - lease is removed
                    - server-address - server address
                    - lease-address - lease address provided by server
                    - interface - name of interface on which client is configured
                    - gateway-address - gateway address provided by server
                    - vendor-specific - stores value of option 43 received from DHCP server
                    - lease-options - array of received options
                    L( C(Example >>),/wiki/Manual:IP/DHCP_Client#Lease_script_example)
            use_peer_dns:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Whether to accept the L( DNS,/wiki/Manual:IP/DNS). (Will override the settings put in the C(/ip dns) submenu.
            use_peer_ntp:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Whether to accept the L( NTP,/wiki/Manual:System/Time#NTP_client_and_server). (Will override the settings put in the C(/system ntp client) submenu)

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.ip.dhcp_client import DhcpClientResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=DhcpClientResource.argument_spec)
    result = ResourceConfig(module, DhcpClientResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
