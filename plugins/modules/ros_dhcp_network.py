#!/usr/bin/python


"""
The module file for ros_dhcp_network
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_dhcp_network
short_description: Manage configuration for C(/ip dhcp-server network)
description: This M(ros_dhcp_network) module provides management for RouterOS C(/ip dhcp-server network).
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
               *  M(ros_dhcp_network) will update existing C(/ip dhcp-server network) configuration
            -  When Resource Not Exists:
               *  M(ros_dhcp_network) will create new C(/ip dhcp-server network),
            Replaced
            -  When Resource Exists:
               *  M(ros_dhcp_network) will restore related C(/ip dhcp-server network) to its default value.
               *  M(ros_dhcp_network) will update C(/ip dhcp-server network) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_dhcp_network) will create new C(/ip dhcp-server network)
            Overridden:
            *  M(ros_dhcp_network) will remove any existing item in C(/ip dhcp-server network)
            *  M(ros_dhcp_network) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_dhcp_network) will remove that item from C(/ip dhcp-server network) configuration
    config:
        description: A dictionary for L(ros_dhcp_network)
        type: list
        elements: dict
        suboptions:
            address:
                type: str
                description: |
                    the network DHCP server(s) will lease addresses from
            boot_file_name:
                type: str
                description: |
                    Boot file name
            caps_manager:
                type: str
                description: |
                    Comma-separated list of IP addresses for one or more CAPsMAN system managers. DHCP Option 138 (capwap) will be used.
            dhcp_option:
                type: str
                description: |
                    Add additional DHCP options from L( option list,#Options).
            dhcp_option_set:
                type: str
                description: |
                    Add additional set of DHCP options.
            dns_none:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    If set, then DHCP Server will not pass dynamic DNS servers configured on the router to the DHCP clients if no DNS Server in dns-server is set. By default if there are no DNS Servers configured, then the dynamic DNS Servers will be passed to DHCP clients.
            dns_server:
                type: str
                description: |
                    the DHCP client will use these as the default DNS servers. Two comma-separated DNS servers can be specified to be used by the DHCP client as primary and secondary DNS servers
            domain:
                type: str
                description: |
                    The DHCP client will use this as the DNS domain setting for the network adapter.
            gateway:
                type: str
                default: 0.0.0.0
                description: |
                    The default gateway to be used by L(DHCP Client,/wiki/DHCP_Client).
            netmask:
                type: str
                description: |
                    The actual network mask to be used by DHCP client. If set to 0 - netmask from network address will be used.
            next_server:
                type: str
                description: |
                    IP address of next server to use in bootstrap.
            ntp_server:
                type: str
                description: |
                    the DHCP client will use these as the default NTP servers. Two comma-separated NTP servers can be specified to be used by the DHCP client as primary and secondary NTP servers
            wins_server:
                type: str
                description: |
                    The Windows DHCP client will use these as the default WINS servers. Two comma-separated WINS servers can be specified to be used by the DHCP client as primary and secondary WINS servers

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.ip.dhcp_network import DhcpNetworkResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=DhcpNetworkResource.argument_spec)
    result = ResourceConfig(module, DhcpNetworkResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
