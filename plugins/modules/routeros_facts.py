from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.kilip.routeros.plugins.module_utils.argspec.facts import FactsArgs
from ansible_collections.kilip.routeros.plugins.module_utils.facts.facts import Facts


def main():
    argument_spec = FactsArgs.argument_spec
    warnings = []
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    result = Facts(module).get_facts()
    ansible_facts, additional_warnings = result
    warnings.extend(additional_warnings)
    return module.exit_json(ansible_facts=ansible_facts, warnings=warnings)


if __name__ == "__main__":
    main()
