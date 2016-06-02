.. _filestore-format:

****************************
Format of File Store Entries
****************************

Introduction
============

The fileStore is for abstracting access to the contents of
data stored in files.  It is important to make the distinction between
*files* and *datasets*, as a single *file* can contain more than one *dataset*.
There are two core collections, ``FileBase``
which stores information about the *files* (where the file physically is,
what format it is) and  ``FileEventLink`` which stores which file and how
to extract a single *dataset* from that file.   Thus, by storing a single
uuid, MetadataStore can keep track of non-scalar data in external storage.
By only linking to ``FileStore`` through a *dataset* ID the grouping of
data by file is de-coupled from any other logical grouping (by run or by
detector).

Associated with the database there needs to be a set of ``Handler`` classes
which deal with opening files and extracting the *dataset* from the file.  There
should also be a set of symmetric classes which handle file/dataset creation
and the generation/insertion of the relevant documents.

There will be one or more secondary (derived) collections which store meta-data
like file size, data shape/type ect.


Collections
===========

FileBase
--------

The ``FileBase`` collection store the bare minimum required to locate and
open a file.  The documents have the following structure ::

  FileBase : {
      spec: <string>,
      file_path: <string>,
      custom: <dict>
      }

Which mean:

 - ``spec`` : a string identifier to control the dispatch to the correct
      ``Handler`` class.  By doing dispatch this way multiple types of files (or
      even different views into the same file) can be stored in the same database.

 - ``file_path`` : path to where the file exists on the physical disk.

 - ``custom`` : dictionary of arguments which are passed to the ``Handler`` along
   with the ``file_path`` when the file is opened.


There is not intended to be any reference to ``FileBase`` documents on in the
analysis client code, but DAQ will need to both create ``FileBase`` entries and
keep track of them to create ``FileEntryLink`` documents.


FileEntryLink
-------------
The ``FileEntryLink`` collections holds the information required to extract a single
data set from a *file*.  The documents have the following structure ::

  FileEntryLink : {
      file_base : <FileBase reference>,
      event_id : <unique id>,
      link_parameters : <dict>,
  }

which mean :

   - ``file_base`` : a link back to what file the *dataset* is in.
   - ``event_id`` : a globally unique identifier for the dataset.  This string is
     exposed to ``metadataStore``
   - ``link_parameters`` : a dictionary of kwargs to pass to the ``Handler`` instance

Handlers
========

The handler classes are what hold all of the data retrieval logic together.  The API on
``Handlers`` is such that, given an ``event_id`` ::


  fel_doc = get_event_link_document(event_id)
  fb_doc = get_file_base_doc(fel_doc)
  # use the spec value to look up what handler to use
  h_class = handler_dispatch(fb_doc.spec)
  # use the file_path and custom values to create a handler
  h = h_class(fb_doc.file_path, **fb_doc.custom)
  dataset = h(**fel_doc.link_parameters)
