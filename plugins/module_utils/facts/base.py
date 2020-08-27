from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..routeros import get_config
from ..utils import parse_config
from ..resource.base import ResourceBase


class FactsBase(object):

    resource = ResourceBase()

    def __init__(self, module, sub_spec="config", options="options"):
        self._module = module
        resource = self.resource
        self.generated_spec = resource.generate_dict(sub_spec, options)

    def populate_facts(self, connection, ansible_facts, data=None):
        resources = []
        resource = self.resource
        if not data:
            data = self._get_resources_data()

        # ensure line between /interface word
        data = data.replace("/", "\n/")
        configs = data.split(resource.command_root + " ")
        del configs[0]
        for config in configs:
            obj = self._render_config(self.generated_spec, config)
            if obj:
                resources.append(obj)

        if resources:
            ansible_facts["ansible_network_resources"].update(
                {resource.resource_name: resources}
            )
        return ansible_facts

    def _get_resources_data(self):
        return get_config(
            self._module, self.resource.command_root + " export terse"
        )

    def _render_config(self, spec, conf):
        config = parse_config(spec, conf)
        # parse dict type config
        for key in spec:
            if type(spec[key]) == dict:
                config[key] = parse_config(spec[key], conf)

        additional_config = self.additional_config(spec, conf)
        if additional_config:
            config.update(additional_config)
        return config

    def additional_config(self, spec, conf):
        return {}
