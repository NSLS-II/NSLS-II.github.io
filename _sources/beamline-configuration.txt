.. highlight:: bash
**********************
Beamline Configuration
**********************

IPython profiles
----------------

Configuration can be done interactively or in a Python script.
At NSLS-II, configuration is done by startup scripts that are part of an
`IPython profile <https://ipython.org/ipython-doc/dev/config/intro.html#profiles>`_
. But note that it is not essential to use IPython or IPython profile in 
general -- this is just a convenience.

Profiles are stored in (or soft-linked) from ``~/.ipython`` in the user profile
of individual users or shared beamline accounts.

The standard profile is called "collection," and the startup scripts are
located in ``~/.ipython/profile_collection/startup/``. As stated in the 
quick start page, they can be invoked by typing:

.. code-block:: bash

    ipython --profile=collection

To refresh a script that has been edited, restart IPython or re-execute the
script using ``%run -i ~/.ipython/profile_collection/startup/<FILENAME>``.
Do this for any file(s) that have been updated. (There is no way to run
all files at once.)

Example Configuration File
--------------------------

This is a example IPython profile startup file.::

    # Make ophyd listen to pyepics.
    from ophyd import setup_ophyd
    setup_ophyd()

    # Subscribe metadatastore to documents.
    # If this is removed, data is not saved to metadatastore.
    import metadatastore.commands
    from bluesky.global_state import gs
    gs.RE.subscribe_lossless('all', metadatastore.commands.insert)

    # At the end of every run, verify that files were saved and
    # print a confirmation message.
    from bluesky.callbacks.broker import verify_files_saved
    gs.RE.subscribe('stop', post_run(verify_files_saved))

    # Import matplotlib and put it in interactive mode.
    import matplotlib.pyplot as plt
    plt.ion()

    # Make plots update live while scans run.
    from bluesky.utils import install_qt_kicker
    install_qt_kicker()

    # Optional: set any metadata that rarely changes.
    # RE.md['beamline_id'] = 'YOUR_BEAMLINE_HERE'

    # convenience imports
    from ophyd.commands import *
    from bluesky.callbacks import *
    from bluesky.spec_api import *
    from bluesky.global_state import gs, abort, stop, resume
    from databroker import (DataBroker as db, get_events, get_images,
                            get_table, get_fields, restream, process)
    from time import sleep
    import numpy as np

    RE = gs.RE  # convenience alias

    # Uncomment the following lines to turn on verbose messages for debugging.
    # import logging
    # ophyd.logger.setLevel(logging.DEBUG)
    # logging.basicConfig(level=logging.DEBUG)

Configuring the Olog
--------------------

Essential Configuration
=======================

pyOlog requires a configuration file to specify the connection
settings. As root, create a file at ``/etc/pyOlog.conf`` with the following
contents.::

    [DEFAULT]
    url = https://<beamline>-log.cs.nsls2.local:8181/Olog
    logbooks = Commissioning   # use the name of an existing logbook
    username = <username>
    password = <password>

where ``<beamline>`` is the designation formatted like ``xf23id1``.

Integration with Bluesky
========================

Bluesky automatically logs basic scan information at the start of a
scan. (All of this information is strictly a subset of what is
also stored in metadatastore -- this is just a convenience.)

Back in an IPython profile startup file, add::

    from functools import partial
    from pyOlog import SimpleOlogClient
    from bluesky.callbacks.olog import logbook_cb_factory

    # Set up the logbook. This configures bluesky's summaries of 
    # data acquisition (scan type, ID, etc.).

    LOGBOOKS = ['Data Acquisition']  # list of logbook names to publish to
    simple_olog_client = SimpleOlogClient()
    generic_logbook_func = simple_olog_client.log
    configured_logbook_func = partial(generic_logbook_func, logbooks=LOGBOOKS)

    cb = logbook_cb_factory(configured_logbook_func)
    RE.subscribe('start', cb)

Integration with Ophyd
======================

Ophyd has as ``log_pos`` method that writes the current position of all
positioners into the log. To enable this, add the following to an IPython
profile startup file, add::
    
    # This is for ophyd.commands.get_logbook, which simply looks for
    # a variable called 'logbook' in the global IPython namespace.
    logbook = simple_olog_client

The log entires will be written into the logbook specified in
``.pyOlog.conf`` (in our example, "Commissioning"), not the logbook
used by bluesky (in our example, "Data Acquisition").

Olog IPython "Magics"
=====================

"Magics" are special IPython commands (not part of Python itself). They
begin with %. There are two IPython magics for conveniently writing to
the Olog.

* Type ``%logit`` to quickly type a text log entry.
* Type ``%grabit``, select an area of the screen to capture, and type in a 
  text caption.

These require their own special configuration. In the profile directory, such
as ``~/.ipython/profile_collection``, edit the file ``ipython_config.py``.

Add the line::

    c.InteractiveShellApp.extensions = ['pyOlog.cli.ipy']

The log entires will be written into the logbook specified in
``.pyOlog.conf`` (in our example, "Commissioning"), not the logbook
used by bluesky (in our example, "Data Acquisition").


Defining Hardware Objects
-------------------------

For example::

    from ophyd import EpicsMotor

    # the two-theta motor
    tth = EpicsMotor('XF:28IDC-ES:1{Dif:1-Ax:2ThI}Mtr', name='tth')

See the `ophyd documentation <http://nsls-ii.github.io/ophyd>`_ for more.

Set up Default ("Global State")
-------------------------------

Set attributes of ``gs``. This can be done interactively or in a startup file.::

    gs.DETS = [det1, det2]
    gs.TABLE_COLS = ['det1']
    gs.PLOT_Y = 'det1'


Customizing IPython
-------------------

Customizing the Prompt
^^^^^^^^^^^^^^^^^^^^^^

Running the following

.. ipython::
    :verbatim:

    In [1]: %config PromptManager.in_template = '\T In [\\#]: '
    In [2]: %config PromptManager.out_template = '\T Out[\\#]: '

will make your terminal look like this:

.. code-block:: bash

    10:01:40 In [49]: 1
    10:01:42 Out[49]: 1
    10:01:42 In [50]: 
    10:02:21 In [50]: a = 2
    10:02:28 In [51]: 

It is not much more work to customize that timestamp to be truncated, include
date / day of week etc. See `this section of the IPython documentation <https://ipython.org/ipython-doc/3/config/details.html#prompts>`_ for details.
