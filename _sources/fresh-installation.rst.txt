.. _bl_installation:

Installation at a Beamline
==========================

New Beamline
------------

Install Services
++++++++++++++++

These are instructions are one-time setup for a new beamline. If you are
configuring a new machine at a beamline that already has the software installed
one at least one machine, skip to the next section.

1. On some dedicated server (the standard choice is ``*-ca1``) apply the puppet
   class that installs mongo 3.x some dedicated server and start the mongo
   daemon.

Create Conda Environments
+++++++++++++++++++++++++

A puppet class should install conda into ``/opt/conda`` on machines designated
``*-srv*`` ("server") or ``*-ws*`` ("workstation") as soon as they are on the
NSLS-II network and have a puppet client configured and running. It should also be 
noted that there are some special cases where other 'classes' of machine also receive
the installation (i.e. on some ``-ca*`` and ``-gpu*`` machines).  Puppet should also 
create an empty directory, ``/opt/conda_envs`` for root-controlled conda environments. 
The configuration in ``/opt/conda/.condarc`` designates this location as the second
place conda should look for environments, after ``~/conda_envs``.

Environments for data collection and data anlysis should be installed into
``/opt/conda_envs``. In the second operating cycle of 2018, the commands to do
this were:

.. code-block:: bash

    sudo conda create -p /opt/conda_envs/collection-2018-2.1 -c nsls2-tag -y collection
    sudo conda create -p /opt/conda_envs/analysis-2018-2.1 -c nsls2-tag -y analysis
    fix_conda_privileges.sh

where ``collection-2018-2.1`` and ``analysis-2018-2.1`` are the names of conda
metapackages and the names of the environments (under ``/opt/conda_envs``)
where these metapackages are installed.

.. note::

   The structure of the enviroment name version numbering is
   ``year-cycle.micro``. For example, in the second beam operating cycle of
   2018, version ``2018-2.0`` was released, followed by ``2018-2.1`` with some
   bug-fixes.

Install Scripts
+++++++++++++++

Two convenience scripts, ``fix_conda_privileges.sh`` and ``bsui`` should be
installed in ``/usr/local/bin``, also by puppet.

* ``fix_conda_privileges.sh`` works around a bug in conda wherein users cannot
  properly access root-installed conda packages. It should be run after
  creating or updating and conda environments in ``/opt/conda_envs``, as shown
  above.
* ``bsui`` is a shortcut script that activates a conda environment and starts
  IPython with the 'collection' profile.

Create New IPython Profile
++++++++++++++++++++++++++

At NSLS-II we use IPython profiles to run startup scripts for user convenience.

Profiles are stored in (or soft-linked) from ``~/.ipython`` in the user profile
of individual users or shared beamline accounts.

The standard profile is called "collection," and the startup scripts are
located in ``~/.ipython/profile_collection/startup/``.

If this beamline does not yet have an IPython profile for data collection
under version control, create one. Start IPython with this command, and
then exit.

    .. code-block:: bash

        ipython --profile=collection

    .. note::

        The official IPython documentation has more information on
        `IPython profiles <https://ipython.org/ipython-doc/dev/config/intro.html#profiles>`_

The above command created new directores and some files under
``~/.ipython/profile_collection``. We add startup files by writing Python
scripts in the subdirectory ``startup/`` in this profile directory.

This is a example IPython profile startup file. Replace ``YOUR_HOST`` with the
server where the mongo daemon is running.

.. code-block:: python

    # Make ophyd listen to pyepics.
    from ophyd import setup_ophyd
    setup_ophyd()

    # Connect to metadatastore and filestore.
    from metadatastore.mds import MDS, MDSRO
    from filestore.fs import FileStoreRO
    from databroker import Broker
    mds_config = {'host': <YOUR HOST>,
                  'port': 27017,
                  'database': 'metadatastore-production-v1',
                  'timezone': 'US/Eastern'}
    fs_config = {'host': <YOUR HOST>,
                 'port': 27017,
                 'database': 'filestore-production-v1',
    mds = MDS(mds_config)
    mds_readonly = MDSRO(mds_config)
    fs_readonly = FileStoreRO(fs_config)
    db = Broker(mds_readonly, fs_readonly)

    # Subscribe metadatastore to documents.
    # If this is removed, data is not saved to metadatastore.
    from bluesky.global_state import gs
    gs.RE.subscribe('all', db.insert)

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
    from time import sleep
    import numpy as np

    RE = gs.RE  # convenience alias

    # Uncomment the following lines to turn on verbose messages for debugging.
    # import logging
    # ophyd.logger.setLevel(logging.DEBUG)
    # logging.basicConfig(level=logging.DEBUG)

Create a Beamline GitHub Organization
+++++++++++++++++++++++++++++++++++++

1. Create a username on github.com if you don't have one. Create a new
   organization with the name NSLS-II-XXX where XXX is the three-letter
   beamline abbreviation (e.g., ISS). Create a new repository in this
   organization named ``profile_colletion``.

2. Make the new IPython profile a git repository.

.. code-block:: bash

    cd ~/.ipython/profile_collection
    git init
    git add startup/
    git commmit -m "initial commit"


3. Upload the ``profile_collection`` git repository to GitHub. Be sure to edit
   the command below to replace NSLS-II-XXX with the name of your organization.

.. code-block:: bash

    git remote add upstream https://github.com/NSLS-II-XXX/profile_collection.git
    git push -u upstream master


Configure the Olog
++++++++++++++++++

Essential Configuration
^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^

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

New Workstation for Data Collection or Analysis
-----------------------------------------------

1. Verify that the conda puppet class has been applied by checking that the
   ``conda`` binary is available at ``/opt/conda/bin``. This should happen
   automatically on machines designated ``*-srv*`` ("server") or ``*-ws*``
   ("workstation") as soon as they are on the NSLS-II network and working with
   puppet.

2. Create configuration files for metadatastore and filestore. As root user,
   compose two new files. The ``hostname`` should be the host where the mongo
   service running (conventionally, the ``*-ca1`` machine, as noted above).

.. code-block:: bash

    # /etc/metadatastore.yml
    host: hostname
    port: 27017
    database: metadatastore-production-v1
    timezone: US/Eastern

    # /etc/filestore.yml
    host: hostname
    port: 27017
    database: filestore-production-v1

New User
--------

One-time configuration
++++++++++++++++++++++

Add the following to the user's ``~/.bashrc`` file.

.. code-block:: bash

    export http_proxy=http://proxy:8888
    export https_proxy=http://proxy:8888
    export no_proxy=cs.nsls2.local
    export PATH=/opt/conda/bin:$PATH

The first three lines are local NSLS-II controls network configuration. They
should already be set at the system level but in practice they are often not.

Conda has already been installed on all NSLS-II workstations (ws) and servers
(srv) in a shared location. The last line adds conda to the user's PATH so that
it overrides any system-installed Python, IPython, etc.

Convenience Script ``bsui``
+++++++++++++++++++++++++++

The script ``bsui``

Custom User Environments
++++++++++++++++++++++++

Any user can create a conda environment, a set of binaries and Python packages
completely under their control. User conda environments are stored under
``~/conda_envs/<environment-name>``.

This command creates a new environment called ``my-env`` with all the versions
of the collection software used for the second operating cycle of 2017.

.. code-block:: bash

    conda create -c nsls2-tag -n my-env collection-17Q2

To test the new environment, activate it:

.. code-block:: bash

    source activate my-env

Troubleshooting: Check that ``which ipython`` points to a path with the word
``my-env`` it in (not ``/usr/bin/python``, as a counterexample). To
troubleshoot, you might need to refresh bash with the command ``hash -r``.

To get "development" versions that are maybe less stable but contain the latest
bug fixes and features, use the ``nsls2-dev`` channel in place of
``nsls2-tag``.

Creating or Updating Shared (Root) Environments
+++++++++++++++++++++++++++++++++++++++++++++++

Administrators with sudo access can create or update conda environments that
users can use ("activate") but only administrators can edit. These environments
are located in ``/opt/conda_envs``.

.. note::

    To review the detailed conda configuration, refer to
    ``/opt/conda/.condarc``, where you can see the list of default channels and
    the search path for environments.

Installing on a Personal Computer
---------------------------------

You can install these packages on your personal laptop outside the controls
network. Install miniconda or Anaconda, and create user environments as
described above. All of the packages are mirrored on anaconda.org, outside of
the NSLS-II firewall, where you will be able to access them. The channels are
called ``lightsource2-tag`` and ``lightsource2-dev`` instead of ``nsls2-tag``
and ``nsls2-dev`` respectively. The following serves as a step by step guide:

#.  Follow the instructions in the link below to install minconda or anaconda.
        https://conda.io/docs/user-guide/install/index.html

#.  Open a terminal and run the following commands to install the enviroments. 

    .. code-block:: bash

        conda create -n collection-2018-2.1 -c lightsource2-tag collection
        conda create -n analysis-2018-2.1 -c lightsource2-tag analysis

    .. note::

        If you get the error

        .. code-block:: none

           The remote server could not find the noarch directory for the requested channel with url: https://conda.anaconda.org/nsls2-tag'

        then you are not on the controls network, replace ``nsls2-tag`` with
        ``lightsource2-tag`` in the command.

       The ``collection-2018-2.1`` or ``analysis-2018-2.1`` part of these
       commands relates to the released versions from the second cycle of 2018;
       you can use any version here.

    .. warning::

       There is a conda channel named ``lightsource2`` that it no longer
       maintained. If you use it, you will find very old versions of some of
       the packages used at NSLS-II. Use ``lightsource2-tag`` instead.

#.  Check this worked by running the command below:
    .. code-block:: bash

        conda env list

    You should see collection-2018-2.1 listed (or whichever version you installed).
