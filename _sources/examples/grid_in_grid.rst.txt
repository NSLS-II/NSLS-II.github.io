.. curentmodule:: bluesky.plans

Scan a grid around each sample in a grid
****************************************

Problem
=======

Examples are arranged on a substrate. There are two motors, x and y, for moving
a detector over the subtrate. Scan a grid of readings around the center
position of each sample.

Approach
========

Specify the samples and their arrangement as a mapping of sample names to
(x, y) positions, like ``{'A': (1, 1), 'B': (1, 2)}``. Write a custom plan that
loops through the samples. For each sample, move to sample's center position
and perform a :func:`relative_outer_product_scan` (i.e., grid scan) around
that position. For each sample, one run will be saved. Include the sample name
in the metadata.

Example Solution
================

.. literalinclude:: grid_in_grid.py

Demo output:

.. plot:: examples/grid_in_grid.py

.. ipython:: python
    :suppress:

    from bluesky import RunEngine
    RE = RunEngine({})
    %run -i source/cookbook/grid_in_grid.py

.. ipython:: python

    RE(grid_in_grid(samples))
