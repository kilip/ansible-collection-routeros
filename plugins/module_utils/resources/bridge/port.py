from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class BridgePortResource(ResourceBase):
    resource_name = "bridge_port"
    command_root = "/interface bridge port"
    related_resources = []
    gather_network_resources = ["bridge_port"]
    resource_keys = ["bridge", "interface"]
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
                "auto_isolate": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "bpdu_guard": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "bridge": {"type": "str", "required": True},
                "broadcast_flood": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "edge": {
                    "type": "str",
                    "choices": [
                        "auto",
                        "no",
                        "no-discover",
                        "yes",
                        "yes-discover",
                    ],
                    "default": "auto",
                },
                "external_fdb": {
                    "type": "str",
                    "choices": ["auto", "no", "yes"],
                    "default": "auto",
                },
                "fast_leave": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "frame_types": {
                    "type": "str",
                    "choices": [
                        "admit-all",
                        "admit-only-untagged-and-priority-tagged",
                        "admit-only-vlan-tagged",
                    ],
                    "default": "admit-all",
                },
                "ingress_filtering": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "learn": {
                    "type": "str",
                    "choices": ["auto", "no", "yes"],
                    "default": "auto",
                },
                "multicast_router": {
                    "type": "str",
                    "choices": ["disabled", "permanent", "temporary-query"],
                    "default": "temporary-query",
                },
                "horizon": {"type": "int"},
                "internal_path_cost": {"type": "str", "default": "10"},
                "interface": {"type": "str", "required": True},
                "path_cost": {"type": "str", "default": "10"},
                "point_to_point": {
                    "type": "str",
                    "choices": ["auto", "yes", "no"],
                    "default": "auto",
                },
                "priority": {"type": "str", "default": "128"},
                "pvid": {"type": "str", "default": "1"},
                "restricted_role": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "restricted_tcn": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "tag_stacking": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "trusted": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "no",
                },
                "unknown_multicast_flood": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "unknown_unicast_flood": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "comment": {"type": "str"},
            },
        },
    }
