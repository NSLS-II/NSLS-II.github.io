***********************
Write Your Own Suitcase
***********************

Scope of a Suitcase
===================

Suitcases are Highly Specific
-----------------------------

Suitcase's design philosophy is to make many, tailored suitcases rather
than try to fit a large range of functionality into one suitcase.

Each file format is implemented in a separate Python package, named
``suitcase-<format>``. As support for new formats is added over time, there may
someday be hundreds of suitcase packages. This modular approach will keep the
number of dependencies manageable (no need to install heavy I/O libraries that
you don't plan to use). It will also allow each suitcase to be updated and
released on its own schedule and maintained by the specific communities,
facilities, or users who care about a particular format.

Even "one suitcase per file format" is too broad. Some formats, such as HDF5,
enable a huge variety of layouts---too many configure via a reasonable number
of parameters. Therefore, there will never be a "suitcase-hdf5" package, but
rather multiple suitcases, each tuned a specific HDF5 layout such as NeXuS or
Data Exchange.

Categories of Suitcases
-----------------------

The :doc:`list of existing and planned suitcases <formats>` groups them into
three categories.

* "One-offs" --- These are tailed to one specific application, writing files to the
  requirements of a particular software program or user.
* "Generics" --- These write commonly-requested formats such as TIFF or CSV.
  There is often room for interpretation in how exactly to lay out the data
  into a given file format. (One TIFF file per detector? Per Event? Per
  exposure?) The design process can devolve into tricky judgment calls or
  a confusing array of options for the user. When it doubt, we encourage you to
  steer toward writing one or more "one-offs".
* "Backends" --- These are less user-facing that the other two categories. They
  write into a file meant to be read back be a programmatic interface. For
  example, suitcase-mongo insert documents into MongoDB.

Creating a New Suitcase Package
===============================

Create the package with cookiecutter
------------------------------------

#. Install cookiecutter. This is a tool for generating a new Python package
   from a template.

   .. code-block:: bash

      pip install --upgrade cookiecutter

#. Use cookiecutter to create a new suitcase package. Just follow the prompts.

   .. code-block:: bash

      cookiecutter https://github.com/NSLS-II/suitcase-cookiecutter

      subproject_name [ex: tiff, spec, pizza-box]: my-special-format
      subpackage_name [my_special_format]: 

   This will have created a new directory named ``suitcase-my-special-format``
   with all the "scaffolding" of a working Python package for suitcase.

#. Initialize the directory as a git repository.

   .. code-block:: bash

      git init
      git add .
      git commit -m "Initial commit"

#. Install the package and its development requirements.

   .. code-block:: bash

      cd suitcase-my-special-format
      pip install -e .
      pip install -r requirements-dev.txt

Write the Serializer
--------------------

Before reading this section, read to the end of :doc:`usage`.

All suitcase packages must contain a :class:`Serializer` class with the
interface outlined below. It should also contain an :func:`export` function.
These should be in ``suitcase/my-special-format/__init__.py``.

Here is a :class:`Serializer` that writes the documents into a
newline-delimited JSON file with one document on each line written as
``[<name>, <doc>]``. This is lifted from suitcase-jsonl, chosen as a teachable
example because it is a very straightforward format from a developer point of
view.

TODO Walk through this code in more detail, in chunks.

.. code-block:: python

    import event_model
    from pathlib import Path
    import suitcase.utils
    import numpy
    import json

    class Serializer(event_model.DocumentRouter):
        def __init__(self, directory, file_prefix='{uid}', **kwargs):

            self._output_file = None
            self._file_prefix = file_prefix
            self._templated_file_prefix = ''
            kwargs.setdefault('cls', NumpyEncoder)
            self._kwargs = kwargs
            self._start_found = False

            if isinstance(directory, (str, Path)):
                self._manager = suitcase.utils.MultiFileManager(directory)
            else:
                self._manager = directory

        @property
        def artifacts(self):
            # The manager's artifacts attribute is itself a property, and we must
            # access it anew each time to be sure to get the latest content.
            return self._manager.artifacts

        def _check_start(self, doc):
            if self._start_found:
                raise RuntimeError(
                    "The serializer in suitcase-jsonl expects "
                    "documents from one run only. Two `start` documents where "
                    "sent to it")
            else:
                self._start_found = True
                self._templated_file_prefix = self._file_prefix.format(**doc)

        def _get_file(self):
            filename = (f'{self._templated_file_prefix}.jsonl')
            self._output_file = self._manager.open('stream_data', filename, 'xt')

        def __call__(self, name, doc):
            if name == 'start':
                self._check_start(doc)
                self._get_file()

            line = "%s\n" % json.dumps((name, doc), **self._kwargs)
            self._output_file.write(line)
            return name, doc

        def close(self):
            if self._output_file is not None:
                self._output_file.close()


    class NumpyEncoder(json.JSONEncoder):
        # Credit: https://stackoverflow.com/a/47626762/1221924
        def default(self, obj):
            if isinstance(obj, (numpy.generic, numpy.ndarray)):
                if numpy.isscalar(obj):
                    return obj.item()
                return obj.tolist()
            return json.JSONEncoder.default(self, obj)

Test the Serializer
-------------------

The suitcase-utils package provides a parametrized pytest fixture,
``example_data`` for generating test data. Tests should go in
``suitcase/my-special-format/tests/tests.py``.

.. code-block:: python

    import json
    from suitcase.jsonl import export, NumpyEncoder


    def test_export(tmp_path, example_data):
        documents = example_data()
        artifacts = export(documents, tmp_path)
        filepath, = artifacts['stream_data']
        with open(filepath) as file:
            actual = [json.loads(line) for line in file]
        expected = [json.loads(json.dumps(doc, cls=NumpyEncoder))
                    for doc in documents]
        assert actual == expected

Run the tests with pytest:

.. code-block:: bash

   pytest

API Documentation
-----------------

TODO Add abstract base class for :class:`Serializer`.

.. autoclass:: suitcase.utils.MultiFileManager
   :members:

.. autoclass:: suitcase.utils.MemoryBuffersManager
   :members:
