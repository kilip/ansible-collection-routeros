#!/usr/bin/python


"""
The module file for ros_capsman_manager
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_capsman_manager
short_description: Manage configuration for C(/caps-man manager)
description: This M(ros_capsman_manager) module provides management for RouterOS C(/caps-man manager).
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
    state:
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_capsman_manager) will update existing C(/caps-man manager) configuration
            -  When Resource Not Exists:
               *  M(ros_capsman_manager) will create new C(/caps-man manager),
            Replaced
            -  When Resource Exists:
               *  M(ros_capsman_manager) will restore related C(/caps-man manager) to its default value.
               *  M(ros_capsman_manager) will update C(/caps-man manager) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_capsman_manager) will create new C(/caps-man manager)
            Overridden:
            *  M(ros_capsman_manager) will remove any existing item in C(/caps-man manager)
            *  M(ros_capsman_manager) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_capsman_manager) will remove that item from C(/caps-man manager) configuration
    config:
        description: A dictionary for L(ros_capsman_manager)
        suboptions:
            enabled:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Disable or enable CAPsMAN functionality
            certificate:
                type: str
                choices:
                    - auto
                    - certificate
                    - name
                    - none
                default: None
                description: |
                    Device certificate
            ca_certificate:
                type: str
                choices:
                    - auto
                    - certificate
                    - name
                    - none
                default: None
                description: |
                    Device CA certificate
            require_peer_certificate:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Require all connecting CAPs to have a valid certificate
            package_path:
                type: str
                choices:
                    - string
                default: None
                description: |
                    Folder location for the RouterOS packages. For example, use "/upgrade" to specify the upgrade folder from the files section. If empty string is set, CAPsMAN can use built-in RouterOS packages, note that in this case only CAPs with the same architecture as CAPsMAN will be upgraded.
            upgrade_policy:
                type: str
                choices:
                    - none
                    - require-same-version
                    - suggest-same-upgrade
                default: None
                description: |
                    Upgrade policy options
                    - none - do not perform upgrade
                    - require-same-version - CAPsMAN suggest to upgrade the CAP RouterOS version and if it fails it will not provision the CAP. (Manual provision is still possible)
                    - suggest-same-version - CAPsMAN suggests to upgrade the CAP RouterOS version and if it fails it will still be provisioned
config:
    type: list
state:
    choices:
        - present
        - reset
    default: present

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.capsman.manager import CapsmanManagerResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=CapsmanManagerResource.argument_spec)
    result = Config(module, CapsmanManagerResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
