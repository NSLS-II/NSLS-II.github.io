Fit and analyze peaks
*********************

Problem
=======

Scan a region where a peak is expected. Fit a nonlinear model to the
measurements and characterize the peak center, full-width half-max, etc.

Approach
========

Use the bluesky ``PeakStats`` callback. Here's how it works:

1. Like ``LiveTable`` and ``LivePlot``, it receives a live stream of data.
2. It silently accumulates this data until a run completes.
3. It performs a nonlinear best fit, and it makes the results available through
   attributes that can be used in plots, computations, or future scans.

A convenience function called ``plot_peak_stats`` takes a ``PeakStats``
instance as input and produces a nice plot.

Example Solution
================

Configuration
-------------

Create an instance of ``PeakStats`` that looks for an x field ``'motor'``
and a y field ``'det'``. (These should match the field names of your motor
and detector, whatever they are.)

.. code-block:: python

    # These may already be imported by your configuration.
    from bluesky.examples import motor, det
    from bluesky.plans import scan
    from bluesky.callbacks import LiveTable

    from bluesky.callbacks.scientific import PeakStats, plot_peak_stats

    ps = PeakStats('motor', 'det')

.. ipython:: python
    :suppress:
    
    from bluesky.callbacks.scientific import PeakStats, plot_peak_stats
    from bluesky.callbacks import LiveTable
    from bluesky.examples import motor, det
    from bluesky.plans import scan
    ps = PeakStats('motor', 'det')
    from bluesky import RunEngine
    RE = RunEngine({})

Execution
---------

Run a simple scan (as we did in :doc:`simple-scan`) but provide the output to our
PeakStats instance, ``ps``,  as well as to ``LiveTable``.

.. ipython:: python
    
    subs = [LiveTable(['motor', 'det']), ps]
    RE(scan([det], motor, -10, 10, 15), subs)
    @savefig fit-peaks-1.png
    plot_peak_stats(ps)

Cross-hairs mark the x and y position of the min and max measurements. (In
this simulated data set, 'cen' and 'com' happen to align perfectly with 'max'
and are thus eclipsed in this particular example.)
