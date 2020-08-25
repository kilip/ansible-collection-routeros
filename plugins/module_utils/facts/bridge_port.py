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
