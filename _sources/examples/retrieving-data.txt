Retrieve metadata, tabular data, and image data
***********************************************

Problem
=======

Retrieve metadata, tabular data, or image data for analysis, processing, or
export.

Approach
========

Use the databroker, the all-in-one interface to saved data.

Retrieve the metadata for the run(s) of interest. Retrieve the data itself
in three different modes:

* a general-purpose method, which provides maximum flexiblity and performance
* a convenient method for retrieving tabular data
* a convenient method for retrieving image data

Example Solution
================

.. ipython:: python
    :suppress:

    from bluesky import RunEngine
    from bluesky.plans import scan
    from bluesky.examples import motor, det
    from metadatastore.mds import MDS
    from metadatastore.utils import create_test_database as mds_ctd
    from filestore.fs import FileStore
    from filestore.utils import create_test_database as fs_ctd
    from databroker import Broker
    mds = MDS(mds_ctd('localhost'))
    fs = FileStore(fs_ctd('localhost'))
    db = Broker(mds, fs)
    RE = RunEngine({})
    RE.subscribe_lossless('all', mds.insert)

The first step is always retrieving the metadata; from there, we can retrieve
the data itself.

We'll preface this example by running a scan to generate some example data.

.. ipython:: python

    uid, = RE(scan([det], motor, -10, 10, 15))

The unique id of the data set has been stashed in the variable ``uid``. We can
use that to retrieve the data from the databroker.

.. ipython:: python

    h = db[uid]

What we get back is a *header*, which contains all of the metadata from the
run.  For example, we can review the names of the detector(s) involved:

.. ipython:: python

    h['start']['detectors']

There is a lot of information in ``h``. See :doc:`/examples/header-contents`.

If we don't know the uid, we can search for the metadata in other ways. One
of the most common is recency: ``db[-1]`` retrieves the header of the most
recent scan; ``db[-5]`` means "five scans ago"; ``db[-5:]`` retrieve *all*
of the last five scans together. See
`this section of the databroker documentation <http://nsls-ii.github.io/databroker/searching.html>`_ 
for more.

Now, what about the data itself?

General-Purpose Method
----------------------

.. ipython:: python

    events = db.get_events(h)

In the variable ``events``, we now have a collection of documents
(dictionary-like mappings of names to values). Each event corresponds to 
a single data point, a row in table.

For performance reasons, the data has not actually been loaded yet. The data
is loaded one point at a time if we loop through ``events``. (This is very
useful for applications where we don't need to load the entire data set.)

To load the entire data set once, convert ``events`` to a list.

.. ipython:: python

    events = list(events)  # for large data sets, this takes awhile

Let's look at all the data in the events.

.. ipython:: python

    [event['data'] for event in events]

You might be thinking, "Just give me data!" As promised, the general-purpose
method is flexible, but it lacks terseness. For more direct methods, read on!

To learn more about the structure of an ``event``, refer to the
`overview of the document model <https://nsls-ii.github.io/architecture-overview.html>`_.

Retrieving a Table
------------------

.. ipython:: python

    db.get_table(h)

The result is a DataFrame. One can access individual columns like so:

.. ipython:: python

    table = db.get_table(h)
    table['det']

perform fast array computations using numpy

.. ipython:: python

    import numpy as np

    np.mean(table)

and much, much more.

.. note::

    The variable ``table`` here is a pandas DataFrame, scientific Python's
    answer to the spreadsheet. Read the
    `pandas documentation <http://pandas.pydata.org/pandas-docs/stable/>`_
    for more. It's an extremely powerful package for analyzing tabular
    data.

Narrowing the Results
+++++++++++++++++++++

The ``get_table`` method accepts several optional arguments which can be used
to filter the results (and corespondingly speed up the retrieval). Examples:

.. ipython:: python

    db.get_table(h, ['det'])  # just include the 'det' column

Retrieving Images
-----------------

Our example data above did not include images, so ``get_table`` served our
purposes. It is not as suitable for image data, so a separate method is
available.

If the scan includes image data, use the ``get_images`` method. You will need
to specify field name with which the image data was labeled. If you aren't sure
what this is, you can review all the field names using ``get_fields``.

.. code-block:: python

    from databroker import get_fields
    get_fields(h)  # returns list of fields names

Common choices are just ``'image'`` or ``'detector_name_image'``.

.. code-block:: python

    images = db.get_images(h, 'image_field_name')

Plot individual images using matplotlib.

.. code-block:: python

    # These imports may be not be necessary; they already be in your config.
    %matplotlib
    import matplotlib.pyplot as plt

    first_img = images[0]

    # First, print the image dimensions and check that they make sense.
    print(first_img.shape)

    # Plot.
    plt.imshow(first_img)

The ``imshow`` (i.e., "image show") function has many useful optional
parameters. Refer to
`this section of the matplotlib documentation <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.imshow>`_
for more.
