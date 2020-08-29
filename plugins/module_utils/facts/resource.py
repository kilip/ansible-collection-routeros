from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..routeros import get_config


class ResourceFacts(object):
    def __init__(self, module, resource, sub_spec="config", options="options"):
        self._module = module
        self._resource = resource()
        self.generated_spec = self._resource.generate_dict(sub_spec, options)

    def populate_facts(self, connection, ansible_facts, data=None):
        resources = []
        resource = self._resource
        if not data:
            data = self._get_resources_data()

        # ensure line between /interface word
        data = data.replace("/", "\n/")
        configs = data.split(resource.command_root + " ")
        del configs[0]
        for config in configs:
            obj = resource.render_config(self.generated_spec, config)
            if obj:
                resources.append(obj)

        if resources:
            ansible_facts["ansible_network_resources"].update(
                {resource.resource_name: resources}
            )
        return ansible_facts

    def _get_resources_data(self):
        command = self._resource.command_root + " export terse"
        if self._resource.use_verbose_mode:
            command = command + " verbose"
        return get_config(self._module, command)
