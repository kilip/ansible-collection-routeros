from __future__ import absolute_import, division, print_function

__metaclass__ = type

from .base import ResourceBase


class UnsupportedResource(ResourceBase):

    argument_spec = {
        "config": {},
        "state": {
            "choices": ["merged", "replaced", "overridden", "deleted"],
            "type": "str",
            "default": "merged",
        },
    }
