Take baseline readings at the beginning and end
***********************************************

Problem
=======

Record the position or value of various motors or detectors at the beginning
and end of a plan --- a snapshot of the state of the hardware.

Approach
========

Customize a plan with the extra readings desired.

Example Solution
================

.. code-block:: python

    from bluesky.plans import baseline

    plan = baseline(scan([det], motor, 1, 5, 5), [motor, det])

If the same list of devices is often used, define a custom function bound to
that specific list:

.. code-block:: python

    # only specify the devices once, here
    my_baseline = partial(baseline, devices=[motor, det])

    plan = my_baseline(scan[det], motor, 1, 5, 5))

.. note:: 

    In simple cases, using ``baseline`` is equivalent to sandwiching its
    contents between two ``trigger_and_read`` plans.

    .. code-block:: python

        from bluesky.plans import pchain, trigger_and_read

        plan = pchain(trigger_and_read([motor, det], name='baseline'),
                    scan([det], motor, 1, 5, 5),
                    trigger_and_read([motor, det], name='baseline'))

    But if a plan involves multiple runs (multiple invocations of 'open_run'),
    ``baseline`` inserts a fresh baseline reading at the beginning and end of
    each run.

An optional ``name`` parameter, which defaults to ``'baseline'``, is a label
which makes it easy to retrieve this particular sequence of readings from the
databroker:

.. code-block:: python

    db.get_table(header, name='baseline')
