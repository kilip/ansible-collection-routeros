from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class DhcpLeaseResource(ResourceBase):
    resource_name = "dhcp_lease"
    command_root = "/ip dhcp-server lease"
    related_resources = []
    gather_network_resources = ["dhcp_lease"]
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
                "insert_queue_before": {"type": "str"},
                "address": {"type": "str"},
                "address_list": {"type": "str"},
                "allow_dual_stack_queue": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "always_broadcast": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": None,
                },
                "block_access": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "client_id": {"type": "str"},
                "dhcp_option": {"type": "str"},
                "dhcp_option_set": {"type": "str"},
                "lease_time": {"type": "str", "default": "0s"},
                "mac_address": {"type": "str", "default": "00:00:00:00:00:00"},
                "rate_limit": {"type": "int"},
                "server": {"type": "str"},
                "use_src_mac": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "comment": {"type": "str"},
            },
        },
    }
