#!/usr/bin/python


"""
The module file for ros_capsman_configuration
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: ros_capsman_configuration
short_description: Manage configuration for C(/caps-man configuration)
description: This M(ros_capsman_configuration) module provides management for RouterOS C(/caps-man configuration).
version_added: 1.0.0
author: Anthonius Munthi (@kilip)
options:
    state:
        choices:
            - merged
            - replaced
            - overridden
            - deleted
        default: merged
        description: |
            Merged:
            -  When Resource Exists:
               *  M(ros_capsman_configuration) will update existing C(/caps-man configuration) configuration
            -  When Resource Not Exists:
               *  M(ros_capsman_configuration) will create new C(/caps-man configuration),
            Replaced
            -  When Resource Exists:
               *  M(ros_capsman_configuration) will restore related C(/caps-man configuration) to its default value.
               *  M(ros_capsman_configuration) will update C(/caps-man configuration) item using the passed C(argument_spec).
            -  When Resource Not Exists:
               *  M(ros_capsman_configuration) will create new C(/caps-man configuration)
            Overridden:
            *  M(ros_capsman_configuration) will remove any existing item in C(/caps-man configuration)
            *  M(ros_capsman_configuration) will create new item using value in the C(argument_spec)
            Deleted:
            ----
            *  If item exists M(ros_capsman_configuration) will remove that item from C(/caps-man configuration) configuration
    config:
        description: A dictionary for L(ros_capsman_configuration)
        type: list
        elements: dict
        suboptions:
            channel:
                type: str
                description: |
                    User defined list taken from Channel names (/caps-man channels)
            channel_band:
                type: str
                choices:
                    - 2ghz-b
                    - 2ghz-b/g
                    - 2ghz-b/g/n
                    - 2ghz-onlyg
                    - 2ghz-onlyn
                    - 5ghz-a
                    - 5ghz-a/n
                    - 5ghz-onlyn
                    - 5ghz-a/n/ac
                    - 5ghz-only-ac
                default: None
                description: |
                    Defines set of used channels.
            channel_control_channel_width:
                type: str
                choices:
                    - 40mhz-turbo
                    - 20mhz
                    - 10mhz
                    - 5mhz
                default: None
                description: |
                    Defines set of used channel widths.
            channel_extension_channel:
                type: str
                choices:
                    - ce
                    - ceee
                    - ec
                    - ecee
                    - eece
                    - eeec
                    - xx
                    - xxxx
                    - disabled
                default: None
                description: |
                    Extension channel configuration. (E.g. Ce = extension channel is above Control channel, eC = extension channel is below Control channel)
            channel_frequency:
                type: int
                description: |
                    Channel frequency value in MHz on which AP will operate. If left blank, CAPsMAN will automatically determine the best frequency that is least occupied.
            channel_reselect_interval:
                type: str
                description: |
                    Interval after which least occupied frequency is chosen. Works only if channel.frequency is left blank.
            channel_save_selected:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    If channel frequency is chosen automatically and channel.reselect-interval is used, then saves the last picked frequency.
            channel_secondary_frequency:
                type: str
                default: auto
                description: |
                    Specifies the second frequency that will be used for 80+80MHz configuration. Set it to Disabled in order to disable 80+80MHz capability.
            channel_skip_dfs_channels:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    If channel.frequency is left blank, the selection will skip DFS channels
            channel_tx_power:
                type: int
                description: |
                    TX Power for CAP interface (for the whole interface not for individual chains) in dBm. It is not possible to set higher than allowed by country regulations or interface. By default max allowed by country or interface is used.
            channel_width:
                type: str
                description: |
                    Sets Channel Width in MHz.
            comment:
                type: str
                description: |
                    Short description of the Configuration profile
            country:
                type: str
                default: no_country_set
                choices:
                    - name
                    - of
                    - the
                    - country
                    - no_country_set
                description: |
                    Limits available bands, frequencies and maximum transmit power for each frequency. Also specifies default value of scan-list. Value no_country_set is an FCC compliant set of channels.
            datapath:
                type: str
                description: |
                    User defined list taken from Datapath names (/caps-man datapath)
            datapath_bridge:
                type: str
                description: |
                    Bridge to which particular interface should be automatically added as port. Required only when local-forwarding is not used.
            datapath_bridge_cost:
                type: int
                description: |
                    bridge port cost to use when adding as bridge port
            datapath_bridge_horizon:
                type: int
                description: |
                    bridge horizon to use when adding as bridge port
            datapath_client_to_client_forwarding:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    controls if client-to-client forwarding between wireless clients connected to interface should be allowed, in local forwarding mode this function is performed by CAP, otherwise it is performed by CAPsMAN
            datapath_interface_list:
                type: str
            datapath_l2mtu:
                type: str
                description: |
                    set Layer2 MTU size
            datapath_local_forwarding:
                type: str
                default: no
                choices:
                    - yes
                    - no
                description: |
                    Controls forwarding mode. If disabled, all L2 and L3 data will be forwarded to CAPsMAN, and further forwarding decisions will be made only then.
                    Note, if disabled, make sure that each CAP interface MAC Address that participates in the same broadcast domain is unique (including local MACs, like Bridge-MAC).
            datapath_mtu:
                type: str
                description: |
                    set MTU size
            datapath_openflow_switch:
                type: str
                description: |
                    OpenFlow switch port (when enabled) to add interface to
            datapath_vlan_id:
                type: int
                description: |
                    VLAN ID to assign to interface if vlan-mode enables use of VLAN tagging
            datapath_vlan_mode:
                type: str
                choices:
                    - use-service-tag
                    - use-tag
                default: None
                description: |
                    Enables and specifies the type of VLAN tag to be assigned to the interface (causes all received data to get tagged with VLAN tag and allows the interface to only send out data tagged with given tag)
            disconnect_timeout:
                type: str
            distance:
                type: str
            frame_lifetime:
                type: str
            guard_interval:
                type: str
                default: any
                choices:
                    - any
                    - long
                description: |
                    Whether to allow the use of short guard interval (refer to 802.11n MCS specification to see how this may affect throughput). "any" will use either short or long, depending on data rate, "long" will use long only.
            hide_ssid:
                type: str
                choices:
                    - yes
                    - no
                default: None
                description: |
                    - yes - AP does not include SSID in the beacon frames and does not reply to probe requests that have broadcast SSID.
                    - no - AP includes SSID in the beacon frames and replies to probe requests that have broadcast SSID.
                    This property has effect only in AP mode. Setting it to yes can remove this network from the list of wireless networks that are shown by some client software. Changing this setting does not improve the security of the wireless network, because SSID is included in other frames sent by the AP.
            hw_protection_mode:
                type: str
            hw_retries:
                type: str
            installation:
                type: str
                default: any
                choices:
                    - any
                    - indoor
                    - outdoor
            keepalive_frames:
                type: str
                default: enabled
                choices:
                    - enabled
                    - disabled
            load_balancing_group:
                type: str
                description: |
                    Tags the interface to the load balancing group. For a client to connect to interface in this group, the interface should have the same number of already connected clients as all other interfaces in the group or smaller. Useful in setups where ranges of CAPs mostly overlap.
            max_sta_count:
                type: int
                description: |
                    Maximum number of associated clients.
            mode:
                type: str
                default: ap
                description: |
                    Set operational mode. Only ap currently supported.
            multicast_helper:
                type: str
                default: default
                choices:
                    - default
                    - disabled
                    - full
                description: |
                    When set to full multicast packets will be sent with unicast destination MAC address, resolving L( multicast problem,/wiki/Manual:Multicast_detailed_example#Multicast_and_Wireless) on a wireless link. This option should be enabled only on the access point, clients should be configured in station-bridge mode. Available starting from v5.15.
                    - disabled - disables the helper and sends multicast packets with multicast destination MAC addresses
                    - full - all multicast packet mac address are changed to unicast mac addresses prior sending them out
                    - default - default choice that currently is set to disabled. Value can be changed in future releases.
            name:
                type: str
                required: True
                description: |
                    Descriptive name for the Configuration Profile
            rates:
                type: str
                description: |
                    User defined list taken from Rates names (/caps-man rates)
            rates_basic:
                type: str
                choices:
                    - 1mbps
                    - 2mbps
                    - 5.5mbps
                    - 6mbps
                    - 11mbps
                    - 11mbps
                    - 12mbps
                    - 18mbps
                    - 24mbps
                    - 36mbps
                    - 48mbps
                    - 54mbps
                default: None
            rates_supported:
                type: str
                choices:
                    - 1mbps
                    - 2mbps
                    - 5.5mbps
                    - 6mbps
                    - 11mbps
                    - 11mbps
                    - 12mbps
                    - 18mbps
                    - 24mbps
                    - 36mbps
                    - 48mbps
                    - 54mbps
                default: None
            rates_ht_basic_mcs:
                type: str
                choices:
                    - list
                    - of
                    - (mcs-0
                    - mcs-1
                    - mcs-2
                    - mcs-3
                    - mcs-4
                    - mcs-5
                    - mcs-6
                    - mcs-7
                    - mcs-8
                    - mcs-9
                    - mcs-10
                    - mcs-11
                    - mcs-12
                    - mcs-13
                    - mcs-14
                    - mcs-15
                    - mcs-16
                    - mcs-17
                    - mcs-18
                    - mcs-19
                    - mcs-20
                    - mcs-21
                    - mcs-22
                    - mcs-23)
                default: None
                description: |
                    L(Modulation and Coding Schemes,http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates) that every connecting client must support. Refer to 802.11n for MCS specification.
            rates_ht_supported_mcs:
                type: str
                choices:
                    - list
                    - of
                    - (mcs-0
                    - mcs-1
                    - mcs-2
                    - mcs-3
                    - mcs-4
                    - mcs-5
                    - mcs-6
                    - mcs-7
                    - mcs-8
                    - mcs-9
                    - mcs-10
                    - mcs-11
                    - mcs-12
                    - mcs-13
                    - mcs-14
                    - mcs-15
                    - mcs-16
                    - mcs-17
                    - mcs-18
                    - mcs-19
                    - mcs-20
                    - mcs-21
                    - mcs-22
                    - mcs-23)
                default: None
                description: |
                    L(Modulation and Coding Schemes,http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates) that this device advertises as supported. Refer to 802.11n for MCS specification.
            rates_vht_basic_mcs:
                type: str
                choices:
                    - none
                    - mcs
                    - 0-7
                    - mcs
                    - 0-8
                    - mcs
                    - 0-9
                default: None
                description: |
                    L(Modulation and Coding Schemes,http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed) that every connecting client must support. Refer to 802.11ac for MCS specification. You can set MCS interval for each of Spatial Stream
                    - none - will not use selected Spatial Stream
                    - MCS 0-7 - client must support MCS-0 to MCS-7
                    - MCS 0-8 - client must support MCS-0 to MCS-8
                    - MCS 0-9 - client must support MCS-0 to MCS-9
            rates_vht_supported_mcs:
                type: str
                choices:
                    - none
                    - mcs
                    - 0-7
                    - mcs
                    - 0-8
                    - mcs
                    - 0-9
                default: None
                description: |
                    L(Modulation and Coding Schemes,http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed) that this device advertises as supported. Refer to 802.11ac for MCS specification. You can set MCS interval for each of Spatial Stream
                    - none - will not use selected Spatial Stream
                    - MCS 0-7 - devices will advertise as supported MCS-0 to MCS-7
                    - MCS 0-8 - devices will advertise as supported MCS-0 to MCS-8
                    - MCS 0-9 - devices will advertise as supported MCS-0 to MCS-9
            rx_chains:
                type: str
                description: |
                    Which antennas to use for receive.
            security:
                type: str
                description: |
                    Name of security configuration from /caps-man security
            security_authentication_types:
                type: str
                description: |
                    Specify the type of Authentication from wpa-psk, wpa2-psk, wpa-eap or wpa2-eap
            security_disable_pmkid:
                type: str
            security_eap_methods:
                type: str
                choices:
                    - eap-tls
                    - passthrough
                default: None
                description: |
                    - eap-tls - Use built-in EAP TLS authentication.
                    - passthrough - Access point will relay authentication process to the RADIUS server.
            security_eap_radius_accounting:
                type: str
                description: |
                    specifies if RADIUS traffic accounting should be used if RADIUS authentication gets done for this client
            security_encryption:
                type: list
                elements: str
                choices:
                    - aes-ccm
                    - tkip
                default: None
                description: |
                    Set type of unicast encryption algorithm used
            security_group_encryption:
                type: str
                default: aes-ccm
                choices:
                    - aes-ccm
                    - tkip
                description: |
                    Access Point advertises one of these ciphers, multiple values can be selected. Access Point uses it to encrypt all broadcast and multicast frames. Client attempts connection only to Access Points that use one of the specified group ciphers.
                    - tkip - Temporal Key Integrity Protocol - encryption protocol, compatible with legacy WEP equipment, but enhanced to correct some of the WEP flaws.
                    - aes-ccm - more secure WPA encryption protocol, based on the reliable AES (Advanced Encryption Standard). Networks free of WEP legacy should use only this cipher.
            security_group_key_update:
                type: str
                default: 5m
                description: |
                    Controls how often Access Point updates the group key. This key is used to encrypt all broadcast and multicast frames. property only has effect for Access Points.
            security_passphrase:
                type: str
                description: |
                    WPA or WPA2 pre-shared key
            security_tls_certificate:
                type: str
                choices:
                    - none
                    - name
                default: None
                description: |
                    Access Point always needs a certificate when security.tls-mode is set to value other than no-certificates.
            security_tls_mode:
                type: str
                choices:
                    - verify-certificate
                    - dont-verify-certificate
                    - no-certificates
                    - verify-certificate-with-crl
                default: None
                description: |
                    This property has effect only when security.eap-methods contains eap-tls.
                    - verify-certificate - Require remote device to have valid certificate. Check that it is signed by known certificate authority. No additional identity verification is done. Certificate may include information about time period during which it is valid. If router has incorrect time and date, it may reject valid certificate because routers clock is outside that period. See also the L( Certificates,/wiki/Manual:System/Certificates) configuration.
                    - dont-verify-certificate - Do not check certificate of the remote device. Access Point will not require client to provide certificate.
                    - no-certificates - Do not use certificates. TLS session is established using 2048 bit anonymous Diffie-Hellman key exchange.
                    - verify-certificate-with-crl - Same as verify-certificate but also checks if the certificate is valid by checking the Certificate Revocation List.
            ssid:
                type: str
                description: |
                    SSID (service set identifier) is a name broadcast in the beacons that identifies wireless network.
            tx_chains:
                type: str
                description: |
                    Which antennas to use for transmit.

"""

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.resources.capsman.configuration import (
    CapsmanConfigurationResource,
)
from ..module_utils.config.resource import ResourceConfig


def main():
    module = AnsibleModule(
        argument_spec=CapsmanConfigurationResource.argument_spec
    )
    result = ResourceConfig(
        module, CapsmanConfigurationResource
    ).execute_module()
    return module.exit_json(**result)


if __name__ == "__main__":
    main()
