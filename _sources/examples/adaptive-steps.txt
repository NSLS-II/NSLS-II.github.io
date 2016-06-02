Use scans with adaptive step sizes
**********************************

Problem
=======

Concentrate measurement in regions of high variability, taking larger strides
through flat regions.

Approach
========

The *plans* in bluesky can be fully adaptive, determining one step at a time.
A couple built-in plans provide this capability out of the box.

Example Solution
================

The ``adaptive_scan`` aims to maintain a certain delta in y between successive
steps through x. After each step, it accounts for the local derivative and
adjusts it step size accordingly. If it misses by a large margin, it takes a
step backward (if allowed).

See its `documentation <http://nsls-ii.github.io/bluesky/bluesky.plans.adaptive_scan.html#bluesky.plans.adaptive_scan>`_
for a full list of paramters and their meanings. Here is working example:

We'll add a ``LiveTable`` and a ``LivePlot``.

.. ipython:: python
    :suppress:

    from bluesky import RunEngine
    from bluesky.callbacks import LiveTable, LivePlot
    from bluesky.plans import adaptive_scan
    from bluesky.examples import det, motor
    RE = RunEngine({})

.. ipython:: python

    from bluesky.plans import adaptive_scan
    ad_scan = adaptive_scan([det], 'det', motor, -15, 10, .01, 5, .05, True)
    RE(ad_scan, [LiveTable(['det', 'motor']), LivePlot('det', 'motor', markersize=10, marker='o')])

.. image:: /_static/adaptive-scan-liveplot.png

Observe how the scan lengthens its stride through the flat regions, oversteps
through the peak, moves back, samples it with smaller steps, and gradually
adopts a larger stride as the peak flattens out again.
