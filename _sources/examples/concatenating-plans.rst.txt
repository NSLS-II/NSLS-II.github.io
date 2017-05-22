Concatenating plans
*******************

Problem
=======

Write a custom plan to run a multi-step procedure and/or collect data for
more than one run.

Approach
========

Bluesky provides several ways to combine plans. The choice depends on your
use case and, to some extent, your personal taste.

Example Solutions
=================

We will use some standard plans (scan, count), some stub plans (abs_set,
sleep), and some plan utilities (pchain, and more later). See the
`plans documentation in bluesky <https://nsls-ii.github.io/plans.html>`_ for
more.

.. code-block:: python

    from bluesky.plans import pchain, scan, count, abs_set, sleep
    from bluesky.examples import det, motor

Simple chaining
---------------

The simplest approach is ``pchain`` (for "plan chain"). Examples:

.. code-block:: python

    # scan; sleep for 5 seconds; scan again with denser steps
    pchain(scan([det], motor, 1, 5, 5),
           sleep(5),
           scan([det], motor, 1, 5, 10))

    # scan; pause and wait for the user to resume; scan again
    pchain(scan([det], motor, 1, 5, 5),
           pause(),
           scan([det], motor, 1, 5, 5))

    # scan a motor; then move a different motor; then count
    pchain(scan([det], motor, 1, 5, 5),
           abs_set(motor2, 5),
           count([det]))

Controlling plans with arbitrary logic
--------------------------------------

Alternatively, plans can be combined by yielding from each plan in turn:

.. code-block:: python

    def scan_sleep_scan():
        yield from scan([det], motor, 1, 5, 5)
        yield from sleep(5)
        yield from scan([det], motor, 1, 5, 10)

This is (approximately) what ``pchain`` does. But this longer form gives us the
opportunity to intercept the results from intermediate steps and use them
to make plans responsive or adaptive. For example, we can query the user for
input:

.. code-block:: python

    from plans import input  # note: this shadows the built-in function of the same name

    def interactive_plan():
        "Ask the user for a position. Move the motor there and count a detector."
        pos = yield from input('where to?')
        pos = float(pos)   # convert string input to number, e.g., '5' -> 5
        yield from abs_set(motor, pos)
        yield from count([det])

We can also print to report progress, and we can include loops:

.. code-block:: python

    def loopy_plan():
        for i in range(5):
            print('iteration number', i)
            yield from count([det])

    # Note this is an illustrative example. In practice, for this specific
    # case just use: count([det], num=5)

Avoiding 'yield from' with a decorator
--------------------------------------

If the ``yield from`` seems forbidding, write a simple function that returns
a list of plans, and top it with a decorator that takes care of the rest.

This:

.. code-block:: python

    from bluesky.plans import planify

    @planify
    def scan_sleep_scan():
        return [scan([det], motor, 1, 5, 5),
                sleep(5),
                scan([det], motor, 1, 5, 10)]

is precisely equivalent to:

.. code-block:: python

    def scan_sleep_scan():
        yield from scan([det], motor, 1, 5, 5)
        yield from sleep(5)
        yield from scan([det], motor, 1, 5, 10)

You may use whichever pattern you find more readable.
