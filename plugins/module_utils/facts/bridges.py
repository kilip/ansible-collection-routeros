from __future__ import absolute_import, division, print_function

__metaclass__ = type

from copy import deepcopy
import re

from ansible.module_utils._text import to_text
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils as net_utils,
)

from ..argspec.bridges import BridgesArgs
from ..connection import (
    get_config
)
from ..utils import (
    parse_config
)

BRIDGES_FACTS_COMMAND = '/interface bridge export verbose terse'


class BridgesFacts(object):

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = BridgesArgs.argument_spec
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
        bridges = []

        if not data:
            data = self._get_bridges_data()

        # ensure line between /interface word
        data = data.replace("/interface", "\n/interface")
        configs = data.split("/interface bridge add ")
        del configs[0]
        for config in configs:
            obj = self._render_config(self.generated_spec, config)
            if obj:
                bridges.append(obj)

        if bridges:
            ansible_facts["ansible_network_resources"].update({"bridges": bridges})
        return ansible_facts

    def _render_config(self, spec, conf):
        config = parse_config(spec, conf)

        # parse stp config
        stp = parse_config(spec['stp'], conf)
        if stp:
            config['stp'] = stp

        # parse vlan config
        vlan = parse_config(spec['vlan'], conf)
        if vlan:
            config['vlan'] = vlan

        return config

    def _get_bridges_data(self):
        return get_config(self._module, BRIDGES_FACTS_COMMAND)
