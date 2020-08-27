from ..compat.unittest import TestCase
from ansible_collections.kilip.routeros.plugins.module_utils.utils import (
    remove_default_values,
)
from ansible_collections.kilip.routeros.plugins.module_utils.resource.bridge import (
    BridgeResource,
)


class TestUtils(TestCase):
    def test_remove_default_values(self):
        config = dict(
            name="br-test", comment="test", vlan=dict(vlan_filtering=False)
        )
        spec = BridgeResource().generate_dict()
        normalized = remove_default_values(spec, config)
        self.assertEqual(normalized["name"], "br-test")
        self.assertEqual(normalized["comment"], "test")
        self.assertEqual(normalized["vlan"], {})
