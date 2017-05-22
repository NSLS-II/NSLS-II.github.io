
History of Changes
==================

This document presents a summary of the release notes for NSLS-II software
(bluesky, databroker, ophyd, and friends) as a convenient reference. See the
individual projects for traditional release notes, where changes are grouped by
tagged releases and documented in greater detail. This document groups notes by
each operating cycle at NSLS-II.

Cycle Beginning 2017-05
-----------------------

New functionality
+++++++++++++++++

* The new databroker-browser provides a GUI for searching runs and viewing text
  summaries, metadata, and figures. It requires some beamline-specific
  customization which DAMA can assist with during the operating cycle. An
  example
  `configuration file <https://github.com/NSLS-II/databroker-browser/blob/master/example.py>`_
  is available. (This is experimental and likely to change in the future.)
* The databroker Headers have methods for more convenience data retrieval. You
  can still do this:

  .. code-block:: python

    header = db[-1]
    db.get_table(header)

  but you can also do this:

  .. code-block:: python

    header = db[-1]
    header.table()

  which allows for succinct one-liners like

  .. code-block:: python

    db[-1].table().plot()

  Another especially useful one:

  .. code-block:: python

    header.fields()

  See the `databroker release notes <https://nsls-ii.github.io/databroker/whats_new.html>`_
  for more new methods and attributes on Headers.

API Changes
+++++++++++

* Any databroker query that potentially returns multiple Headers used to return
  a list. Now it returns a ``Results`` object, which lazily retrieves Headers
  one at a time, like so:

  .. code-block:: python

    for header in db():
        # do something

  This makes queries fast, even when the results set is large.
* Area Detector file store plugin classes have a new required argument ``fs``
  that expects an instance of filestore. Usually ``fs=db.fs`` is correct. They
  also accept an option ``root`` argument which specifies which part of the
  ``read_file_path`` is machine-specific (as opposed to permanent semantics
  that should be maintained when the files are copied or moved).
* Stepscan plans used to provide the metadata field 'num_steps'. This was
  unintentionally ambigious. Now 'num_steps' has been renamed 'num_points'.
  Additionally 'num_intervals' (num_points - 1) has been added. The removal of
  the 'num_steps' field may break user code that expects to find that field.
* The suitcase package now expects an instance of databroker (``db``) where it
  used to expect an instance of metadatastore (``db.mds``). See the
  `suitcase documentation <https://github.com/NSLS-II/suitcase>`_ for more.
