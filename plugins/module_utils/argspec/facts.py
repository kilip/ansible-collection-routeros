"""
The arg spec for the RouterOS facts module.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class FactsArgs(object):
    """ The arg spec for the RouterOS facts module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "gather_subset": dict(
            default=["!config"], type="list", elements="str"
        ),
        "gather_network_resources": dict(type="list", elements="str"),
    }
