#!/usr/bin/python


"""
The module file for ros_dhcp_lease
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_dhcp_lease
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
            - I(merged) M(ros_dhcp_lease) will update existing C(/ip dhcp-server lease) configuration, or create new C(/ip dhcp-server lease) when resource not found
            - I(replaced) M(ros_dhcp_lease) will restore existing C(/ip dhcp-server lease) configuration to its default value, then update existing resource with the new configuration. If the resource C(/ip dhcp-server lease) not found, M(ros_dhcp_lease) will create resource in C(/ip dhcp-server lease)
            - I(overridden) M(ros_dhcp_lease) will remove any resource in C(/ip dhcp-server lease) first, and then create new C(/ip dhcp-server lease) resources.
            - I(deleted) M({module}) when found module will delete C(/ip dhcp-server lease)
    config:
        description: A dictionary for L(ros_dhcp_lease)
        type: list
        elements: dict
        suboptions:
            address:
                type: str
                description: |
                    Specify IP address (or ip pool) for static lease. If set to 0.0.0.0 - pool from server will be used
            address_list:
                type: str
                description: |
                    Address list to which address will be added if lease is bound.
            allow_dual_stack_queue:
                type: str
                default: yes
                choices:
                    - yes
                    - no
                description: |
                    Creates a single simple queue entry for both IPv4 and IPv6 addresses, uses the MAC address and DUID for identification. Requires L( IPv6 DHCP Server,/wiki/Manual:IPv6/DHCP_Server) to have this option enabled as well to work properly.
            always_broadcast:
                type: str
                choices:
                    - yes
                    - no
                default: None
                description: |
                    Send all replies as broadcasts
            block_access:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Block access for this client
            client_id:
                type: str
                description: |
                    If specified, must match DHCP client identifier option of the request
            dhcp_option:
                type: str
                description: |
                    Add additional DHCP options from L( option list,#Options).
            dhcp_option_set:
                type: str
                description: |
                    Add additional set of DHCP options.
            insert_queue_before:
                type: str
                ignore: true
                description: |
                    Specify where to place dynamic simple queue entries for static DCHP leases with rate-limit parameter set.
            lease_time:
                type: str
                default: 0s
                description: |
                    Time that the client may use the address. If set to 0s lease will never expire.
            mac_address:
                type: str
                default: 00:00:00:00:00:00
                description: |
                    If specified, must match the MAC address of the client
            rate_limit:
                type: int
                description: |
                    Adds a dynamic simple queue to limit IPs bandwidth to a specified rate. Requires the lease to be static. Format is: rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]]. All rates should be numbers with optional k (1,000s) or M (1,000,000s). If tx-rate is not specified, rx-rate is as tx-rate too. Same goes for tx-burst-rate and tx-burst-threshold and tx-burst-time. If both rx-burst-threshold and tx-burst-threshold are not specified (but burst-rate is specified), rx-rate and tx-rate is used as burst thresholds. If both rx-burst-time and tx-burst-time are not specified, 1s is used as default.
            server:
                type: str
                description: |
                    Server name which serves this client
            use_src_mac:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    When this option is set server uses source MAC address instead of received CHADDR to assign address.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.ip.dhcp_lease import DhcpLeaseResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=DhcpLeaseResource.argument_spec)
    result = ResourceConfig(module, DhcpLeaseResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
