"""
Simply 'count' a detector
*************************

Problem
-------

Take five sequential readings of a detector.

Approach
--------

Execute :func:`bluesky.plans.count` with a simulated detector (which could be
substituted by a real detector from ophyd) and display the reading using
:func:`bluesky.callbacks.LiveTable`.

Example Solution
----------------
"""
import bluesky.plans as bp
import bluesky.callbacks as bc
from bluesky import RunEngine
from ophyd.sim import det  # a simulated detector

RE = RunEngine({})

RE(bp.count([det], num=5), bc.LiveTable([det]))
