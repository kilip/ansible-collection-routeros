from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..base import ResourceBase


class FirewallNatResource(ResourceBase):
    resource_name = "firewall_nat"
    command_root = "/ip firewall nat"
    related_resources = []
    gather_network_resources = ["firewall_nat"]
    resource_keys = ["name"]
    config_type = "plural"
    argument_spec = {
        "running_config": {"type": "str"},
        "state": {"choices": ["overridden"], "type": "str"},
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                "chain": {
                    "type": "str",
                    "required": True,
                    "choices": ["dstnat", "srcnat"],
                },
                "out_interface": {"type": "str"},
                "action": {
                    "type": "str",
                    "choices": [
                        "accept",
                        "add-dst-to-address-list",
                        "add-src-to-address-list",
                        "drop",
                        "fasttrack-connection",
                        "jump",
                        "log",
                        "passthrough",
                        "reject",
                        "return",
                        "tarpit",
                    ],
                    "default": "accept",
                },
                "address_list": {"type": "str"},
                "address_list_timeout": {
                    "type": "str",
                    "choices": ["none-dynamic", "none-static", "time"],
                    "default": "none-dynamic",
                },
                "comment": {"type": "str"},
                "connection_bytes": {"type": "int"},
                "connection_limit": {"type": "int"},
                "connection_mark": {
                    "type": "str",
                    "choices": ["no-mark", "string"],
                    "default": None,
                },
                "connection_rate": {"type": "int"},
                "connection_type": {
                    "type": "str",
                    "choices": [
                        "ftp",
                        "h323",
                        "irc",
                        "pptp",
                        "quake3",
                        "sip",
                        "tftp",
                    ],
                    "default": None,
                },
                "content": {"type": "str"},
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
                "layer7_protocol": {"type": "str"},
                "limit": {"type": "int"},
                "log_prefix": {"type": "str"},
                "nth": {"type": "int"},
                "out_bridge_port": {"type": "str"},
                "packet_mark": {
                    "type": "str",
                    "choices": ["no-mark", "string"],
                    "default": None,
                },
                "packet_size": {"type": "int"},
                "per_connection_classifier": {"type": "str"},
                "port": {"type": "int"},
                "protocol": {"type": "str", "default": "tcp"},
                "psd": {"type": "int"},
                "random": {"type": "int"},
                "routing_mark": {"type": "str"},
                "same_not_by_dst": {
                    "type": "str",
                    "choices": ["yes", "no"],
                    "default": None,
                },
                "src_address": {"type": "str"},
                "src_address_list": {"type": "str"},
                "src_address_type": {
                    "type": "str",
                    "choices": ["unicast", "local", "broadcast", "multicast"],
                    "default": None,
                },
                "src_port": {"type": "int"},
                "src_mac_address": {"type": "str"},
                "tcp_mss": {"type": "int"},
                "to_addresses": {"type": "str", "default": "0.0.0.0"},
                "to_ports": {"type": "int"},
                "ttl": {"type": "int"},
            },
        },
    }
