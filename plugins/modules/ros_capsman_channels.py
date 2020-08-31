#!/usr/bin/python


"""
The module file for ros_capsman_channels
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_capsman_channels
short_description: Manage configuration for C(/caps-man channels)
description: This M(ros_capsman_channels) module provides management for RouterOS C(/caps-man channels).
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
               *  M(ros_capsman_channels) will update existing C(/caps-man channels) configuration
            -  When Resource Not Exists:
               *  M(ros_capsman_channels) will create new C(/caps-man channels),
            Replaced
            -  When Resource Exists:
               *  M(ros_capsman_channels) will restore related C(/caps-man channels) to its default value.
               *  M(ros_capsman_channels) will update C(/caps-man channels) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_capsman_channels) will create new C(/caps-man channels)
            Overridden:
            *  M(ros_capsman_channels) will remove any existing item in C(/caps-man channels)
            *  M(ros_capsman_channels) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_capsman_channels) will remove that item from C(/caps-man channels) configuration
    config:
        description: A dictionary for L(ros_capsman_channels)
        type: list
        elements: dict
        suboptions:
            band:
                type: str
                choices:
                    - 2ghz-b
                    - 2ghz-b/g
                    - 2ghz-b/g/n
                    - 2ghz-onlyg
                    - 2ghz-onlyn
                    - 5ghz-a
                    - 5ghz-a/n
                    - 5ghz-onlyn
                default: None
                description: |
                    Define operational radio frequency band and mode taken from hardware capability
                    of wireless card
            comment:
                type: str
                description: |
                    Short description of the Channel Group profile
            extension_channel:
                type: str
                choices:
                    - ce
                    - ceee
                    - ec
                    - ecee
                    - eece
                    - eeec
                    - disabled
                default: None
                description: |
                    Extension channel configuration. (E.g. Ce = extension channel is above Control
                    channel, eC = extension channel is below Control channel)
            frequency:
                type: int
                description: |
                    Channel frequency value in MHz on which AP will operate.
            name:
                type: str
                required: True
                description: |
                    Descriptive name for the Channel Group Profile
            tx_power:
                type: int
                description: |
                    TX Power for CAP interface (for the whole interface not for individual chains)
                    in dBm. It is not possible to set higher than allowed by country regulations or
                    interface. By default max allowed by country or interface is used.
            width:
                type: str
                description: |
                    Sets Channel Width in MHz. (E.g. 20, 40)
            save_selected:
                type: str
                default: yes
                description: |
                    Saves selected channel for the CAP Radio - will select this channel after the
                    CAP reconnects to CAPsMAN and use it till the channel Re-optimize is done for
                    this CAP.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.capsman.channels import CapsmanChannelsResource
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(argument_spec=CapsmanChannelsResource.argument_spec)
    result = ResourceConfig(module, CapsmanChannelsResource).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
