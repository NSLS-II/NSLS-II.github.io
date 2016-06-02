Interruptions: interactively pause and resume
*********************************************

Problem
=======

Pause data collection interactively and then cleanly resume it.

Approach
========

Execution can be paused interactively by pressing Ctrl+C.

* Ctrl+C once: Pause at the next convenient stopping point.
* Ctrl+C twice: Pause now, and roll back to the last convenient stopping point.

To resume, call the ``resume`` method of the RunEngine instance, e.g.,

.. code-block:: python

    RE.resume()


.. note::

    The "global state RunEngine instance," ``gs.RE``, which is typically
    aliased to ``RE``, includes a top-level function for terser resuming:

    .. code-block:: python

        # This is typically imported in the IPython profile.
        from bluesky.global_state import resume

        resume()  # an alias for gs.RE.resume()

See the
`relevant section of the bluesky documentation <https://nsls-ii.github.io/bluesky/state-machine.rst>`_
for background on how pausing and resuming operates and how to customize its
action.
