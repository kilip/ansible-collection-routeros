#!/usr/bin/python


"""
The module file for ros_capsman_provisioning
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_capsman_provisioning
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
        description:
            - I(merged) M(ros_capsman_provisioning) will update existing C(/caps-man provisioning) configuration, or create new C(/caps-man provisioning) when resource not found
            - I(replaced) M(ros_capsman_provisioning) will restore existing C(/caps-man provisioning) configuration to its default value, then update existing resource with the new configuration. If the resource C(/caps-man provisioning) not found, M(ros_capsman_provisioning) will create resource in C(/caps-man provisioning)
            - I(overridden) M(ros_capsman_provisioning) will remove any resource in C(/caps-man provisioning) first, and then create new C(/caps-man provisioning) resources.
            - I(deleted) M({module}) when found module will delete C(/caps-man provisioning)
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
