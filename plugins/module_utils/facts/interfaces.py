from __future__ import absolute_import, division, print_function

__metaclass__ = type

from copy import deepcopy
import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.kilip.routeros.plugins.module_utils.argspec.interfaces import (
    InterfacesArgs,
)
from ansible_collections.kilip.routeros.plugins.module_utils.connection import (
    get_config
)
from ansible_collections.kilip.routeros.plugins.module_utils.utils import (
    get_interface_type,
    normalize_interface,
    parse_conf_arg,
)

INTERFACES_FACTS_COMMAND = "/interface export verbose terse"

class InterfacesFacts(object):

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = InterfacesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_interfaces_data(self, connection):
        return get_config(self._module, INTERFACES_FACTS_COMMAND)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for interfaces
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = []

        if not data:
            data = self.get_interfaces_data(connection)

        # operate on a collection of resource
        config = data.split("/interface ")
        del config[0]
        for conf in config:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
                if obj:
                    objs.append(obj)
        facts = {}

        if objs:
            facts["interfaces"] = []
            params = utils.validate_config(
                self.argument_spec, {"config": objs}
            )
            for cfg in params["config"]:
                facts["interfaces"].append(utils.remove_empties(cfg))

        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)
        match = re.search(r"^(\S+)", conf)
        intf = match.group(1)
        intype = get_interface_type(intf)
        if get_interface_type(intype) == "unknown":
            return {}
        # populate the facts from the configuration

        config["comment"] = parse_conf_arg(conf, "comment")
        config["type"] = intype

        name = parse_conf_arg(conf, "name")
        if not name:
            name = parse_conf_arg(conf, "default-name")
            if not name: # unnamed interface do not process
                return {}

        config["name"] = name
        disabled = parse_conf_arg(conf, "disabled")
        if disabled:
            config["disabled"] = True if disabled == "yes" else False
        return utils.remove_empties(config)
