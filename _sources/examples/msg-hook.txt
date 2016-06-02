Troubleshoot a slow or stalling plan
************************************

Problem
=======

A plan gets stuck or takes an unexpectedly long time to complete. We want to
discover where the problem is.

Approach
========

Print to the screen each time a new messsage from the plan in processed by the
RunEngine. Then we will see the last message received before the plan freezes
and/or slows.

Example Solution
================

The RunEngine provides a special hook, a function that is calls every time it
is about to process the next message in the plan.

.. code-block:: python

    RE.msg_hook = print

Now the RunEngine will call ``print(msg)`` before processing each ``msg`` in
the plan. Execute the plan that is causing the issue and watch the output.
Suppose we are running a ``count`` that freezes up while triggering a detector.
That would look like this:

.. code-block:: python

   In [7]: RE(count([det]))
   stage: (<bluesky.examples.SynGauss object at 0x10f1bfb38>), (), {}
   open_run: (None), (), {'plan_args': {'num': 1, 'detectors': ['<bluesky.examples.SynGauss object at 0x10f1bfb38>']}, 'detectors': ['det'], 'plan_name': 'count'}
   checkpoint: (None), (), {}
   trigger: (<bluesky.examples.SynGauss object at 0x10f1bfb38>), (), {'group': 'trigger-ff93f4'}
   wait: (None), (), {'group': 'trigger-ff93f4'}

The last message is is a 'wait' message, and it waiting for the 'trigger' just
above it to complete. If the plan freezes at this point, a likely culprit is
the triggering mechanism of the detector. In this example, we can see the
detector in question is a simulated detector, ``bluesky.examples.SynGauss``.
From here we would investigate whether the hardware was behaving properly and
whether its triggering behavior was programmed properly on the Python side.

When finished troubleshooting, set ``RE.msg_hook = None``.

We used ``print`` for simple debugging. Any user-defined function that accepts
a ``bluesky.Msg`` namedtuple as its argument could also be used.
