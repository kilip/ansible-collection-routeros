#!/usr/bin/python


"""
The module file for ros_user
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_user
short_description: Router User Group Management
description: Router user database stores the information such as username, password, allowed access addresses and group about router management personnel.
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
            - I(merged) M(ros_user) will update existing C(/user) configuration, or create new C(/user) when resource not found
            - I(replaced) M(ros_user) will restore existing C(/user) configuration to its default value, then update existing resource with the new configuration. If the resource C(/user) not found, M(ros_user) will create resource in C(/user)
            - I(overridden) M(ros_user) will remove any resource in C(/user) first, and then create new C(/user) resources.
            - I(deleted) M({module}) when found module will delete C(/user)
    config:
        description: A dictionary for L(ros_user)
        type: list
        elements: dict
        suboptions:
            address:
                type: str
                description: |
                    Host or network address from which the user is allowed to log in
            group:
                type: str
                description: |
                    Name of the L( group,#User_Groups) the user belongs to
            name:
                type: str
                required: True
                description: |
                    User name. Although it must start with an alphanumeric character, it may contain "", "_", "." and "@" symbols.
            password:
                type: str
                description: |
                    User password. If not specified, it is left blank (hit [Enter] when logging in). It conforms to standard Unix characteristics of passwords and may contain letters, digits, "" and "_" symbols.
            last_logged_in:
                type: str
                description: |
                    Read-only field. Last time and date when user logged in.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.user.user import UserResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=UserResource.argument_spec)
    result = ResourceConfig(module, UserResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
