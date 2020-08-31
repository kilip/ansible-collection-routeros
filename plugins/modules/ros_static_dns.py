#!/usr/bin/python


"""
The module file for ros_static_dns
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_static_dns
short_description: Manage configuration for C(/ip dns static)
description: This M(ros_static_dns) module provides management for RouterOS C(/ip dns static).
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
short_documentation: DNS Cache Configuration
options:
    state:
        choices:
            - merged
            - replaced
            - overridden
            - deleted
        default: merged
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_static_dns) will update existing C(/ip dns static) configuration
            -  When Resource Not Exists:
               *  M(ros_static_dns) will create new C(/ip dns static),
            Replaced
            -  When Resource Exists:
               *  M(ros_static_dns) will restore related C(/ip dns static) to its default value.
               *  M(ros_static_dns) will update C(/ip dns static) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_static_dns) will create new C(/ip dns static)
            Overridden:
            *  M(ros_static_dns) will remove any existing item in C(/ip dns static)
            *  M(ros_static_dns) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_static_dns) will remove that item from C(/ip dns static) configuration
    config:
        description: A dictionary for L(ros_static_dns)
        type: list
        elements: dict
        suboptions:
            address:
                type: str
                description: |
                    IP address to resolve domain name with
            name:
                type: str
                required: True
                description: |
                    DNS name to be resolved to a given IP address.
            regex:
                type: str
                description: |
                    DNS regex
            ttl:
                type: str
                description: |
                    time-to-live of the DNS record
            type:
                type: str
                description: |
                    type of the DNS record. Available values are: A, AAAA, CNAME, FWD, MX, NS, NXDOMAIN, SRV, TXT

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.ip.static_dns import StaticDnsResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=StaticDnsResource.argument_spec)
    result = ResourceConfig(module, StaticDnsResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
