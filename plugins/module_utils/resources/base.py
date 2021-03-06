from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from copy import deepcopy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    generate_dict,
)
from ..utils import parse_config


class ResourceBase(object):
    def __init__(self):
        pass

    name = ""
    type = "config"
    argument_spec = {}
    command = ""
    gather_subset = ["!all", "!min"]
    gather_network_resources = []
    resource_name = ""
    keys = ["name"]
    filters = []
    use_verbose_mode = False
    prefixes = []
    facts_argument_spec = dict()
    supports = []

    def support(self, feature):
        return feature in self.supports

    def has_options(self):
        return "options" in self.argument_spec["config"]

    def generate_dict(self, sub_spec="config", options="options"):
        spec = deepcopy(self.argument_spec)
        if sub_spec:
            if options and self.has_options():
                facts_argument_spec = spec[sub_spec][options]
            else:
                facts_argument_spec = spec[sub_spec]
        else:
            facts_argument_spec = spec
        self.facts_argument_spec = facts_argument_spec
        return generate_dict(facts_argument_spec)

    def render_config(self, spec, conf):
        split = re.split("set|add", conf)
        argspec = self.facts_argument_spec
        del split[0]
        configs = []
        for sp in split:
            config = parse_config(spec, sp, argspec, self.prefixes)
            configs.append(config)

        if self.type == "config":
            return configs
        else:
            return configs[0]

    def get_command_prefix(self, want, have=None):
        prefix = self.command
        return prefix

    def _custom_config(self, spec, conf):
        """
        Add additional config for resource
        :param spec: resource spec
        :param conf: routeros config
        :return: returns the custom config for current resource
        """
        return {}
