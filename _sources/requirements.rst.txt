Design Requirements
*******************

The design requirements have been developed iteratively through testing with
beamline scientists and users at NSLS-II. They will continue to change as we
learn.

Data Model
==========

* The event-based document model is the core of the project. It is not tied to
  any specific language or storage technology.
* Nothing in the schema will be specific to NSLS-II or synchrotron science. It
  will be kept general to experimental science.
* A facility or a beamline can impose extra required fields in the schema at
  configuration time (e.g. requiring username, SAF number, proposal ID, or some
  beamline-specific metadata).
* At NSLS-II, there is yet no facility-wide standard for collecting information
  identifying the owner of a data set. We await guidance from the user task
  force on this issue. Ultimately, we expect that a set of required fields will
  likely be imposed at the facility level, once the tooling is in place to
  authenticate the user and validate their inputs.
* At NSLS-II, there is no facility-wide standard for collecting sample
  information. We expect that sample metadata fields will *never* be required at the
  facility level (beyond the general SAF number) because some beamlines would
  find such a requirement onerous and unhelpful. But a suggested set of prompts
  and names should be made available for user groups or beamlines that wish to
  opt in to imposing requirements.
* The dynamic documents ('start', 'stop', 'descriptor') should support rich
  search, akin to mongo queries. The 'event' documents may not support fast
  rich queries.

Data Storage and Access
=======================

* Each beamline will run separate instances of the document databases and
  maintain separate large file storage capability.
* All data should be accessed through the databroker, not by directly using the
  files indexed by filestore.
* For the present, all of the document databases in production run an
  implementation backed by MongoDB. Other implementations will be explored
  with performance and portability in mind. In the future, different beamlines
  may run different database implementations to meet their particular
  requirements. All will satisfy the same schema and present the
  metadatastore/filestore object API.
* In the future, we hope a tiered storage system will be proided, whereby
  older or less frequently accessed large files can be transparently migrated
  to other physical storage but still accessible using the same POSIX path.
* For the present, nothing is ever deleted. In the future, we will add the
  capability for beamline scientists to selectively delete data or for the
  facility to "garbage collect" old data that has not speicfically been marked
  for long-term archival. However, this will not be implemented until all runs
  are clearly identified with an owner, which relies on guidance from the user
  task force, as outlined previously.
* Suitcase will provide tools for exporting from the databroker to various file
  formats (SPEC files and HDF5 are currently support). We are not advocating
  these formats as standards in any way: they are merely conveniences for users
  who rely on a file-based workflow and are not prepared to write their own
  custom export code. In general they are lossy and do not capture the full
  information or structure of the original documents.

Python Software Dependencies
============================

* Data collection software will require Python 3. Presently it requires
  3.4 or greater, but may be updated to rely on later minor releases
  (e.g. Python 3.6). Minor upgrades are expected to require little or no
  change to user code.
* Data analysis software will support both Python 2.7 and Python 3.4+ for now.
  Following the lead of the
  `scientific Python community at large <http://www.python3statement.org/>`_,
  support for 2.7 will be dropped before 2020, when Python 2.7 itself will stop
  receiving security patches.
* Users often interact with the software using IPython, but no core
  functionality should rely on IPython. Though IPython integration such as
  "magics" may be created for convenience and packaged with the software, all
  important functions should be runnable from a plain Python script and should
  not assume IPython is installed.
* In general, if an acceptable implementation of some functionality exists in a
  widely-used and actively-supported library, we prefer reusing that
  implementation over rewriting. In evaluating an implementation, we look for
  separation of I/O and visualization code from the core scientific logic, good
  community practices like open development and automated unit testing,
  reasonable packaging and dependencies, and a design that makes individual
  components easy to pick apart.

Python Software APIs
====================

* Ophyd will provide a low-level API for debugging hardware and whatever
  high-level API is needed by bluesky.
* Bluesky will interact with hardware only through ophyd's high-level API. It
  will provide general-purpose "plans" and the tools to assemble more
  beamline- and experiment-specific plans.
* Databroker will provide a user-friendly programmatic interface for retrieval
  documents and deferencing data from files indexed by filestore.
* The documents emmited by bluesky and the documents returned by databroker
  should be compatible (i.e., equal).
* Amostra will provide separate document collection, outside the core document
  schema, intended to store sample information. Its main technical feature is
  that it provides a way to *deference* sample information rather than store a
  separate copy of the information in every run.
* Datamuxer will provide tooling for de-multiplexing asynchronous event
  streams. (The project has not been actively developed since early 2015 and
  will need to be revisited, maybe rewritten, in light of subsequent
  developments in the document model and bluesky.)
* Scikit-beam is the name of a github organization and a Python project
  providing "core" code for projects in that organization. Any analysis code
  written at or for the beamlines that can be of general use should be refined,
  documented, and moved into scikit-beam (or some other external scipy project,
  such as scikit-image, if it is sufficiently general).
