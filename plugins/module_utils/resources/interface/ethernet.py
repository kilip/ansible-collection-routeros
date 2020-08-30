from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class EthernetResource(ResourceBase):
    resource_name = "ethernet"
    command_root = "/interface ethernet"
    related_resources = []
    gather_network_resources = ["ethernet"]
    resource_keys = ["name"]
    config_type = "plural"
    argument_spec = {
        "running_config": {"type": "str"},
        "state": {"choices": ["merged"], "default": "merged", "type": "str"},
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                "advertise": {
                    "type": "list",
                    "elements": "str",
                    "choices": [
                        "10m-full",
                        "10m-half",
                        "100m-full",
                        "100m-half",
                        "1000m-full",
                        "1000m-half",
                        "2500m-full",
                        "5000m-full",
                        "10000m-full",
                    ],
                    "default": None,
                },
                "arp": {
                    "type": "str",
                    "choices": [
                        "disabled",
                        "enabled",
                        "local-proxy-arp",
                        "proxy-arp",
                        "reply-only",
                    ],
                    "default": "enabled",
                },
                "auto_negotiation": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "bandwidth": {"type": "str", "default": "unlimited/unlimited"},
                "cable_setting": {
                    "type": "str",
                    "choices": ["default", "short", "standard"],
                    "default": "default",
                },
                "combo_mode": {
                    "type": "str",
                    "choices": ["auto", "copper", "sfp"],
                    "default": "auto",
                },
                "comment": {"type": "str"},
                "disable_running_check": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "tx_flow_control": {
                    "type": "str",
                    "choices": ["on", "off", "auto"],
                    "default": "off",
                },
                "rx_flow_control": {
                    "type": "str",
                    "choices": ["on", "off", "auto"],
                    "default": "off",
                },
                "full_duplex": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "l2mtu": {"type": "int"},
                "mac_address": {"type": "str"},
                "master_port": {"type": "str"},
                "mdix_enable": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": "yes",
                },
                "mtu": {"type": "str", "default": "1500"},
                "name": {"type": "str", "required": True},
                "poe_out": {
                    "type": "str",
                    "choices": ["auto-on", "forced-on", "off"],
                    "default": "off",
                },
                "poe_priority": {"type": "int"},
                "speed": {
                    "type": "str",
                    "choices": ["10mbps", "10gbps", "100mbps", "1gbps"],
                    "default": None,
                },
            },
        },
    }
