from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class FirewallRawResource(ResourceBase):
    resource_name = "firewall_raw"
    command_root = "/ip firewall raw"
    related_resources = []
    gather_network_resources = ["firewall_raw"]
    resource_keys = ["name"]
    config_type = "plural"
    argument_spec = {
        "running_config": {"type": "str"},
        "state": {"choices": ["overridden"], "type": "str"},
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                "action": {
                    "type": "str",
                    "choices": [
                        "accept",
                        "add-dst-to-address-list",
                        "add-src-to-address-list",
                        "drop",
                        "jump",
                        "log",
                        "no-track",
                        "passthrough",
                        "return",
                    ],
                    "default": "accept",
                },
                "out_interface": {"type": "str"},
                "per_connection_classifier": {"type": "str"},
                "address_list": {"type": "str"},
                "address_list_timeout": {
                    "type": "str",
                    "choices": ["none-dynamic", "none-static", "time"],
                    "default": "none-dynamic",
                },
                "chain": {"type": "str"},
                "comment": {"type": "str"},
                "dscp": {"type": "int"},
                "dst_address": {"type": "str"},
                "dst_address_list": {"type": "str"},
                "dst_address_type": {
                    "type": "str",
                    "choices": ["unicast", "local", "broadcast", "multicast"],
                    "default": None,
                },
                "dst_limit": {"type": "int"},
                "dst_port": {"type": "int"},
                "fragment": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": None,
                },
                "hotspot": {
                    "type": "str",
                    "choices": [
                        "auth",
                        "from-client",
                        "http",
                        "local-dst",
                        "to-client",
                    ],
                    "default": None,
                },
                "icmp_options": {"type": "int"},
                "in_bridge_port": {"type": "str"},
                "in_interface": {"type": "str"},
                "in_interface_list": {"type": "str"},
                "ingress_priority": {"type": "int"},
                "ipsec_policy": {
                    "type": "str",
                    "choices": ["in", "ipsec", "none"],
                    "default": None,
                },
                "ipv4_options": {
                    "type": "str",
                    "choices": [
                        "any",
                        "loose-source-routing",
                        "no-record-route",
                        "no-router-alert",
                        "no-source-routing",
                        "no-timestamp",
                        "none",
                        "record-route",
                        "router-alert",
                        "strict-source-routing",
                        "timestamp",
                    ],
                    "default": None,
                },
                "jump_target": {"type": "str"},
                "limit": {"type": "int"},
                "log": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": None,
                },
                "log_prefix": {"type": "str"},
                "nth": {"type": "int"},
                "out_bridge_port": {"type": "str"},
                "out_interface_list": {"type": "str"},
                "packet_size": {"type": "int"},
                "port": {"type": "int"},
                "priority": {"type": "int"},
                "protocol": {"type": "str", "default": "tcp"},
                "psd": {"type": "int"},
                "random": {"type": "int"},
                "src_address": {"type": "str"},
                "src_address_list": {"type": "str"},
                "src_address_type": {
                    "type": "str",
                    "choices": ["unicast", "local", "broadcast", "multicast"],
                    "default": None,
                },
                "src_port": {"type": "int"},
                "src_mac_address": {"type": "str"},
                "tcp_flags": {
                    "type": "str",
                    "choices": [
                        "ack",
                        "cwr",
                        "ece",
                        "fin",
                        "psh",
                        "rst",
                        "syn",
                        "urg",
                    ],
                    "default": None,
                },
                "tcp_mss": {"type": "int"},
                "tls_host": {"type": "str"},
                "ttl": {"type": "int"},
            },
        },
    }
