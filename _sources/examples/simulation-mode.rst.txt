Inspect or rehearse a plan without touching hardware ("simulation mode")
************************************************************************

Problem
=======

Check a plan for mistakes before running it on real hardware.

Approach
========

1. Display the steps of a plan and read through them to verify that they match
   our intention.
2. Execute the plan on "simulated hardware," Python objects that stand in for
   real motors and detectors but do not actually communicate with any hardware.

Example Solutions
=================

The ``bluesky.examples`` module includes simulated motors and detectors.

.. code-block:: python

    # Import simulated motors and a detector.
    from bluesky.examples import motor, motor1, motor2, det

    # This may already be imported in the configuration.
    from bluesky.plan_tools import print_summary
    from bluesky.plans import count, scan, outer_product_scan

.. ipython:: python
    :suppress:

    from bluesky.examples import motor, motor1, motor2, det
    from bluesky.plan_tools import print_summary
    from bluesky.plans import count, scan, outer_product_scan

Inspect plans
-------------

Use ``print_summary`` which translates the plan into a human-readable list
of steps.


.. ipython:: python

    print_summary(count([det]))
    print_summary(scan([det], motor, 1, 3, 3))
    print_summary(outer_product_scan([det], motor1, 1, 3, 3, motor2, 1, 2, 2, False))

Note that ``print_summary`` cannot be used on plans the require feedback from
the hardware, such as adaptively-spaced step scans.

Rehearse plans
--------------

Simply execute the plan as usual --- ``RE(plan)`` --- but define that plan
using the simulated motors and detectors from ``bluesky.examples`` instead of
the variables that represent real hardware.

.. code-block:: python

    RE(count([det]))  # executes the plan, 'reading' the simulated detector

To avoid saving data from these "rehearsal" runs, make a separate instance of
the RunEngine, and do not subscribe metadatastore.

.. code-block:: python

    SIM_RE = RunEngine({})
