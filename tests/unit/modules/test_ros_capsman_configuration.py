from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.plugins.modules import (
    ros_capsman_configuration,
)
from .utils import set_module_args
from ansible_collections.kilip.routeros.plugins.module_utils.utils import (
    gen_remove_invalid_resource,
)
from .resource_module import TestResourceModule


class TestROSCapsmanConfigurationModule(TestResourceModule):

    module = ros_capsman_configuration

    def test_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(name="olympus", datapath_bridge="changed"),
                    dict(name="new", datapath_bridge="br-trunk"),
                ]
            )
        )
        commands = [
            "/caps-man configuration set [ find name=olympus ] datapath.bridge=changed",
            "/caps-man configuration add name=new datapath.bridge=br-trunk",
        ]
        self.execute_module(False, True, commands)
