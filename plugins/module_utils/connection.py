# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

import os
import re
from ansible.module_utils._text import to_text
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.community.network.plugins.module_utils.network.routeros.routeros import (
    run_commands
)
from ansible_collections.community.network.plugins.module_utils.network.routeros.routeros import (
    get_connection,
)

_DEVICE_CONFIGS = {}


def _generate_key(command):
    key = command.replace("/","").replace(" ","_")
    return key


def normalize_config(config):
    return re.sub(r"([a-z|=|\-])(\n)", '\\1', config)


def get_config(module, command):
    key = _generate_key(command)
    try:
        return _DEVICE_CONFIGS[key]
    except KeyError:
        cfg = run_commands(module, command)

    cfg = "\n".join(cfg)
    cfg = to_text(cfg)
    cfg = normalize_config(cfg)
    _DEVICE_CONFIGS[key] = cfg
    return cfg


def reset_config(command):
    """
    Reset configuration cache for specified command
    :param command: RouterOS command
    """
    key = _generate_key(command)
    if _DEVICE_CONFIGS and _DEVICE_CONFIGS.get(key) is not None:
        del _DEVICE_CONFIGS[key]


def load_config(module, commands, facts_command=None):
    response = {}
    results = []
    requests = []
    for line in to_list(commands):
        requests.append(line)
        out = run_commands(module, commands)
        results.append("\n".join(out))

    response["results"] = results
    response["requests"] = requests

    if facts_command:
        reset_config(facts_command)

    return response
