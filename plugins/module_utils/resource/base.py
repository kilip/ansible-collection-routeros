from __future__ import absolute_import, division, print_function

__metaclass__ = type
from copy import deepcopy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    generate_dict,
)


class ResourceBase(object):
    def __init__(self):
        pass

    name = ""
    argument_spec = {}
    command_root = ""
    remove_related_resource = False
    related_resource_key = "name"
    gather_subset = ["!all", "!min"]
    gather_network_resources = []
    resource_name = ""
    resource_keys = ["name"]
    value_filters = []

    def generate_dict(self, sub_spec="config", options="options"):
        spec = deepcopy(self.argument_spec)
        if sub_spec:
            if options:
                facts_argument_spec = spec[sub_spec][options]
            else:
                facts_argument_spec = spec[sub_spec]
        else:
            facts_argument_spec = spec
        return generate_dict(facts_argument_spec)
