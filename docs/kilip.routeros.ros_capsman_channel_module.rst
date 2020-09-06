.. _kilip.routeros.ros_capsman_channel_module

********************************
kilip.routeros.ros_capsman_channel
********************************

Version Added: **1.0.0**

RouterOS Submenu: **/caps-man channel**

.. contents::
   :local:
   :depth: 2



========
Synopsis
========


-  This modules manages CAPsMan Channels configuration on Mikrotik RouterOS network devices



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
  A dictionary for `/caps-man channel` options described in the table below

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table"><tr><th>Name</th><th>Choices/Default</th><th>Description</th></tr><tr><td><b>band</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              2ghz-b
                            </li><li>
                              2ghz-b/g
                            </li><li>
                              2ghz-b/g/n
                            </li><li>
                              2ghz-onlyg
                            </li><li>
                              2ghz-onlyn
                            </li><li>
                              5ghz-a
                            </li><li>
                              5ghz-a/n
                            </li><li>
                              5ghz-onlyn
                            </li></ul></td><td><p>Define operational radio frequency band and mode taken from hardware capability of wireless card</p></td></tr><tr><td><b>comment</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Short description of the Channel Group profile</p></td></tr><tr><td><b>extension_channel</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li>
                              Ce
                            </li><li>
                              Ceee
                            </li><li>
                              disabled
                            </li><li>
                              eC
                            </li><li>
                              eCee
                            </li><li>
                              eeCe
                            </li><li>
                              eeeC
                            </li></ul></td><td><p>Extension channel configuration. (E.g. Ce = extension channel is above Control channel, eC = extension channel is below Control channel)</p></td></tr><tr><td><b>frequency</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>Channel frequency value in MHz on which AP will operate.</p></td></tr><tr><td><b>name</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Descriptive name for the Channel Group Profile</p></td></tr><tr><td><b>save_selected</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td><ul style="margin: 0; padding: 0;"><li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li><li>
                              no
                            </li></ul></td><td><p>Saves selected channel for the CAP Radio - will select this channel after the CAP reconnects to CAPsMAN and use it till the channel Re-optimize is done for this CAP.</p></td></tr><tr><td><b>tx_power</b><div style="font-size: small"><span style="color: purple">int</span></div></td><td></td><td><p>TX Power for CAP interface (for the whole interface not for individual chains) in dBm. It is not possible to set higher than allowed by country regulations or interface. By default max allowed by country or interface is used.</p></td></tr><tr><td><b>width</b><div style="font-size: small"><span style="color: purple">str</span></div></td><td></td><td><p>Sets Channel Width in MHz. (E.g. 20, 40)</p></td></tr></table>



========
Examples
========




------------
Using merged
------------


**Before State**

.. code-block:: ssh

    [admin@MikroTik] > /caps-man channel export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man channel
    add name=test



**Configuration**


.. code-block:: yaml+jinja

    - name: Merge with device configuration
      kilip.routeros.ros_capsman_channel:
        config:
          - name: test
            save_selected: 'no'
          - name: new
            extension_channel: Ce
        state: merged
        
      

**Executed Command**


.. code-block:: ssh

    /caps-man channel set [ find name=test ] save-selected=no
    /caps-man channel add name=new extension-channel=Ce


**After State**


.. code-block:: ssh

    [admin@MikroTik] > /caps-man channel export
    # sep/06/2020 03:08:16 by RouterOS 6.47.2
    # software id =
    /caps-man channel add name=test save-selected=no add name=new extension-channel=Ce


