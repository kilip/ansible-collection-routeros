from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from ansible_collections.community.network.plugins.module_utils.network.routeros.routeros import (
    run_commands,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
    to_text,
)

DEVICE_CONFIGS = {}


def generate_config_key(command):
    sub = re.sub("(.*)(export|add|remove).*", "\\1", command)
    sub = sub.strip().replace(" ", "_").replace("/", "")
    return sub


def normalize_config(config):
    """
    Replace all line break between an alphabet, equal, or underscore sign
    :param config: The configuration text
    :rtype string
    :return: normalized config
    """
    config = re.sub(r"([a-z|=|\\|\-])(\n)(\s+)", "\\1", config)
    config = config.replace("\\", "")
    return config


def reset_config(command):
    key = generate_config_key(command)
    if DEVICE_CONFIGS.get(key) is not None:
        del DEVICE_CONFIGS[key]


def get_config(module, command):
    key = generate_config_key(command)
    try:
        return DEVICE_CONFIGS[key]
    except KeyError:
        cfg = run_commands(module, commands=[command])

    cfg = "\n".join(cfg)
    cfg = to_text(cfg)
    cfg = normalize_config(cfg)
    DEVICE_CONFIGS[key] = cfg
    return cfg


def load_config(module, commands):
    response = {}
    results = []
    requests = []
    for line in to_list(commands):
        requests.append(line)
        out = run_commands(module, commands=line)
        results.append("\n".join(out))
        reset_config(line)

    response["results"] = results
    response["requests"] = requests

    return response
