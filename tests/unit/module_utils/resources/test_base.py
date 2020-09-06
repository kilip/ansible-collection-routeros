from ...compat.unittest import TestCase
from .....plugins.module_utils.resources.base import ResourceBase


class RouterosResource(ResourceBase):
    name = "test"
    command = "/test"
    keys = ["name"]
    custom_props = {
        "three_gpp": {"ros_key": "3gpp"},
        "channel_band": {"ros_key": "channel.band"},
    }
    argument_spec = {
        "config": {
            "type": "list",
            "elements": "dict",
            "options": {
                "name": {"type": "str"},
                "three_gpp": {"type": "str"},
                "channel_band": {"type": "str"},
                "some_property": {"type": "str"},
            },
        }
    }


class TestResourceBase(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.resource = RouterosResource()

    def test_get_routeros_key(self):
        resource = self.resource
        self.assertEqual(
            resource.get_routeros_key("some_property"), "some-property"
        )
        self.assertEqual(resource.get_routeros_key("three_gpp"), "3gpp")

    def test_render_config(self):
        resource = self.resource
        conf = """
set 3gpp=value channel.band=value some-property=value
"""
        spec = resource.generate_dict()
        result = resource.render_config(spec, conf)
        self.assertEqual(result[0]["three_gpp"], "value")
        self.assertEqual(result[0]["channel_band"], "value")
        self.assertEqual(result[0]["some_property"], "value")

    def test_add(self):
        want = {
            "name": "spaced name",
            "some_property": "value",
            "channel_band": "value",
            "three_gpp": "value",
        }
        resource = self.resource
        result = resource.add(want)
        cmd = result[0]
        self.assertEqual(
            '/test add name="spaced name" some-property=value channel.band=value 3gpp=value',
            cmd,
        )

    def test_update(self):
        want = {
            "name": "spaced name",
            "some_property": "value",
            "channel_band": "value",
            "three_gpp": "value",
        }
        have = {
            "name": "name",
            "some_property": "old-value",
            "channel_band": "old-value",
            "three_gpp": "old-value",
        }
        resource = self.resource
        result = resource.update(want, have)
        cmd = result[0]
        self.assertEqual(
            '/test set [ find name="spaced name" ] some-property=value channel.band=value 3gpp=value',
            cmd,
        )

    def test_delete(self):
        want = {"name": "spaced name"}
        resource = self.resource
        result = resource.delete(want)

        self.assertEqual(result[0], '/test remove [ find name="spaced name" ]')
