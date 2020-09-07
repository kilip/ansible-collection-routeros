.. _kilip.routeros.kilip.routeros.ros_capsman_manager_module

********************************
kilip.routeros.kilip.routeros.ros_capsman_manager
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/caps-man manager**

.. contents::
   :local:
   :depth: 2

========
Synopsis
========

-  This modules manages CAPsMan Maanager Setting on Mikrotik RouterOS network devices

==========
Parameters
==========

state
  | **choices**: present, reset
  | **default**: present
  | **required**: False
  | **type**: str
  Available state for this module

config
  | **type**: list
  | **elements**: dict
  A dictionary for `/caps-man manager` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>ca_certificate</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Device CA certificate</p></td></tr><tr><td><b>certificate</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              auto
                            </li><li>
                              certificate name
                            </li><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li></ul></td><td><p>Device certificate</p></td></tr><tr><td><b>enabled</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Disable or enable CAPsMAN functionality</p></td></tr><tr><td><b>package_path</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Folder location for the RouterOS packages. For example, use '/upgrade' to specify the upgrade folder from the files section. If empty string is set, CAPsMAN can use built-in RouterOS packages, note that in this case only CAPs with the same architecture as CAPsMAN will be upgraded.</p></td></tr><tr><td><b>require_peer_certificate</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li><li>
                              yes
                            </li></ul></td><td><p>Require all connecting CAPs to have a valid certificate</p></td></tr><tr><td><b>upgrade_policy</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li><li>
                              require-same-version
                            </li><li>
                              suggest-same-upgrade
                            </li></ul></td><td><p>Upgrade policy options</p><ul><li>none - do not perform upgrade</li><li>require-same-version - CAPsMAN suggest to upgrade the CAP RouterOS version and if it fails it will not provision the CAP. (Manual provision is still possible)</li><li>suggest-same-version - CAPsMAN suggests to upgrade the CAP RouterOS version and if it fails it will still be provisioned</li></ul></td></tr></table>

========
Examples
========

-------------------
Using Present State
-------------------

**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /caps-man manager export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man manager
    set ca-certificate=none \
        certificate=none \
        enabled=no \
        package-path="" \
        require-peer-certificate=no \
        upgrade-policy=none

**Configuration**

.. code-block:: yaml+jinja

    - name: Update Settings
      kilip.routeros.kilip.routeros.ros_capsman_manager:
        state: present
        config:
          ca_certificate: auto
          enabled: 'yes'

**Executed Command**

.. code-block:: ssh

    /caps-man manager set ca-certificate=auto enabled=yes

**After State**

.. code-block:: ssh

    [admin@MikroTik] > /caps-man manager export verbose
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man manager
    set ca-certificate=none \
        certificate=auto \
        enabled=yes \
        package-path="" \
        require-peer-certificate=no \
        upgrade-policy=none
