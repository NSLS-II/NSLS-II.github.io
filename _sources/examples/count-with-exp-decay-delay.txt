Take successive readings spaced exponentially in time or space
**************************************************************

Problem
=======

Read a detector (or detectors) multiple times, with successive readings spaced
1, 2, 4, 8, 16, ... seconds apart. Or, similarly, move a motor is steps with
an exponential spacing.

Approach
========

We will define an iterator that specifies the delays between readings.

Example Solution
================

Use the built-in function ``range`` to generate sequential integers.

.. code-block:: python

    range(5)  # generates 0, 1, 2, 3, 4

Modify each element like so:

.. code-block:: python

    (2**i for i in range(4))  # generates 1, 2, 4, 8, 16

The above is called a *generator comprehension*. It evaluates "lazily",
computing the result for one element at a time.

We can pass this expression to the ``delay`` parameter of a ``count`` plan.

.. ipython:: python
    :suppress:

    from bluesky.examples import det  # or use an actual detector, of course
    from bluesky.callbacks import LiveTable
    from bluesky.plans import count
    from bluesky import RunEngine
    RE = RunEngine({})

.. code-block:: python
    
    from bluesky.plans import count
    from bluesky.callbacks import LiveTable

    plan = count([det], num=None, delay=(2**i for i in range(4)))

The setting ``num=None`` means, "Run until the end of list of delays."
Let's attach a ``LiveTable`` to the output and watch it in action. Notice
the readings' timestamps.

.. ipython:: python
    :suppress:

    plan = count([det], num=None, delay=(2**i for i in range(4)))


.. ipython:: python

    RE(plan, LiveTable([det]))

We could use the same principle to arrange readings in *space* instead of
time using a ``list_scan``.

.. code-block:: python

    from blusky.plans import list_scan

    # Take readings with motor moved positioned at 1, 2, 4, 8, 16.
    plan = list_scan([det], motor, (2**i for i in range(4)))

Next, instead of giving a specific number of readings, let's run ``count``
indefinitely --- until interrupted by the user pressing Ctrl^C. Instead of
``range``, which counts integers up to a given upper limit, we'll use another
built in function, ``itertools.count``, which counts integers without bound.


.. code-block:: python

    import itertools

    # This would run forever until interrupted (for example, with Ctrl^C).
    plan = count([det], delay=(2**i for i in itertools.count(0)))


.. ipython:: python

.. note::

    Python provides many convenient tools for working with series
    ("iterators").  Many are available in the built-in module
    `itertools <https://docs.python.org/3/library/itertools.html>`_, which is
    worth getting to know.

