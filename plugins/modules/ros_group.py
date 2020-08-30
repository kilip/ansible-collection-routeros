#!/usr/bin/python


"""
The module file for ros_group
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_group
short_description: Router User Group Management
description: The router user groups provide a convenient way to assign different permissions and access rights to different user classes.
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
            - I(merged) M(ros_group) will update existing C(/user group) configuration, or create new C(/user group) when resource not found
            - I(replaced) M(ros_group) will restore existing C(/user group) configuration to its default value, then update existing resource with the new configuration. If the resource C(/user group) not found, M(ros_group) will create resource in C(/user group)
            - I(overridden) M(ros_group) will remove any resource in C(/user group) first, and then create new C(/user group) resources.
            - I(deleted) M({module}) when found module will delete C(/user group)
    config:
        description: A dictionary for L(ros_group)
        type: list
        elements: dict
        suboptions:
            name:
                type: str
                required: True
                description: |
                    The name of the user group
            policy:
                elements: str
                type: list
                negation_symbol: !
                choices:
                    - local
                    - telnet
                    - ssh
                    - ftp
                    - reboot
                    - read
                    - write
                    - policy
                    - test
                    - winbox
                    - password
                    - web
                    - sniff
                    - sensitive
                    - api
                    - romon
                    - dude
                    - tikapp
                    - !local
                    - !telnet
                    - !ssh
                    - !ftp
                    - !reboot
                    - !read
                    - !write
                    - !policy
                    - !test
                    - !winbox
                    - !password
                    - !web
                    - !sniff
                    - !sensitive
                    - !api
                    - !romon
                    - !dude
                    - !tikapp
                default: None
                description: |
                    List of allowed policies:
                    Login policies:
                    - local - policy that grants rights to log in locally via console
                    - telnet - policy that grants rights to log in remotely via telnet
                    - ssh - policy that grants rights to log in remotely via secure shell protocol
                    - web - policy that grants rights to log in remotely via WebFig.
                    - winbox - policy that grants rights to log in remotely via WinBox and bandwidth test authentication
                    - password - policy that grants rights to change the password
                    - api - grants rights to access router via API.
                    - tikapp - policy that grants rights to log in remotely via Tik-App.
                    - dude - grants rights to log in to dude server.
                    - ftp - policy that grants full rights to log in remotely via FTP, to read/write/erase files and to transfer files from/to the router. Should be used together with read/write policies.
                    - romon - policy that grants rights to connect to RoMon server.
                    Config Policies:
                    - reboot - policy that allows rebooting the router
                    - read - policy that grants read access to the routers configuration. All console commands that do not alter routers configuration are allowed. Doesnt affect FTP
                    - write - policy that grants write access to the routers configuration, except for user management. This policy does not allow to read the configuration, so make sure to enable read policy as well
                    - policy - policy that grants user management rights. Should be used together with write policy. Allows also to see global variables created by other users (requires also test policy).
                    - test - policy that grants rights to run ping, traceroute, bandwidth-test, wireless scan, snooper and other test commands
                    - sensitive - grants rights to change "hide sensitive" option, if this policy is disabled sensitive information is not displayed, see below list as to what is regarded as sensitive.
                    - sniff - policy that grants rights to use packet sniffer tool.
            skin:
                type: str
                default: default
                description: |
                    Used L( skin,/wiki/Manual:Webfig#Skins) for WebFig

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.user.group import GroupResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=GroupResource.argument_spec)
    result = ResourceConfig(module, GroupResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
