.. currentmodule:: bluesky

Re-scan until fit achieves desired confidence
*********************************************

Problem
=======

Scan a peak and, in real time, fit Gaussian model to the data. Repeatedly
re-scan the same region until the uncertainty in the Gaussian width parameter,
sigma, is below some threshold.

Approach
========

Use :func:`callbacks.LiveFit` and :func:`callbacks.LiveFitPlot` to perform and
visualize a non-linear least-squared fit.

Normally we would use :func:`plans.scan` to perform the 1D scan. In this case,
we need something more sophisticated to incorporate adaptive logic that
continues the scan until the fit attains sufficient confidence in sigma. We
write our scan logic using the lower-level plans :func:`plans.abs_set` and
:func:`plans.trigger_and_read`.

Example Solution
================

.. literalinclude:: scan_gaussian.py

.. plot:: examples/scan_gaussian.py
