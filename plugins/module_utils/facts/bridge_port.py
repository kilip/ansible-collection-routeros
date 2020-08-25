from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..argspec.bridge_ports import BridgePortsArgs
from .resource_facts_base import ResourceFactsBase
from ..utils import (
    parse_config
)

class BridgePortFacts(ResourceFactsBase):
    def __init__(
        self, 
        module,
        subspec="config",
        options="options"
    ):
        self.argument_spec = BridgePortsArgs().argument_spec
        self.config_root = "/interface bridge port"
        self.network_resource_name = "bridge_ports"
        super(BridgePortFacts, self).__init__(
            module,
            subspec,
            options
        )

    def do_render_config(self, spec, conf):
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