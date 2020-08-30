# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kilip.routeros.plugins.modules import (
    ros_bridge_settings,
)
from .utils import set_module_args
from .config_module import TestConfigModule


class TestROSBridgeSettingsModule(TestConfigModule):

    module = ros_bridge_settings

    def test_present(self):
        set_module_args(
            dict(
                config=dict(
                    allow_fast_path=True,
                    use_ip_firewall=False,
                    use_ip_firewall_for_pppoe=False,
                    use_ip_firewall_for_vlan=False,
                )
            )
        )
        commands = [
            "/interface bridge settings set allow-fast-path=yes use-ip-firewall-for-pppoe=no use-ip-firewall-for-vlan=no use-ip-firewall=no"
        ]
        self.execute_module(False, True, commands, True)

    def test_reset(self):
        set_module_args(dict(state="reset"))
        commands = [
            "/interface bridge settings set allow-fast-path=yes use-ip-firewall-for-pppoe=no use-ip-firewall-for-vlan=no use-ip-firewall=no"
        ]
        self.execute_module(False, True, commands)
