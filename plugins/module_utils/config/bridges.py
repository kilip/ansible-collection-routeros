from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..utils import (
    generate_command_values,
)

from .resources import Resources
from ..facts.bridges import BRIDGES_FACTS_COMMAND


class Bridges(Resources):

    def __init__(self, module):
        super(Bridges, self).__init__(
            module,
            "bridges",
            BRIDGES_FACTS_COMMAND
        )

    def do_delete(self, want, have):
        commands = []
        cmd = f"/interface bridge remove [ find name=%s ]" % want["name"]
        commands.append(cmd)
        return commands

    def do_set_config(self, want, have):
        commands = []
        prefix = f"/interface bridge add name=%s " % (want["name"])
        if have:
            prefix = f"/interface bridge set [ find name=%s ] " % (want["name"])

        values = generate_command_values(want, have)
        if values:
            cmd = prefix + " ".join(values)
            commands.append(cmd)
        return commands
