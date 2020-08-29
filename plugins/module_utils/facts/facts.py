from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts import (
    FactsBase,
)
from .legacy import Default, Hardware, Interfaces, Config
from ..resources.interface import InterfaceResource
from ..resources.bridge import BridgeResource
from ..resources.bridge_port import BridgePortResource
from .resource import ResourceFacts

FACT_LEGACY_SUBSETS = dict(
    default=Default, hardware=Hardware, interfaces=Interfaces, config=Config
)

FACT_RESOURCE_SUBSETS = dict(
    interfaces=InterfaceResource,
    bridges=BridgeResource,
    bridge_ports=BridgePortResource,
)


class Facts(FactsBase):
    """ The fact class for RouterOS
    """

    VALID_LEGACY_GATHER_SUBSETS = frozenset(FACT_LEGACY_SUBSETS.keys())
    VALID_RESOURCE_SUBSETS = frozenset(FACT_RESOURCE_SUBSETS.keys())

    def __init__(self, module):
        super(Facts, self).__init__(module)

    def get_facts(
        self, legacy_facts_type=None, resource_facts_type=None, data=None
    ):
        """ Collect the facts for RouterOS
        :param legacy_facts_type: List of legacy facts types
        :param resource_facts_type: List of resource fact types
        :param data: previously collected conf
        :rtype: dict
        :return: the facts gathered
        """
        if self.VALID_RESOURCE_SUBSETS:
            self.get_network_resources_facts(
                FACT_RESOURCE_SUBSETS, resource_facts_type, data
            )

        if self.VALID_LEGACY_GATHER_SUBSETS:
            self.get_network_legacy_facts(
                FACT_LEGACY_SUBSETS, legacy_facts_type
            )

        return self.ansible_facts, self._warnings

    def get_network_resources_facts(
        self, facts_resource_obj_map, resource_facts_type=None, data=None
    ):
        """
        :param facts_resource_obj_map
        :param resource_facts_type:
        :param data: previously collected configuration
        :return:
        """
        if not resource_facts_type:
            resource_facts_type = self._gather_network_resources

        restorun_subsets = self.gen_runable(
            resource_facts_type,
            frozenset(facts_resource_obj_map.keys()),
            resource_facts=True,
        )
        if restorun_subsets:
            self.ansible_facts["ansible_net_gather_network_resources"] = list(
                restorun_subsets
            )
            instances = list()
            for key in restorun_subsets:
                fact_cls_obj = facts_resource_obj_map.get(key)
                if fact_cls_obj:
                    obj = ResourceFacts(self._module, fact_cls_obj)
                    instances.append(obj)
                else:
                    self._warnings.extend(
                        [
                            "network resource fact gathering for '%s' is not supported"
                            % key
                        ]
                    )

            for inst in instances:
                inst.populate_facts(self._connection, self.ansible_facts, data)
