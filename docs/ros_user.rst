.. _ros_user_module:


ros_user -- Router User Group Management
========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Router user database stores the information such as username, password, allowed access addresses and group about router management personnel.






Parameters
----------

  state (optional, any, merged)
    Merged:
-  When Resource Exists:
   *  :ref:`ros_user <ros_user_module>` will update existing ``/user`` configuration
-  When Resource Not Exists:
   *  :ref:`ros_user <ros_user_module>` will create new ``/user``,
Replaced
-  When Resource Exists:
   *  :ref:`ros_user <ros_user_module>` will restore related ``/user`` to its default value.
   *  :ref:`ros_user <ros_user_module>` will update ``/user`` item using the passed ``argument_spec``.
-  When Resource Not Exists:
   *  :ref:`ros_user <ros_user_module>` will create new ``/user``
Overridden:
*  :ref:`ros_user <ros_user_module>` will remove any existing item in ``/user``
*  :ref:`ros_user <ros_user_module>` will create new item using value in the ``argument_spec``
Deleted:
----
*  If item exists :ref:`ros_user <ros_user_module>` will remove that item from ``/user`` configuration



  config (optional, list, None)
    A dictionary for L(ros_user)


    address (optional, str, None)
      Host or network address from which the user is allowed to log in



    group (optional, str, None)
      Name of the ` group <#User_Groups>`_ the user belongs to



    name (True, str, None)
      User name. Although it must start with an alphanumeric character, it may contain
"", "_", "." and "@" symbols.



    password (optional, str, None)
      User password. If not specified, it is left blank (hit [Enter] when logging
in). It conforms to standard Unix characteristics of passwords and may contain
letters, digits, "" and "_" symbols.



    last_logged_in (optional, str, None)
      Read-only field. Last time and date when user logged in.















Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

