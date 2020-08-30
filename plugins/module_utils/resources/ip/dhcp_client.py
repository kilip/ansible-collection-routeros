from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class DhcpClientResource(ResourceBase):
    resource_name = "dhcp_client"
    command_root = "/ip dhcp-client"
    related_resources = []
    gather_network_resources = ["dhcp_client"]
    resource_keys = ["name"]
    config_type = "plural"
    argument_spec = {
        "running_config": {"type": "str"},
        "state": {
            "choices": ["merged", "replaced", "deleted", "overridden"],
            "default": "merged",
            "type": "str",
        },
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                "add_default_route": {
                    "type": "str",
                    "choices": ["yes", "no", "special-classless"],
                    "default": "yes",
                },
                "client_id": {"type": "str"},
                "comment": {"type": "str"},
                "default_route_distance": {"type": "int"},
                "disabled": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "host_name": {"type": "str"},
                "interface": {"type": "str"},
                "script": {"type": "str"},
                "use_peer_dns": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "use_peer_ntp": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
            },
        },
    }
