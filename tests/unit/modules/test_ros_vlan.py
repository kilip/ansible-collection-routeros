from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.plugins.modules import ros_vlan
from .utils import set_module_args
from ansible_collections.kilip.routeros.plugins.module_utils.utils import (
    gen_remove_invalid_resource,
)
from .resource_module import TestResourceModule


class TestROSVlanModule(TestResourceModule):

    module = ros_vlan

    def test_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(interface="br-trunk", vlan_id=100, name="vlan-100"),
                    dict(interface="br-trunk", vlan_id=300, name="vlan-300"),
                ]
            )
        )
        commands = [
            "/interface vlan set [ find interface=br-trunk and name=vlan-100 ] vlan-id=100",
            "/interface vlan add interface=br-trunk vlan-id=300 name=vlan-300",
        ]
        self.execute_module(False, True, commands)

    def test_deleted(self):
        set_module_args(
            dict(
                config=[dict(interface="br-trunk", name="vlan-100")],
                state="deleted",
            )
        )
        commands = [
            "/interface vlan remove [ find interface=br-trunk and name=vlan-100 ]",
            gen_remove_invalid_resource(),
        ]
        self.execute_module(False, True, commands)
