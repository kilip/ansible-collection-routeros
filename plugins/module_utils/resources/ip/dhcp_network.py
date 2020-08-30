from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class DhcpNetworkResource(ResourceBase):
    resource_name = "dhcp_network"
    command_root = "/ip dhcp-server network"
    related_resources = []
    gather_network_resources = ["dhcp_network"]
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
                "address": {"type": "str"},
                "boot_file_name": {"type": "str"},
                "caps_manager": {"type": "str"},
                "dhcp_option": {"type": "str"},
                "dhcp_option_set": {"type": "str"},
                "dns_none": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "dns_server": {"type": "str"},
                "domain": {"type": "str"},
                "gateway": {"type": "str", "default": "0.0.0.0"},
                "netmask": {"type": "str"},
                "next_server": {"type": "str"},
                "ntp_server": {"type": "str"},
                "wins_server": {"type": "str"},
                "comment": {"type": "str"},
            },
        },
    }
