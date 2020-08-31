.. _ros_capsman_provisioning_module:


ros_capsman_provisioning -- Manage configuration for ``/caps-man provisioning``
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_capsman_provisioning <ros_capsman_provisioning_module>` module provides management for RouterOS ``/caps-man provisioning``.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_capsman_provisioning <ros_capsman_provisioning_module>` will update existing ``/caps-man provisioning`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_capsman_provisioning <ros_capsman_provisioning_module>` will create new ``/caps-man provisioning``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_capsman_provisioning <ros_capsman_provisioning_module>` will restore related ``/caps-man provisioning`` to its default value.
   *  :ref:`ros_capsman_provisioning <ros_capsman_provisioning_module>` will update ``/caps-man provisioning`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_capsman_provisioning <ros_capsman_provisioning_module>` will create new ``/caps-man provisioning``
Overridden:
*  :ref:`ros_capsman_provisioning <ros_capsman_provisioning_module>` will remove any existing item in ``/caps-man provisioning``
*  :ref:`ros_capsman_provisioning <ros_capsman_provisioning_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_capsman_provisioning <ros_capsman_provisioning_module>` will remove that item from ``/caps-man provisioning`` configuration



  config (optional, list, None)
    A dictionary for L(ros_capsman_provisioning)


    action (optional, str, None)
      Action to take if rule matches are specified by the following settings:
- create-disabled - create disabled static interfaces for radio. I.e., the
interfaces will be bound to the radio, but the radio will not be operational
until the interface is manually enabled;
- create-enabled - create enabled static interfaces. I.e., the interfaces will
be bound to the radio and the radio will be operational;
- create-dynamic-enabled - create enabled dynamic interfaces. I.e., the
interfaces will be bound to the radio, and the radio will be operational;
- none - do nothing, leaves radio in non-provisioned state;



    comment (optional, str, None)
      Short description of the Provisioning rule



    common_name_regexp (optional, str, None)
      Regular expression to match radios by common name. Each CAPs common name
identifier can be found under "/caps-man radio" as value "REMOTE-CAP-NAME"



    hw_supported_modes (optional, str, None)
      Match radios by supported wireless modes



    identity_regexp (optional, str, None)
      Regular expression to match radios by router identity



    ip_address_ranges (optional, str, None)
      Match CAPs with IPs within configured address range.



    master_configuration (optional, str, None)
      If action specifies to create interfaces, then a new master interface with its
configuration set to this configuration profile will be created



    name_format (optional, str, cap)
      specify the syntax of the CAP interface name creation
- cap - default name
- identity - CAP boards system identity name
- prefix - name from the name-prefix value
- prefix-identity - name from the name-prefix value and the CAP boards system
identity name



    name_prefix (optional, str, None)
      name prefix which can be used in the name-format for creating the CAP interface
names



    radio_mac (optional, str, 00:00:00:00:00:00)
      MAC address of radio to be matched, empty MAC (00:00:00:00:00:00) means match
all MAC addresses



    slave_configurations (optional, str, None)
      If action specifies to create interfaces, then a new slave interface for each
configuration profile in this list is created.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

