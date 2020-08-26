from __future__ import absolute_import, division, print_function

__metaclass__ = type


import re
from ansible.module_utils.six import iteritems
from ansible_collections.community.network.plugins.module_utils.network.routeros.routeros import (
    run_commands,
)


class FactsBase(object):
    COMMANDS = list()

    def __init__(self, module):
        self.module = module
        self.facts = dict()
        self.warnings = list()
        self.responses = None

    def populate(self):
        self.responses = run_commands(
            self.module, commands=self.COMMANDS, check_rc=False
        )

    def run(self, cmd):
        return run_commands(self.module, commands=cmd, check_rc=False)


class Default(FactsBase):
    COMMANDS = [
        "/system identity print without-paging",
        "/system resource print without-paging",
        "/system routerboard print without-paging",
    ]

    def populate(self):
        super(Default, self).populate()
        data = self.responses[0]
        if data:
            self.facts["hostname"] = self.parse_hostname(data)

        data = self.responses[1]
        if data:
            self.facts["version"] = self.parse_version(data)

        data = self.responses[2]
        if data:
            self.facts["model"] = self.parse_model(data)
            self.facts["serialnum"] = self.parse_serialnum(data)

    def parse_hostname(self, data):
        match = re.search(r"name:\s(.*)\s*$", data, re.M)
        if match:
            return match.group(1)

    def parse_version(self, data):
        match = re.search(r"version:\s(.*)\s*$", data, re.M)
        if match:
            return match.group(1)

    def parse_model(self, data):
        match = re.search(r"model:\s(.*)\s*$", data, re.M)
        if match:
            return match.group(1)

    def parse_serialnum(self, data):
        match = re.search(r"serial-number:\s(.*)\s*$", data, re.M)
        if match:
            return match.group(1)


class Hardware(FactsBase):
    COMMANDS = ["/system resource print without-paging"]

    def populate(self):
        super(Hardware, self).populate()
        data = self.responses[0]
        if data:
            self.parse_filesystem_info(data)
            self.parse_memory_info(data)

    def parse_filesystem_info(self, data):
        match = re.search(r"free-hdd-space:\s(.*)([KMG]iB)", data, re.M)
        if match:
            self.facts["spacefree_mb"] = self.to_megabytes(match)
        match = re.search(r"total-hdd-space:\s(.*)([KMG]iB)", data, re.M)
        if match:
            self.facts["spacetotal_mb"] = self.to_megabytes(match)

    def parse_memory_info(self, data):
        match = re.search(r"free-memory:\s(\d+\.?\d*)([KMG]iB)", data, re.M)
        if match:
            self.facts["memfree_mb"] = self.to_megabytes(match)
        match = re.search(r"total-memory:\s(\d+\.?\d*)([KMG]iB)", data, re.M)
        if match:
            self.facts["memtotal_mb"] = self.to_megabytes(match)

    def to_megabytes(self, data):
        if data.group(2) == "KiB":
            return float(data.group(1)) / 1024
        elif data.group(2) == "MiB":
            return float(data.group(1))
        elif data.group(2) == "GiB":
            return float(data.group(1)) * 1024
        else:
            return None


class Config(FactsBase):
    COMMANDS = ["/export"]

    def populate(self):
        super(Config, self).populate()
        data = self.responses[0]
        if data:
            self.facts["config"] = data


class Interfaces(FactsBase):
    COMMANDS = [
        "/interface print detail without-paging",
        "/ip address print detail without-paging",
        "/ipv6 address print detail without-paging",
        "/ip neighbor print detail without-paging",
    ]

    DETAIL_RE = re.compile(
        r"([\w\d\-]+)=\"?(\w{3}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}|[\w\d\-\.:/]+)"
    )
    WRAPPED_LINE_RE = re.compile(r"^\s+(?!\d)")

    def populate(self):
        super(Interfaces, self).populate()

        self.facts["interfaces"] = dict()
        self.facts["all_ipv4_addresses"] = list()
        self.facts["all_ipv6_addresses"] = list()
        self.facts["neighbors"] = list()

        data = self.responses[0]
        if data:
            interfaces = self.parse_interfaces(data)
            self.populate_interfaces(interfaces)

        data = self.responses[1]
        if data:
            data = self.parse_detail(data)
            self.populate_addresses(data, "ipv4")

        data = self.responses[2]
        if data:
            data = self.parse_detail(data)
            self.populate_addresses(data, "ipv6")

        data = self.responses[3]
        if data:
            self.facts["neighbors"] = list(self.parse_detail(data))

    def populate_interfaces(self, data):
        for key, value in iteritems(data):
            self.facts["interfaces"][key] = value

    def populate_addresses(self, data, family):
        for value in data:
            key = value["interface"]
            if family not in self.facts["interfaces"][key]:
                self.facts["interfaces"][key][family] = list()
            addr, subnet = value["address"].split("/")
            ip = dict(address=addr.strip(), subnet=subnet.strip())
            self.add_ip_address(addr.strip(), family)
            self.facts["interfaces"][key][family].append(ip)

    def add_ip_address(self, address, family):
        if family == "ipv4":
            self.facts["all_ipv4_addresses"].append(address)
        else:
            self.facts["all_ipv6_addresses"].append(address)

    def preprocess(self, data):
        preprocessed = list()
        for line in data.split("\n"):
            if len(line) == 0 or line[:5] == "Flags":
                continue
            elif not re.match(self.WRAPPED_LINE_RE, line):
                preprocessed.append(line)
            else:
                preprocessed[-1] += line
        return preprocessed

    def parse_interfaces(self, data):
        facts = dict()
        data = self.preprocess(data)
        for line in data:
            parsed = dict(re.findall(self.DETAIL_RE, line))
            if "name" not in parsed:
                continue
            facts[parsed["name"]] = dict(re.findall(self.DETAIL_RE, line))
        return facts

    def parse_detail(self, data):
        data = self.preprocess(data)
        for line in data:
            parsed = dict(re.findall(self.DETAIL_RE, line))
            if "interface" not in parsed:
                continue
            yield parsed
