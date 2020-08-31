.. _ros_capsman_manager_module:


ros_capsman_manager -- Manage configuration for ``/caps-man manager``
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_capsman_manager <ros_capsman_manager_module>` module provides management for RouterOS ``/caps-man manager``.






Parameters
----------

  state (optional, any, None)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_capsman_manager <ros_capsman_manager_module>` will update existing ``/caps-man manager`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_capsman_manager <ros_capsman_manager_module>` will create new ``/caps-man manager``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_capsman_manager <ros_capsman_manager_module>` will restore related ``/caps-man manager`` to its default value.
   *  :ref:`ros_capsman_manager <ros_capsman_manager_module>` will update ``/caps-man manager`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_capsman_manager <ros_capsman_manager_module>` will create new ``/caps-man manager``
Overridden:
*  :ref:`ros_capsman_manager <ros_capsman_manager_module>` will remove any existing item in ``/caps-man manager``
*  :ref:`ros_capsman_manager <ros_capsman_manager_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_capsman_manager <ros_capsman_manager_module>` will remove that item from ``/caps-man manager`` configuration



  config (optional, any, None)
    A dictionary for L(ros_capsman_manager)


    enabled (optional, str, False)
      Disable or enable CAPsMAN functionality



    certificate (optional, str, None)
      Device certificate



    ca_certificate (optional, str, None)
      Device CA certificate



    require_peer_certificate (optional, str, False)
      Require all connecting CAPs to have a valid certificate



    package_path (optional, str, None)
      Folder location for the RouterOS packages. For example, use "/upgrade" to
specify the upgrade folder from the files section. If empty string is set,
CAPsMAN can use built-in RouterOS packages, note that in this case only CAPs
with the same architecture as CAPsMAN will be upgraded.



    upgrade_policy (optional, str, None)
      Upgrade policy options
- none - do not perform upgrade
- require-same-version - CAPsMAN suggest to upgrade the CAP RouterOS version and
if it fails it will not provision the CAP. (Manual provision is still possible)
- suggest-same-version - CAPsMAN suggests to upgrade the CAP RouterOS version
and if it fails it will still be provisioned















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

