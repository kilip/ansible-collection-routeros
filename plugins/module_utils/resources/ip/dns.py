from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class DnsResource(ResourceBase):
    """
    Class Dns contains definition for `/ip dns`
    """

    resource_name = "dns"
    command_root = "/ip dns"
    gather_network_resources = ["dns"]
    resource_keys = ["name"]
    config_type = "singular"
    argument_spec = {
        "running_config": {"type": "str"},
        "state": {
            "choices": ["present", "reset"],
            "default": "present",
            "type": "str",
        },
        "config": {
            "type": "dict",
            "options": {
                "allow_remote_requests": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "cache_max_ttl": {"type": "str", "default": "1w"},
                "cache_size": {"type": "str", "default": "2048"},
                "max_concurrent_queries": {"type": "str", "default": "100"},
                "max_concurrent_tcp_sessions": {
                    "type": "str",
                    "default": "20",
                },
                "max_udp_packet_size": {"type": "str", "default": "4096"},
                "query_server_timeout": {"type": "str", "default": "2s"},
                "query_total_timeout": {"type": "str", "default": "10s"},
                "servers": {"type": "str"},
                "comment": {"type": "str"},
            },
        },
    }
