.. _kilip.routeros.ros_capsman_provisioning_module

********************************
kilip.routeros.ros_capsman_provisioning
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/caps-man provisioning**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This modules manages CAPsMan Provisioning on Mikrotik RouterOS network devices



==========
Parameters
==========


state
  | **choices**: merged, replaced, overridden, deleted
  | **default**: merged
  | **required**: False
  | **type**: str
  Available state for this module

config
  | **type**: list
  | **elements**: dict
  A dictionary for `/caps-man provisioning` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>action</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              create-disabled
                            </li><li>
                              create-dynamic-enabled
                            </li><li>
                              create-enabled
                            </li><li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li></ul></td><td><p>Action to take if rule matches are specified by the following settings:</p><ul><li><strong>create-disabled</strong> - create disabled static interfaces for radio. I.e., the interfaces will be bound to the radio, but the radio will not be operational until the interface is manually enabled;</li><li><strong>create-enabled</strong> - create enabled static interfaces. I.e., the interfaces will be bound to the radio and the radio will be operational;</li><li><strong>create-dynamic-enabled</strong> - create enabled dynamic interfaces. I.e., the interfaces will be bound to the radio, and the radio will be operational;</li><li><strong>none</strong> - do nothing, leaves radio in non-provisioned state;</li></ul></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Short description of the Provisioning rule</p></td></tr><tr><td><b>common_name_regexp</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Regular expression to match radios by common name. Each CAP's common name identifier can be found under '/caps-man radio' as value 'REMOTE-CAP-NAME'</p></td></tr><tr><td><b>hw_supported_modes</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              a
                            </li><li>
                              a-turbo
                            </li><li>
                              ac
                            </li><li>
                              an
                            </li><li>
                              b
                            </li><li>
                              g
                            </li><li>
                              g-turbo
                            </li><li>
                              gn
                            </li></ul></td><td><p>Match radios by supported wireless modes</p></td></tr><tr><td><b>identity_regexp</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Regular expression to match radios by router identity</p></td></tr><tr><td><b>ip_address_ranges</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Match CAPs with IPs within configured address range.</p></td></tr><tr><td><b>master_configuration</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>If <strong>action</strong> specifies to create interfaces, then a new master interface with its configuration set to this configuration profile will be created</p></td></tr><tr><td><b>name_format</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>cap</b>&nbsp;&larr;</div></li><li>
                              identity
                            </li><li>
                              prefix
                            </li><li>
                              prefix-identity
                            </li></ul></td><td><p>specify the syntax of the CAP interface name creation</p><ul><li>cap - default name</li><li>identity - CAP boards system identity name</li><li>prefix - name from the name-prefix value</li><li>prefix-identity - name from the name-prefix value and the CAP boards system identity name</li></ul></td></tr><tr><td><b>name_prefix</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>name prefix which can be used in the name-format for creating the CAP interface names</p></td></tr><tr><td><b>radio_mac</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>MAC address of radio to be matched, empty MAC (00:00:00:00:00:00) means match all MAC addresses</p></td></tr><tr><td><b>slave_configurations</b><div style="font-size: small"><span style="color: purple">list</span></div></td><td></td><td><p>If <strong>action</strong> specifies to create interfaces, then a new slave interface for each configuration profile in this list is created.</p></td></tr></table>



========
Examples
========




------------------
Using merged state
------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /caps-man provisioning export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man provisioning
    add comment=test



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge with device configuration
      kilip.routeros.ros_capsman_provisioning:
        state: merged
        config:
          - comment: test
            action: create-disabled
          - comment: 'Olympus Wireless Network'
            identity_regexp: olympus-
            master_configuration: olympus-network
            name_format: identity
            slave_configurations:
              - troy-network
              - gaia-network
            action: create-enabled
        
      

**Executed Command**


.. code-block:: ssh

    /caps-man provisioning set [ find comment=test ] action=create-disabled
    /caps-man provisioning add action=create-enabled comment="Olympus Wireless Network" identity-regexp=olympus- master-configuration=olympus-network name-format=identity slave-configurations=troy-network,gaia-network


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /caps-man provisioning export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man provisioning
    add comment=test action=create-disabled
    add comment="Olympus Wireless Network" \
        identity-regexp=olympus- \
        master-configuration=olympus-network \
        name-format=identity \
        slave-configurations=troy-network,gaia-network




-------------------
Using deleted state
-------------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /caps-man provisioning export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man provisioning
    add comment=test



**Configuration**


.. code-block:: yaml+jinja

    - name: Delete provisioning config
      kilip.routeros.ros_capsman_provisioning:
        state: deleted
        config:
          - comment: test
        
      

**Executed Command**


.. code-block:: ssh

    /caps-man provisioning remove [ find comment=test ]
    /system script run ansible-remove-invalid


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /caps-man provisioning export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    # empty caps-man provisioning config


