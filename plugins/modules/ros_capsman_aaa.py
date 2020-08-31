#!/usr/bin/python


"""
The module file for ros_capsman_aaa
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_capsman_aaa
short_description: Manage configuration for C(/caps-man aaa)
description: This M(ros_capsman_aaa) module provides management for RouterOS C(/caps-man aaa).
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
    state:
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_capsman_aaa) will update existing C(/caps-man aaa) configuration
            -  When Resource Not Exists:
               *  M(ros_capsman_aaa) will create new C(/caps-man aaa),
            Replaced
            -  When Resource Exists:
               *  M(ros_capsman_aaa) will restore related C(/caps-man aaa) to its default value.
               *  M(ros_capsman_aaa) will update C(/caps-man aaa) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_capsman_aaa) will create new C(/caps-man aaa)
            Overridden:
            *  M(ros_capsman_aaa) will remove any existing item in C(/caps-man aaa)
            *  M(ros_capsman_aaa) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_capsman_aaa) will remove that item from C(/caps-man aaa) configuration
    config:
        description: A dictionary for L(ros_capsman_aaa)
        suboptions:
            mac_format:
                type: str
                default: xx:xx:xx:xx:xx:xx
                description: |
                    Controls how MAC address of the client is encoded by Access Point in the
                    User-Name attribute of the MAC authentication and MAC accounting RADIUS
                    requests.
            mac_mode:
                type: str
                choices:
                    - as-username
                    - as-username-and-password
                default: None
                description: |
                    By default Access Point uses an empty password, when sending Access-Request
                    during MAC authentication. When this property is set to
                    as-username-and-password, Access Point will use the same value for User-Password
                    attribute as for the User-Name attribute.
            mac_caching:
                type: str
                default: disabled
                choices:
                    - disabled
                    - time-interval
                description: |
                    If this value is set to time interval, the Access Point will cache RADIUS MAC
                    authentication responses for specified time, and will not contact RADIUS server
                    if matching cache entry already exists. Value disabled will disable cache,
                    Access Point will always contact RADIUS server.
            interim_update:
                type: str
                default: disabled
                choices:
                    - disabled
                    - time-interval
                description: |
                    When RADIUS accounting is used, Access Point periodically sends accounting
                    information updates to the RADIUS server. This property specifies default update
                    interval that can be overridden by the RADIUS server using the L(
                    Acct-Interim-Interval,/wiki/Manual:Interface/Wireless#RADIUS_MAC_authentication)
                    attribute.
            called_format:
                type: str
                default: mac:ssid
                choices:
                    - mac
                    - mac
                description: |
                    Format of how the "called-id" identifier will be passed to RADIUS. When
                    configuring radius server clients, you can specify "called-id" in order to
                    separate multiple entires.
config:
    type: list
state:
    choices:
        - present
        - reset
    default: present

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.capsman.aaa import CapsmanAaaResource
from ..module_utils.config.config import Config


def main():
    module = AnsibleModule(argument_spec=CapsmanAaaResource.argument_spec)
    result = Config(module, CapsmanAaaResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
