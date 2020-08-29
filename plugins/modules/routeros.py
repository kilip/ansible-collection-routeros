#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: routeros
author: Anthonius Munthi @(kilip)
short_description: Main RouterOS Configuration Module 
description:
- Configure RouterOS Resource
version_added: 1.0.0
options:
  resource: resource to config
    choices:
    - interface
    - bridge
    - bridge_port
    description:
    - Resource to config
    type: str
    required: True
  state:
    
"""
EXAMPLES = """

"""
RETURN = """
"""

from ansible.module_utils.basic import AnsibleModule, _load_params
from ..module_utils.config.resource import ResourceConfig
from ..module_utils.resources.resource_set import RESOURCES_SET

def get_resource():
    params = _load_params()
    rsc = params["resource"]
    resource = RESOURCES_SET.get(rsc)
    if resource:
        return resource


def create_argument_spec(resource):
    resource_choices = []
    for key in RESOURCES_SET:
        resource_choices.append(key)

    argument_spec = dict(
        resource=dict(choices=resource_choices, type="str", required=True),
        config=dict(),
        state=dict(),
    )

    if resource:
        argument_spec.update(resource.argument_spec)
    return argument_spec


def main():
    resource = get_resource()
    argument_spec = create_argument_spec(resource)
    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True
    )
    if resource:
        result = ResourceConfig(module, resource).execute_module()
        return module.exit_json(**result)
    else:
        result = {"changed": False}
        return module.exit_json(**result)


if __name__ == "__main__":
    main()
