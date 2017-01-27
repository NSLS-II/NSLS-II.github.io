Access EPICS Archiver Appliance via the data broker
***************************************************

Problem
=======

Access all readings from a given PV during the duration of a run.

Approach
========

Use the data broker's plugin mechanism.

Example Solution
================

Configuration
-------------

This setup only has to be done once, typically in an IPython profile.

Create an ``ArchiverPlugin``.

.. code-block:: python

    from datbroker import ArchiverPlugin
    ARCHIVER_URL = 'http://xf16idc-ca.cs.nsls2.local:17668/'  # for example
    ap = ArchiverPlugin(ARCHIVER_URL, 'US/Eastern')

Then map the plugin to a custom keyword argument. We'll use ``archiver_pvs``
for this example. Either customize an existing instance of ``Broker``,

.. code-block:: python

    from databroker import DataBroker as db  # singleton instance
    db.plugins = {'archiver_pvs': ap}

*or* create a new instance of ``Broker``.

.. code-block:: python

    import metadatastore.conf
    from metadatastore.mds import MDSRO
    mds = MDSRO(metadatastore.conf.connection_config)

    import filestore.conf
    from filestore.fs import FileStoreRO
    fs = FileStoreRO(filestore.conf.connection_config)

    db = Broker(mds, fs, plugins={'archiver_pvs': ap})

Usage
-----

The configuration above adds a new, optional keyword argument to the data
retrival methods, ``archiver_pvs``. They will query the Archiver Appliance for
all readings for given PVs between the ``header['start']['time']`` and
``header['stop']['time']``.

.. code-block:: python

    header = db[-1]
    db.get_events(header, archiver_pvs=['...'])
