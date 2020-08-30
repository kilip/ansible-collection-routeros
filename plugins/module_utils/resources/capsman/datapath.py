from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class CapsmanDatapathResource(ResourceBase):
    resource_name = "capsman_datapath"
    command_root = "/caps-man datapath"
    related_resources = []
    gather_network_resources = ["capsman_datapath"]
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
                "name": {"type": "str"},
                "comment": {"type": "str"},
                "arp": {
                    "type": "str",
                    "choices": [
                        "disabled",
                        "enabled",
                        "proxy-arp",
                        "reply-only",
                    ],
                    "default": "enabled",
                },
                "bridge": {"type": "str"},
                "bridge_cost": {"type": "int"},
                "bridge_horizon": {"type": "int"},
                "client_to_client_forwarding": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "interface_list": {"type": "str"},
                "l2mtu": {"type": "str"},
                "local_forwarding": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "mtu": {"type": "str"},
                "openflow_switch": {"type": "str"},
                "vlan_id": {"type": "int"},
                "vlan_mode": {
                    "type": "str",
                    "choices": ["use-service-tag", "use-tag"],
                },
            },
        },
    }
