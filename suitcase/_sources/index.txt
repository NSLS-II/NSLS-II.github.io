.. NSLS-II arch documentation master file, created by
   sphinx-quickstart on Sun Jan 18 10:00:09 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Suitcase
********

Suitcase is a simple utility for exporting data from the
`databroker <https://nsls-ii.github.io/databroker>`_
into a stand-alone, portable file.

Currently, it has just one function, ``export``, which writes the data from
one or more runs into HDF5 file.

Usage Example
-------------

.. code-block:: python

    from databroker import DataBroker as db
    import suitcase
    last_run = db[-1]
    suitcase.export(last_run, 'myfile.h5')

The first argument may be a single Header or a list of Headers. This is the
API documentation for the only function in suitcase:

.. currentmodule:: suitcase

.. autofunction:: export

File Format and Project Roadmap
-------------------------------

The output file in the `HDF5 format <https://www.hdfgroup.org/HDF5/>`_, used by
many large scientific organizations where long-term archival is critical. It
can be read using a GUI interface such as `HDF Compass
<https://www.hdfgroup.org/projects/compass/>`_ or programmatically in many
languages, `including Python <http://www.h5py.org/>`_.

The contents are organized in a straightforward way that closely reflects the
way the data is stored internally in metadatastore (a mongoDB database). The
authors are emphatically *not* promoting this particular layout as a new file
format to be imitated elsewhere or adopted as a standard. It is merely an
expedient and simple way to export data. These files can easily be rearranged
and "translated" into other HDF5 layout or other file formats.  Direct support
for other formats in suitcase itself -- including other HDF5 layouts that are
standard in certain scientific communities -- is planned.
