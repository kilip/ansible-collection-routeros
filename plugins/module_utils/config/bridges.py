from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .resources import Resources
from ..facts.bridges import BRIDGES_FACTS_COMMAND


class Bridges(Resources):

    def __init__(self, module):
        super(Bridges, self).__init__(
            module,
            "bridges",
            BRIDGES_FACTS_COMMAND
        )
        self.config_root = "/interface bridge"

