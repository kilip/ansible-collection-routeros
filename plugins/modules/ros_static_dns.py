#!/usr/bin/python


"""
The module file for ros_static_dns
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_static_dns
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
        description:
            - I(merged) M(ros_static_dns) will update existing C(/ip dns static) configuration, or create new C(/ip dns static) when resource not found
            - I(replaced) M(ros_static_dns) will restore existing C(/ip dns static) configuration to its default value, then update existing resource with the new configuration. If the resource C(/ip dns static) not found, M(ros_static_dns) will create resource in C(/ip dns static)
            - I(overridden) M(ros_static_dns) will remove any resource in C(/ip dns static) first, and then create new C(/ip dns static) resources.
            - I(deleted) M({module}) when found module will delete C(/ip dns static)
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
