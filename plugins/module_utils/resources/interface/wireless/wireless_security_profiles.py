# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Anthonius Munthi
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Ansible RouterOS Module Generator
#     and manual changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://github.com/kilip/routeros-generator
#
# ----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ...base import ResourceBase


class WirelessSecurityProfilesResource(ResourceBase):
    resource_name = "wireless_security_profiles"
    command = "/interface wireless security-profiles"
    gather_network_resources = ["wireless_security_profiles"]
    keys = ["name"]
    config_type = "config"
    argument_spec = {
        "state": {
            "type": "str",
            "choices": ["merged", "replaced", "overridden", "deleted"],
            "default": "merged",
        },
        "config": {
            "type": "list",
            "elements": "dict",
            "options": {
                "authentication_types": {
                    "type": "list",
                    "choices": ["wpa-eap", "wpa-psk", "wpa2-eap", "wpa2-psk"],
                },
                "comment": {"type": "str"},
                "disable_pmkid": {"type": "bool", "default": False},
                "disabled": {"type": "bool", "default": False},
                "eap_methods": {
                    "type": "str",
                    "choices": [
                        "eap-tls",
                        "eap-ttls-mschapv2",
                        "passthrough",
                        "peap",
                    ],
                    "default": "passthrough",
                },
                "group_ciphers": {
                    "type": "str",
                    "choices": ["aes-ccm", "tkip"],
                    "default": "aes-ccm",
                },
                "group_key_update": {"type": "str", "default": "5m"},
                "interim_update": {"type": "str", "default": 0},
                "mode": {
                    "type": "str",
                    "choices": [
                        "dynamic-keys",
                        "none",
                        "static-keys-optional",
                        "static-keys-required",
                    ],
                },
                "mschapv2_password": {"type": "str"},
                "mschapv2_username": {"type": "str"},
                "name": {"type": "str", "required": True},
                "radius_called_format": {
                    "type": "str",
                    "choices": ["mac", "mac:ssid", "ssid"],
                    "default": "mac:ssid",
                },
                "radius_eap_accounting": {"type": "bool", "default": False},
                "radius_mac_accounting": {"type": "bool", "default": False},
                "radius_mac_authentication": {
                    "type": "bool",
                    "default": False,
                },
                "radius_mac_caching": {
                    "type": "str",
                    "choices": ["disabled", "time"],
                    "default": "disabled",
                },
                "radius_mac_format": {
                    "type": "str",
                    "choices": [
                        "XX XX XX XX XX XX",
                        "XX-XX-XX-XX-XX-XX",
                        "XX:XX:XX:XX:XX:XX",
                        "XXXX:XXXX:XXXX",
                        "XXXXXX-XXXXXX",
                        "XXXXXX:XXXXXX",
                        "XXXXXXXXXXXX",
                    ],
                    "default": "XX:XX:XX:XX:XX:XX",
                },
                "radius_mac_mode": {
                    "type": "str",
                    "choices": ["as-username", "as-username-and-password"],
                    "default": "as-username",
                },
                "supplicant_identity": {
                    "type": "str",
                    "default": '[ Identity](https://wiki.mikrotik.com/wiki/Manual:System/identity "Manual:System/identity")',
                },
                "tls_certificate": {
                    "type": "str",
                    "choices": ["name", "none"],
                },
                "tls_mode": {
                    "type": "str",
                    "choices": [
                        "dont-verify-certificate",
                        "no-certificates",
                        "verify-certificate",
                        "verify-certificate-with-crl",
                    ],
                    "default": "no-certificates",
                },
                "unicast_ciphers": {
                    "type": "str",
                    "choices": ["aes-ccm", "tkip"],
                    "default": "aes-ccm",
                },
                "wpa2_pre_shared_key": {"type": "str"},
                "wpa_pre_shared_key": {"type": "str"},
            },
        },
    }