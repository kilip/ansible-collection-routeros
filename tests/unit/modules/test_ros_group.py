from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.plugins.modules import ros_group
from .utils import set_module_args
from ansible_collections.kilip.routeros.plugins.module_utils.utils import (
    gen_remove_invalid_resource,
)
from .resource_module import TestResourceModule


class TestROSGroupModule(TestResourceModule):

    module = ros_group

    def test_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(name="group1", policy=["!reboot", "!api"]),
                    dict(name="test", policy=["!reboot", "api"]),
                ]
            )
        )
        commands = [
            "/user group set [ find name=group1 ] policy=!reboot,!api",
            "/user group add name=test policy=!reboot,api",
        ]
        self.execute_module(False, True, commands)

    def test_deleted(self):
        set_module_args(dict(config=[dict(name="group1")], state="deleted"))
        commands = [
            "/user group remove [ find name=group1 ]",
            gen_remove_invalid_resource(),
        ]
        self.execute_module(False, True, commands),
