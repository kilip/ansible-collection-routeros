from __future__ import absolute_import, division, print_function

__metaclass__ = type

from abc import abstractmethod
from copy import deepcopy
import re

from ansible.module_utils._text import to_text
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils as net_utils,
)

from ..connection import (
    get_config
)
from ..utils import (
    parse_config
)

class ResourceFactsBase(object):
    
    argument_spec = {}
    config_root = ""
    network_resource_name = ""
    resource_facts_command = ""

    def __init__(
        self, 
        module,
        subspec="config",
        options="options"
    ):
        self._module = module
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec
        self.generated_spec = net_utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        resources = []
        if not data:
            data = self._get_resources_data()

        # ensure line between /interface word
        data = data.replace("/interface", "\n/interface")
        configs = data.split(self.config_root + " add ")
        del configs[0]
        for config in configs:
            obj = self.do_render_config(self.generated_spec, config)
            if obj:
                resources.append(obj)

        if resources:
            ansible_facts["ansible_network_resources"].update({self.network_resource_name: resources})
        return ansible_facts

    @abstractmethod
    def do_render_config(self, spec, conf):
        pass

    def _get_resources_data(self):
        return get_config(self._module, self.config_root + " export verbose terse")
