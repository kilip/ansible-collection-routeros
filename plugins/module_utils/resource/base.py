from __future__ import absolute_import, division, print_function

__metaclass__ = type


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
