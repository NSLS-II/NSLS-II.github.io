*****
Usage
*****

Simple Export
=============

#. Peruse the :doc:`list of suitcases <formats>` and install the suitcase for
   the format you want. For example, CSV.

   .. code-block:: bash

      pip install suitcase-csv

#. Access the bluesky "documents" containing the data/metadata that you want to
   export. For example, saved data can be accessed from the databroker.

   .. code-block:: python

      from databroker import Broker
      db = Broker.named('my_beamline')
      docs = db[-1].documents(fill=True)

#. Use the :func:`export` function in the suitcase.

   .. code-block:: python

      suitcase.csv.export(docs, '')

   This will generate one or more files in the current directory. You may also
   specify a different directory like so:

   .. code-block:: python

      suitcase.csv.export(docs, 'path/to/usb_stick')

   The number of files generated depends on the format and also the specifics
   of the data being exported.  For example, suitcase-csv generates one CSV
   file for each logical table ("stream") in the data, which varies. The
   filenames are returned by the :func:`export` function.

   By default the file names are derived from the run's unique ID, which is
   guaranteed to be *unique* but not very descriptive --- names like
   ``e687d1b6-af34-4f8f-9f0d-2ebe1e1edcb7-primary.csv`` and
   ``e687d1b6-af34-4f8f-9f0d-2ebe1e1edcb7-baseline.csv``. To tailor the name to
   your needs, you can specify a file prefix:

   .. code-block:: python

      suitcase.csv.export(docs, 'path/to/files', 'my-data-')

   which would lead to names like ``my-data-primary.csv`` and
   ``my-data-baseline.csv`` in this case.

   You can also *template* the file prefix with metadata (extracted from the
   RunStart document). Examples:

   .. code-block:: python

      export(docs, 'path/to/files', '{plan_name}-{motors}-')
      export(docs, 'path/to/files', '{time:%%Y-%%m-%%d_%%H:%%M}-') # timestamp
      export(docs, 'path/to/files', '{sample_name}')

   The last example assumes that ``sample_name`` was included in the metadata
   when the data was acquired.

#. Repeat if multiple formats are desired. For example, you may wish to
   export to CSV (which captures only scalar data), TIFF (which captures only
   image data), and JSON (which is well-suited for exporting metadata). It may
   be useful to wrap these up in a custom function.

   .. code-block:: python

      from itertools import tee
      import suitcase.csv
      import suitcase.tiff_series
      import suitcase.json_metadata

      def my_exporter(docs, directory, file_prefix):
          docs1, docs2, docs3 = tee(docs, 3)
          suitcase.csv.export(docs1, directory, file_prefix)
          suitcase.tiff_series.export(docs2, directory, file_prefix)
          suitcase.json_metadata.export(docs3, directory, file_prefix)

      my_exporter(docs)

   .. note::

      The first line in ``my_exporter`` above duplicates docs into 3 identical
      versions. It is required as ``docs`` may be a generator that will be
      exhausted when used and we need to use it 3 independent times.

.. warning::

    Note that :func:`export` can only be used on one "run" (one RunStart
    document) at a time. Do multiple runs like this:

    .. code-block:: python

       for header in db(since='2018-01'):
           export(header.documents(), '')

Streaming Export
================

In addition to the :func:`export` function, each suitcase package implements a
:class:`Serializer` class. It produces exactly the same files and has the same
options; :func:`export` is just a wrapper around :class:`Serializer`. But
where :func:`export` loops through a list or generator of documents,
:class:`Serializer` expect documents to be *pushed* through, thus:

.. code-block:: python

   # Export documents from *one run only* in a streaming fashion.

   from suitcase.csv import Serializer
   serializer = Serializer('path/to/files')
   for name, doc in docs:
       serializer(name, doc)

   serializer.artifacts  # Access the filenames.

The filenames may be accessed at any time via ``serializer.artifacts``. (This
is what is returned by :func:`export`.) The :class:`Serializer` should be
closed when finished. This closes all the of the resources (e.g. files) that is
has opened.

This is suitable for streaming export. Note that a given :class:`Serializer`
instance *may only be used for one run* (one RunStart document, RunStop document,
and whatever in between). A new instance must be created for each new run.
The :class:`~event_model.RunRouter` streamlines this process.

.. code-block:: python

   # Set up a RunRouter suitable for exporting from many runs.

   from event_model import RunRouter
   from suitcase.csv import Serializer

   def factory(name, start_doc):

       serializer = Serializer('path/to/files')
       serializer('start', start_doc)

       return [serializer], []

   rr = RunRouter([factory])

The :class:`~event_model.RunRouter` will call our ``factory`` at the beginning
of each run, creating a fresh ``serializer`` instance and routing
documents through it. We can push documents in directly

.. code-block:: python

   for name, doc in docs:
       rr(name, doc)

or subscribe them to the bluesky RunEngine to receive documents in a streaming
fashion during acquition.

.. code-block:: python

   RE.subscribe(rr)

For documents containing pointers to external files that need to be "filled"
(that is, employing Resource and Datum documents), a
:class:`~event_model.Filler` must be used as well. This is typically relevant
for exporting images.

.. code-block:: python

   from event_model import RunRouter, Filler
   import suitcase.tiff_series
   
   def factory(name, start_doc):
   
       filler = Filler(...)
       serializer = suitcase.tiff_series.Serializer('path/to/files')
       serializer('start', start_doc)
   
       def cb(name, doc):
           filler(name, doc)  # Fill in place any externally-stored data.
           serializer(name, doc)
   
       return [cb], []
   
   rr = RunRouter([factory])
   RE.subscribe(rr)

Serialize to Any Buffer
=======================

While most users will use suitcase to write files to disk, advanced users may
write to a memory buffer, a network socket, etc. This is useful if the data's
ultimate destination is a web client or some ready application. There is no
need to waste time writing the data to disk and then reading it right back.

To support this naturally, suitcase's architecture cleanly separates the
serialization (documents-to-bytes) from the transport (what to do with the
bytes).

This:

.. code-block:: python

   serializer = Serializer(directory)

is a shorthand for this:

.. code-block:: python

   from suitcase.utils import MultiFileManager

   manager = MultiFileManager(directory)
   serializer = Serializer(manager)

"Who asked for :class:`MultiFileManager`?" you may ask. At first one might
expect to simply hand the :class:`Serializer` a writable buffer instead of
filename, as in ``Serializer(buffer)``. In fact, a more sophisticated interface
is necessary because, for many formats, the :class:`Serializer` needs to create
*multiple* buffers, sometimes a mixture of text (string) buffers and binary
(bytes) buffers. And for some formats, the number and type of buffers may vary
from one dataset to another.

The :class:`MultiFileManager` class handles opening the file(s) with the name
requested by a :class:`Serializer` and providing it with writable buffers. The
:class:`Serializer` interacts with files only indirectly, always mediated
through the :class:`MultiFileManager`. Therefore, to write to a different sort
of buffer, you need only provide a different manager class. No changes are
necessary to the :class:`Serializer` itself.

This example will write the serialized data into memory buffers---subclasses of
``StringIO`` and/or ``BytesIO``, as requested by a given :class:`Serializer`.
The buffers can then be accessed via ``serializer.artifacts`` or, equivalently,
``manager.artifacts``.

.. code-block:: python

   from suitcase.utils import MemoryBuffersManager

   manager = MemoryBuffersManager()
   serializer = Serializer(manager)

There may be formats where it is not possible to write to anything but an
ordinary file because the underlying I/O library *requires* a filename and
cannot write to an arbitrary buffer. In that case, a clear error will be
raised. See :doc:`writing` for details.
