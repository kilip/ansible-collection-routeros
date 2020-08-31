.. _ros_facts_module:


ros_facts -- Gather facts for routeros configuration
====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This :ref:`ros_facts <ros_facts_module>` module provides gathering facts for RouterOS.






Parameters
----------

  gather_subset (False, list, !config)
    When supplied, this argument restricts the facts collected to a given subset.

    Possible values for this argument include ``all``, ``min``, ``interface``

    Specify a list of values to include a larger subset.

    Use a value with an initial ``!`` to collect all facts except that subset.


  gather_network_resources (optional, list, None)
    When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, vlans etc. Can specify a list of values to include a larger subset. Values can also be used with an initial ``:ref:`! <!_module>``` to specify that a specific subset should not be collected. Valid subsets are 'all', 'interface'













Status
------





Authors
~~~~~~~

- Anthonius Munthi (@kilip)

