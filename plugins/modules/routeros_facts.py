from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.facts.facts import Facts


def main():
    argument_spec = {
        "gather_subset": dict(
            default=["!config"], type="list", elements="str"
        ),
        "gather_network_resources": dict(type="list", elements="str"),
    }
    warnings = []
    module = AnsibleModule(argument_spec=argument_spec)

    result = Facts(module).get_facts()
    ansible_facts, additional_warnings = result
    warnings.extend(additional_warnings)
    return module.exit_json(ansible_facts=ansible_facts, warnings=warnings)


if __name__ == "__main__":
    main()
