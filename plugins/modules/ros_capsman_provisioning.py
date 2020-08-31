#!/usr/bin/python


"""
The module file for ros_capsman_provisioning
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_capsman_provisioning
short_description: Manage configuration for C(/caps-man provisioning)
description: This M(ros_capsman_provisioning) module provides management for RouterOS C(/caps-man provisioning).
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
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
               *  M(ros_capsman_provisioning) will update existing C(/caps-man provisioning) configuration
            -  When Resource Not Exists:
               *  M(ros_capsman_provisioning) will create new C(/caps-man provisioning),
            Replaced
            -  When Resource Exists:
               *  M(ros_capsman_provisioning) will restore related C(/caps-man provisioning) to its default value.
               *  M(ros_capsman_provisioning) will update C(/caps-man provisioning) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_capsman_provisioning) will create new C(/caps-man provisioning)
            Overridden:
            *  M(ros_capsman_provisioning) will remove any existing item in C(/caps-man provisioning)
            *  M(ros_capsman_provisioning) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_capsman_provisioning) will remove that item from C(/caps-man provisioning) configuration
    config:
        description: A dictionary for L(ros_capsman_provisioning)
        type: list
        elements: dict
        suboptions:
            action:
                type: str
                choices:
                    - create-disabled
                    - create-enabled
                    - create-dynamic-enabled
                    - none
                default: None
                description: |
                    Action to take if rule matches are specified by the following settings:
                    - create-disabled - create disabled static interfaces for radio. I.e., the interfaces will be bound to the radio, but the radio will not be operational until the interface is manually enabled;
                    - create-enabled - create enabled static interfaces. I.e., the interfaces will be bound to the radio and the radio will be operational;
                    - create-dynamic-enabled - create enabled dynamic interfaces. I.e., the interfaces will be bound to the radio, and the radio will be operational;
                    - none - do nothing, leaves radio in non-provisioned state;
            comment:
                type: str
                description: |
                    Short description of the Provisioning rule
            common_name_regexp:
                type: str
                description: |
                    Regular expression to match radios by common name. Each CAPs common name identifier can be found under "/caps-man radio" as value "REMOTE-CAP-NAME"
            hw_supported_modes:
                type: str
                choices:
                    - a
                    - a-turbo
                    - ac
                    - an
                    - b
                    - g
                    - g-turbo
                    - gn
                default: None
                description: |
                    Match radios by supported wireless modes
            identity_regexp:
                type: str
                description: |
                    Regular expression to match radios by router identity
            ip_address_ranges:
                type: str
                description: |
                    Match CAPs with IPs within configured address range.
            master_configuration:
                type: str
                description: |
                    If action specifies to create interfaces, then a new master interface with its configuration set to this configuration profile will be created
            name_format:
                type: str
                default: cap
                choices:
                    - cap
                    - identity
                    - prefix
                    - prefix-identity
                description: |
                    specify the syntax of the CAP interface name creation
                    - cap - default name
                    - identity - CAP boards system identity name
                    - prefix - name from the name-prefix value
                    - prefix-identity - name from the name-prefix value and the CAP boards system identity name
            name_prefix:
                type: str
                description: |
                    name prefix which can be used in the name-format for creating the CAP interface names
            radio_mac:
                type: str
                default: 00:00:00:00:00:00
                description: |
                    MAC address of radio to be matched, empty MAC (00:00:00:00:00:00) means match all MAC addresses
            slave_configurations:
                type: str
                description: |
                    If action specifies to create interfaces, then a new slave interface for each configuration profile in this list is created.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.capsman.provisioning import (
    CapsmanProvisioningResource,
)
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(
        argument_spec=CapsmanProvisioningResource.argument_spec
    )
    result = ResourceConfig(
        module, CapsmanProvisioningResource
    ).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
