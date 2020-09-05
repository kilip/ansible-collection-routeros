from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..routeros import get_config


class ResourceFacts(object):
    def __init__(self, module, resource, sub_spec="config", options="options"):
        self._module = module
        self._resource = resource()
        self.generated_spec = self._resource.generate_dict(sub_spec, options)

    def populate_facts(self, connection, ansible_facts, data=None):
        resource = self._resource
        if not data:
            data = self._get_resources_data()

        configs = data.split(resource.command)

        # remove export header
        del configs[0]

        if resource.type == "config":
            resources = []
            for config in configs:
                objs = resource.render_config(self.generated_spec, config)
                if objs:
                    resources.extend(objs)
        else:
            resources = dict()
            for config in configs:
                objs = resource.render_config(self.generated_spec, config)
                if objs:
                    resources = objs

        if resources:
            ansible_facts["ansible_network_resources"].update(
                {resource.resource_name: resources}
            )
        return ansible_facts

    def _get_resources_data(self):
        command = self._resource.command + " export"
        if self._resource.support("facts_verbose_mode"):
            command = command + " verbose"
        return get_config(self._module, command)
