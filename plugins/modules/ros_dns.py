#!/usr/bin/python


"""
The module file for ros_dns
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_dns
short_description: Manage configuration for C(/ip dns)
description: This M(ros_dns) module provides management for RouterOS C(/ip dns).
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
short_documentation: DNS Cache Configuration
options:
    state:
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_dns) will update existing C(/ip dns) configuration
            -  When Resource Not Exists:
               *  M(ros_dns) will create new C(/ip dns),
            Replaced
            -  When Resource Exists:
               *  M(ros_dns) will restore related C(/ip dns) to its default value.
               *  M(ros_dns) will update C(/ip dns) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_dns) will create new C(/ip dns)
            Overridden:
            *  M(ros_dns) will remove any existing item in C(/ip dns)
            *  M(ros_dns) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_dns) will remove that item from C(/ip dns) configuration
    config:
        description: A dictionary for L(ros_dns)
        suboptions:
            allow_remote_requests:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Specifies whether to allow network requests
            cache_max_ttl:
                type: str
                default: 1w
                description: |
                    Maximum time-to-live for cache records. In other words, cache records will
                    expire unconditionally after cache-max-ttl time. Shorter TTL received from DNS
                    servers are respected.
            cache_size:
                type: str
                default: 2048
                description: |
                    Specifies the size of DNS cache in KiB
            max_concurrent_queries:
                type: str
                default: 100
                description: |
                    Specifies how much concurrent queries are allowed
            max_concurrent_tcp_sessions:
                type: str
                default: 20
                description: |
                    Specifies how much concurrent TCP sessions are allowed
            max_udp_packet_size:
                type: str
                default: 4096
                description: |
                    Maximum size of allowed UDP packet.
            query_server_timeout:
                type: str
                default: 2s
                description: |
                    Specifies how long to wait for query response from one server
            query_total_timeout:
                type: str
                default: 10s
                description: |
                    Specifies how long to wait for query response in total. Note that this setting
                    must be configured taking into account query-server-timeout and number of used
                    DNS server.
            servers:
                type: str
                description: |
                    List of DNS server IPv4/IPv6 addresses
config:
    type: list
state:
    choices:
        - present
        - reset
    default: present

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.ip.dns import DnsResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=DnsResource.argument_spec)
    result = Config(module, DnsResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
