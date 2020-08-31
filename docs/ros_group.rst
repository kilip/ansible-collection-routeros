.. _ros_group_module:


ros_group -- Router User Group Management
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The router user groups provide a convenient way to assign different permissions and access rights to different user classes.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_group <ros_group_module>` will update existing ``/user group`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_group <ros_group_module>` will create new ``/user group``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_group <ros_group_module>` will restore related ``/user group`` to its default value.
   *  :ref:`ros_group <ros_group_module>` will update ``/user group`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_group <ros_group_module>` will create new ``/user group``
Overridden:
*  :ref:`ros_group <ros_group_module>` will remove any existing item in ``/user group``
*  :ref:`ros_group <ros_group_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_group <ros_group_module>` will remove that item from ``/user group`` configuration



  config (optional, list, None)
    A dictionary for L(ros_group)


    name (True, str, None)
      The name of the user group



    policy (optional, list, None)
      List of allowed policies:
Login policies:
- local - policy that grants rights to log in locally via console
- telnet - policy that grants rights to log in remotely via telnet
- ssh - policy that grants rights to log in remotely via secure shell protocol
- web - policy that grants rights to log in remotely via WebFig.
- winbox - policy that grants rights to log in remotely via WinBox and bandwidth
test authentication
- password - policy that grants rights to change the password
- api - grants rights to access router via API.
- tikapp - policy that grants rights to log in remotely via Tik-App.
- dude - grants rights to log in to dude server.
- ftp - policy that grants full rights to log in remotely via FTP, to
read/write/erase files and to transfer files from/to the router. Should be used
together with read/write policies.
- romon - policy that grants rights to connect to RoMon server.
Config Policies:
- reboot - policy that allows rebooting the router
- read - policy that grants read access to the routers configuration. All
console commands that do not alter routers configuration are allowed. Doesnt
affect FTP
- write - policy that grants write access to the routers configuration, except
for user management. This policy does not allow to read the configuration, so
make sure to enable read policy as well
- policy - policy that grants user management rights. Should be used together
with write policy. Allows also to see global variables created by other users
(requires also test policy).
- test - policy that grants rights to run ping, traceroute, bandwidth-test,
wireless scan, snooper and other test commands
- sensitive - grants rights to change "hide sensitive" option, if this policy is
disabled sensitive information is not displayed, see below list as to what is
regarded as sensitive.
- sniff - policy that grants rights to use packet sniffer tool.



    skin (optional, str, default)
      Used ` skin </wiki/Manual:Webfig#Skins>`_ for WebFig















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

