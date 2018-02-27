Examples
********

These examples assume:

1. The user is working at the command line with IPython and the full data
   collection software stack installed. (See :doc:`/collection-quick-start`.)
2. The user has an IPython profile with scripts that perform essential
   configuration when IPython starts up. (See :doc:`/beamline-configuration`.)
   Typically, this includes defining an instance of the RunEngine and
   configuring it to save data. To experiment *without* saving data, define
   a new instance of the RunEngine like so.

   .. ipython:: python

       from bluesky import RunEngine
       RE = RunEngine({})

.. toctree::
    :maxdepth: 1

    simple-scan
    retrieving-data
    replot
    pausing
    concatenating-plans
    fit-peaks
    header-contents
    exporting-csv
    exporting-images
    simulation-mode
    baseline-readings
    adaptive-steps
    count-with-exp-decay-delay
    flyer-progress-bar
    archiver-appliance-integration
    msg-hook
