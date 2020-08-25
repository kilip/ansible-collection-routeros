from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from copy import deepcopy
from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils as net_utils,
)

def get_interface_type(interface):
    """Gets the type of interface from config
    """
    if interface.upper().startswith("ETHERNET"):
        return "ethernet"
    elif interface.upper().startswith("BRIDGE"):
        return "bridge"
    elif interface.upper().startswith("VLAN"):
        return "vlan"
    else:
        return "unknown"


def normalize_interface(name):
    if not name:
        return None


def parse_config(spec, conf):
    """
    Parse routeros configuration and extract values
    :param spec: Configuration specification
    :param conf: routeros configuration values
    :return: an array of routeros config
    """
    config = deepcopy(spec)
    for key in config:
        mt_key = key.replace("_", "-")
        value = parse_conf_arg(conf, mt_key)
        if value == 'yes' or value == 'no':
            value = True if value == 'yes' else False

        if value is not None:
            config[key] = value

    return net_utils.remove_empties(config)


def parse_conf_arg(cfg, arg):
    """
    Parse config based on argument

    :param cfg: A text string which is a line of configuration.
    :param arg: A text string which is to be matched.
    :rtype: A text string
    :returns: A text string if match is found
    """
    match = re.search(r'%s=(".*?"|\S+)' % arg, cfg, re.M)
    if match:
        result = match.group(1).strip("\n")
        result = result.replace('"', "")
    else:
        result = None
    return result


def dict_to_set(sample_dict):
    # Generate a set with passed dictionary for comparison
    test_dict = dict()
    if isinstance(sample_dict, dict):
        for k, v in iteritems(sample_dict):
            if v is not None:
                if isinstance(v, list):
                    if isinstance(v[0], dict):
                        li = []
                        for each in v:
                            for key, value in iteritems(each):
                                if isinstance(value, list):
                                    each[key] = tuple(value)
                            li.append(tuple(iteritems(each)))
                        v = tuple(li)
                    else:
                        v = tuple(v)
                elif isinstance(v, dict):
                    li = []
                    for key, value in iteritems(v):
                        if isinstance(value, list):
                            v[key] = tuple(value)
                    li.extend(tuple(iteritems(v)))
                    v = tuple(li)
                test_dict.update({k: v})
        return_set = set(tuple(iteritems(test_dict)))
    else:
        return_set = set(sample_dict)
    return return_set


def key_to_routeros(key):
    return key.replace('_', '-').strip()


def value_to_routeros(value):
    if type(value) is bool:
        value = "yes" if value else "no"

    if " " in value:
        value = '"' + value + '"'
    return value


def generate_command_values(want, have):
    cmd = []
    want_dict = dict_to_set(want)
    have_dict = dict_to_set(have)
    diff = want_dict - have_dict
    diff = dict(diff)
    for key in want:
        if key == 'name':
            continue
        if diff.get(key) is not None:
            ros_key = key_to_routeros(key)
            value = want.get(key)
            if type(value) is not dict:
                value = value_to_routeros(value)
                cmd.append(ros_key + "=" + value)
            else:
                have_section = dict()
                if have.get(key) is not None:
                    have_section = have.get(key)
                cmd.extend(generate_command_values(want[key], have_section))
    return cmd
