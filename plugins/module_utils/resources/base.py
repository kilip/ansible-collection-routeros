from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from copy import deepcopy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    generate_dict,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils as net_utils,
)
from ..utils import dict_to_set, value_to_routeros, list_to_routeros


class ResourceBase(object):

    name = ""
    config_type = "config"
    argument_spec = {}
    command = ""
    gather_subset = ["!all", "!min"]
    gather_network_resources = []
    resource_name = ""
    keys = ["name"]
    filters = []
    use_verbose_mode = False
    prefixes = []
    supports = []
    custom_props = dict()
    facts_argument_spec = dict()
    has_delete_command = False

    def __init__(self):
        pass

    def support(self, feature):
        return feature in self.supports

    def has_options(self):
        return "options" in self.argument_spec["config"]

    def generate_dict(self, sub_spec="config", options="options"):
        spec = deepcopy(self.argument_spec)
        if sub_spec:
            if options and self.has_options():
                facts_argument_spec = spec[sub_spec][options]
            else:
                facts_argument_spec = spec[sub_spec]
        else:
            facts_argument_spec = spec
        self.facts_argument_spec = facts_argument_spec
        return generate_dict(facts_argument_spec)

    def render_config(self, spec, conf):
        split = re.split("set|add", conf)
        argspec = self.facts_argument_spec
        del split[0]
        configs = []
        for sp in split:
            config = self.parse_config(spec, sp, argspec)
            configs.append(config)

        if self.config_type == "config":
            return configs
        else:
            return configs[0]

    def clear_config(self, want, have):
        commands = []
        t = dict()
        self.generate_dict()
        argspec = self.facts_argument_spec

        for key in have:
            if have.get(key) != want.get(key):
                ctype = argspec[key]["type"]
                if ctype == "int":
                    t[key] = 0
                else:
                    t[key] = ""

        for key in self.keys:
            t[key] = want[key]

        commands.extend(self.update(t, have))
        return commands

    def get_command_prefix(self, want, have=None):
        prefix = self.command
        return prefix

    def get_routeros_key(self, key):
        props = self.custom_props
        ros_key = key.replace("_", "-")
        if props.get(key):
            prop = props[key]
            if prop.get("ros_key"):
                ros_key = props[key]["ros_key"]

        return ros_key

    def parse_config(self, spec, conf, argspec):
        """
        Parse routeros configuration and extract values
        :param spec: Configuration specification
        :param conf: routeros configuration values
        :return: an array of routeros config
        """
        config = deepcopy(spec)
        for key in config:
            mt_key = self.get_routeros_key(key)
            value = self.parse_conf_arg(conf, mt_key, argspec[key])

            if argspec is not None:
                vtype = argspec[key]["type"]
                if vtype == "list" and value is not None:
                    value = value.split(",")

            if value is not None:
                config[key] = value

        return net_utils.remove_empties(config)

    def parse_conf_arg(self, cfg, arg, argspec):
        """
        Parse config based on argument

        :param argspec: current facts argument spec
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

        vtype = argspec["type"]
        if result is not None:
            if vtype == "int":
                result = int(result)
            if vtype == "str":
                result = str(result)

        return result

    def _create_find_command(self, want):
        keys = self.keys
        finds = []
        for key in keys:
            if want.get(key) is None:
                continue
            value = value_to_routeros(want[key])
            finds.append(key.replace("_", "-") + "=" + value)
        return "[ find %s ]" % (" and ".join(finds))

    def add(self, want):
        commands = []
        command_prefix = self.get_command_prefix(want)
        prefix = "{0} add ".format(command_prefix)

        # always remove default values for new resource
        defaults = self.generate_dict()
        values = self.generate_command_values(want, defaults, [])
        if values:
            cmd = prefix + " ".join(values)
            commands.append(cmd)
        return commands

    def update(self, want, have):
        find_command = self._create_find_command(want)
        command_prefix = self.get_command_prefix(want, have)
        prefix = "{0} set {1} ".format(command_prefix, find_command)
        commands = []
        filters = self.keys
        for fkey in self.filters:
            filters.append(fkey)

        # start generating values
        values = self.generate_command_values(want, have, filters)
        if values:
            cmd = prefix + " ".join(values)
            commands.append(cmd)
        return commands

    def delete(self, want):
        commands = []
        prefix = self.get_command_prefix(want)
        find_command = self._create_find_command(want)
        cmd = "{0} remove {1}".format(prefix, find_command)
        commands.append(cmd)

        self.has_delete_command = True

        return commands

    def generate_command_values(self, want, have, filters):
        cmd = []
        want_dict = dict_to_set(want)
        have_dict = dict_to_set(have)
        diff = want_dict - have_dict
        diff = dict(diff)
        for key in want:
            if key in filters:
                continue
            if diff.get(key) is not None:
                ros_key = self.get_routeros_key(key)
                value = want.get(key)
                if type(value) is list:
                    cmd.append(ros_key + "=" + list_to_routeros(value))
                else:
                    value = value_to_routeros(value)
                    cmd.append(ros_key + "=" + str(value))
        return cmd

    def _custom_config(self, spec, conf):
        """
        Add additional config for resource
        :param spec: resource spec
        :param conf: routeros config
        :return: returns the custom config for current resource
        """
        return {}
