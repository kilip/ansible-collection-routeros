from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class DhcpServerResource(ResourceBase):
    resource_name = "dhcp_server"
    command_root = "/ip dhcp-server"
    related_resources = []
    gather_network_resources = ["dhcp_server"]
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
                "comment": {"type": "str"},
                "address_pool": {"type": "str"},
                "bootp_lease_time": {"type": "str"},
                "delay_threshold": {"type": "str"},
                "dhcp_option_set": {"type": "str"},
                "parent_queue": {"type": "str"},
                "insert_queue_before": {"type": "str"},
                "client_mac_limit": {"type": "str"},
                "add_arp": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "allow_dual_stack_queue": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "always_broadcast": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "authoritative": {
                    "type": "str",
                    "choices": [
                        "after-10sec-delay",
                        "after-2sec-delay",
                        "yes",
                        "no",
                    ],
                    "default": "yes",
                },
                "bootp_support": {
                    "type": "str",
                    "choices": ["none", "static", "dynamic"],
                    "default": "static",
                },
                "conflict_detection": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": None,
                },
                "interface": {"type": "str"},
                "lease_script": {"type": "str"},
                "lease_time": {"type": "str", "default": "10m"},
                "name": {"type": "str", "required": True},
                "relay": {"type": "str", "default": "0.0.0.0"},
                "src_address": {"type": "str", "default": "0.0.0.0"},
                "use_framed_as_classless": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "use_radius": {
                    "type": "str",
                    "choices": ["yes", "no", "accounting"],
                    "default": "no",
                },
            },
        },
    }
