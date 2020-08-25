from __future__ import absolute_import, division, print_function

__metaclass__ = type

SPEC_GENERAL = {
    "bridge": {"type": "str", "required": True},
    "interface": {"type": "str", "required": True},
    "comment": {"type": "str"},
    "disabled": {"type": "bool"},
    "horizon": {"type": "int"},
    "learn": {
        "choices": ["auto","yes","no"],
        "type": "str"
    },
    "unknown_multicast_flood": {"type": "bool"},
    "unknown_unicast_flood": {"type": "bool"},
    "broadcast_flood": {"type": "bool"},
    "trusted": {"type": "bool"},
    "hw": {"type": "bool"},
    "fast_leave": {"type": "bool"},
    "place_before": {"type": "int"},
    "multicast_router": {
        "choices": [
            "disabled",
            "permanent",
            "temporary-query"
        ]
    },
}

SPEC_STP = {
    "stp": {
        "type": "dict",
        "options": {
            "priority": {"type": "int"},
            "path_cost": {"type": "int"},
            "internal_path_cost": {"type": "int"},
            "edge": {
                "choices": ["auto", "no", "no-discover", "yes", "yes-discover"],
                "type": "str"
            },
            "point_to_point": {
                "choices": ["auto", "no", "yes"]
            },
            "auto_isolate": {"type": "bool"},
            "restricted_role": {"type": "bool"},
            "restricted_tcn": {"type": "bool"},
            "bpdu_guard": {"type": "bool"},
            "copy_from": {"type": "bool"},
        }
    }
}

SPEC_VLAN = {
    "vlan": {
        "type": "dict",
        "options": {
            "pvid": {"type": "int"},
            "frame_types": {
                "choices": [
                    "admit-all",
                    "admit-only-untagged-and-priority-tagged",
                    "admit-only-vlan-tagged"
                ]
            },
            "ingress_filtering": {"type": "bool"},
            "tag_stacking": {"type": "bool"},
        }
    }
}


class BridgePortsArgs(object):
    argument_spec = {
        "config": {
            "element": "dict",
            "type": "list",
        },
        "options": {},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
            ],
            "type": "str",
            "default": "merged"
        }
    }

    def __init__(self, **kwargs):
        options = dict()
        options.update(SPEC_GENERAL)
        options.update(SPEC_STP)
        options.update(SPEC_VLAN)
        self.argument_spec["config"]["options"] = options