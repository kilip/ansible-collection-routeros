from __future__ import absolute_import, division, print_function

__metaclass__ = type

from copy import deepcopy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    generate_dict,
)
from ..utils import parse_config


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
    use_verbose_mode = False

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

    def render_config(self, spec, conf):
        config = parse_config(spec, conf)
        # parse dict type config
        for key in spec:
            if type(spec[key]) == dict:
                config[key] = parse_config(spec[key], conf)

        additional_config = self._custom_config(spec, conf)
        if additional_config is not None:
            config.update(additional_config)
        return config

    def get_command_prefix(self, want, have=None):
        prefix = self.command_root
        return prefix

    def _custom_config(self, spec, conf):
        """
        Add additional config for resource
        :param spec: resource spec
        :param conf: routeros config
        :return: returns the custom config for current resource
        """
        return {}
