from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.six import iteritems

ANSIBLE_REMOVE_INVALID_SCRIPT_NAME = "ansible-remove-invalid"


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


def key_to_routeros(key, prefixes=None):
    if prefixes is None:
        prefixes = list()

    if prefixes:
        for prefix in prefixes:
            if -1 != key.find(prefix):
                key = key.replace(prefix + "_", prefix + ".")
                break

    return key.replace("_", "-").strip()


def value_to_routeros(value):
    if type(value) is bool:
        value = "yes" if value else "no"

    if type(value) == str and " " in value:
        value = '"' + value + '"'

    if value == "":
        value = '""'
    return value


def list_to_routeros(value):
    converted = []
    for val in value:
        converted.append(str(val))
    return ",".join(converted)


def find_existing_resource(keys, want, have):
    """
    Find existing resource by comparing keys
    :param want: a resour
    :param have:
    :return:
    """
    resource = dict()
    for each in have:
        exist = True
        for key in keys:
            if each[key] != want[key]:
                exist = False
        if exist:
            resource = each

    return resource


def filter_dict_having_none_value(want, have):
    # Generate dict with have dict value which is None in want dict
    test_dict = dict()
    name = want.get("name")
    if name:
        test_dict["name"] = name
    diff_ip = False
    for k, v in iteritems(want):
        if isinstance(v, dict):
            for key, value in iteritems(v):
                test_key_dict = dict()
                if value is None:
                    dict_val = have.get(k).get(key)
                    test_key_dict.update({key: dict_val})
                elif (
                    k == "ipv6"
                    and value.lower() != have.get(k)[0].get(key).lower()
                ):
                    # as multiple IPV6 address can be configured on same
                    # interface, for replace state in place update will
                    # actually create new entry, which isn't as expected
                    # for replace state, so in case of IPV6 address
                    # every time 1st delete the existing IPV6 config and
                    # then apply the new change
                    dict_val = have.get(k)[0].get(key)
                    test_key_dict.update({key: dict_val})
                if test_key_dict:
                    test_dict.update({k: test_key_dict})
        if isinstance(v, list):
            for key, value in iteritems(v[0]):
                test_key_dict = dict()
                if value is None:
                    if have.get(k) and key in have.get(k):
                        dict_val = have.get(k)[0].get(key)
                        test_key_dict.update({key: dict_val})
                elif have.get(k):
                    if (
                        k == "ipv6"
                        and value.lower() != have.get(k)[0].get(key).lower()
                    ):
                        dict_val = have.get(k)[0].get(key)
                        test_key_dict.update({key: dict_val})
                if test_key_dict:
                    test_dict.update({k: test_key_dict})
            # below conditions checks are added to check if
            # secondary IP is configured, if yes then delete
            # the already configured IP if want and have IP
            # is different else if it's same no need to delete
            for each in v:
                if each.get("secondary"):
                    want_ip = each.get("address").split("/")
                    have_ip = have.get("ipv4")
                    if (
                        len(want_ip) > 1
                        and have_ip
                        and have_ip[0].get("secondary")
                    ):
                        have_ip = have_ip[0]["address"].split(" ")[0]
                        if have_ip != want_ip[0]:
                            diff_ip = True
                    if each.get("secondary") and diff_ip is True:
                        test_key_dict.update({"secondary": True})
                    test_dict.update({"ipv4": test_key_dict})
        if v is None:
            val = have.get(k)
            test_dict.update({k: val})
    return test_dict


def remove_duplicate_interface(commands):
    # Remove duplicate interface from commands
    set_cmd = []
    for each in commands:
        if "interface" in each:
            if each not in set_cmd:
                set_cmd.append(each)
        else:
            set_cmd.append(each)

    return set_cmd


def gen_remove_invalid_resource():
    script_name = ANSIBLE_REMOVE_INVALID_SCRIPT_NAME
    command = "/system script run {0}".format(script_name)
    return command
