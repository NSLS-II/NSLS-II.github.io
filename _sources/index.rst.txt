.. NSLS-II arch documentation master file, created by
   sphinx-quickstart on Sun Jan 18 10:00:09 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NSLS-II Software Documentation
******************************

The NSLS-II software toolchain is a set of cooperative software components
for scientific data acquisition, management, and analysis. It aims to address
the entire process, from experiment specification to the composition of
publication-quality plots.

Design Goals
============

* Integrated data collection and analysis.
* Rich Metadata is automatically captured and organized for rich search
  and reproducibility.
* Live, Streaming Data: Available for inline visualization and
  processing.
* Pluggable I/O: Export data (live) into any desired format or
  database; standardized in-memory format for retrieval.
* Experiment Generality: Seamlessly reuse a procedure on completely
  different hardware.
* Use same tools for prompt and offline analysis
* Capture provenance and result of intermediate computation.
* Use existing, open-source technologies and languages.

Overview of Software Components
===============================

This diagram illustrates the scope of each library in the NSLS-II software
stack and the libraries' interfaces. *Bluesky* orchestrates the execution of an
experiment, communicating with hardware only via a high-level abstraction
provided by *ophyd*. Bluesky collates measurements and metadata into documents
which are stored in a database and, concurrently, used in any live
visualization or processing. These documents can then be accessed later via the
*databroker*. Detectors with high acquisition rates may write files directly
(in any format). Records for locating and interpreting these files are also
stored in the database.

.. image:: _static/collection-overview.svg
   :width: 100%
   :align: center

Bluesky is agnostic to the underlying control system and has been co-developed
with ophyd, a hardware abstraction library. Ophyd currently interfaces with
EPICS, but is designed to be generalized to support other control systems.

The Documents organize measurements and metadata in an :ref:`event-based model
<architecture>`. The model is formally specified but minimalist. It is
flexible, able to capture the wide range of scientific domains studied at
NSLS-II. Nothing in the model is specific to NSLS-II or even to synchrotron
science.

Project Status & Roadmap
========================

The acquisition software (ophyd & bluesky) have stabilized and are used in
production at twelve NSLS-II beamlines.  We have been able to handle all of the
expected use cases and several unforeseen applications, validating the
architecture of ophyd/bluesky and the document model.  Recently, most of the
development effort has been going into documentation and community-building.
(The `bluesky documentation <https://nsls-ii.github.io/bluesky>`_ is
particularly polished and comprehensive.)  In addition, the software has been
installed at several other facilities for testing and evaluation.

Simple prompt analysis (plots, data tables, curve fitting) is widely used
at NSLS-II. Some beamlines are taking full advantage of the event-based data
model and live access to data, and there are some early examples of feeding
prompt analysis back into the experiment control logic.

Going into the Spring 2017 cycle, the focus will shift to data access and
analysis. This includes streamlining the user interface to saved data
(databroker) and optimizing the data storage backends with performance and
portability in mind. Additionally, work is ongoing to capture intermediate
analysis results with associated provenance.

Building on top of this data retrieval software, we will write cross-beamline
multimodal analysis tools.

Detailed plans for each project are managed and discussed in the open on
`GitHub <https://github.com/NSLS-II/>`_, where the user community is invited to
observe, comment, and contribute.

Software Packages
=================

Each package has its own documentation, linked below.

* Specify experiment procedures and acquire data using
  `bluesky <http://nsls-ii.github.io/bluesky>`_.
* Set up hardware to communicate with bluesky using
  `ophyd <http://nsls-ii.github.io/ophyd>`_.
* Access saved data (and metadata) using
  `databroker <http://nsls-ii.github.io/databroker>`_.

The following projects are in use but in a less mature stage of development.

* For high-throughput applications, make a database of samples using
  `amostra <https://nsls-ii.github.io/amostra>`_.
* Align ("de-multiplex") asynchronously collected data streams, based on time
  stamps, using `datamuxer <http://nsls-ii.github.io/datamuxer>`_.
* Export data from the databroker to common formats using
  `suitcase <http://nsls-ii.github.io/suitcase>`_.
* Write analysis code using `scikit-beam <scikit-beam.github.io/scikit-beam>`_,
  in conjunction with
  `widely-used scientific Python libraries <http://www.scipy.org/>`_.
* Utilize beamline-specific libraries in the Github organizations maintained
  by individual NSLS-II beamlines at ``github.com/NSLS-II-XXX`` where XXX
  is the three-letter beamline acronym (e.g., HXN, ISS, CHX, etc.).



.. toctree::
   :hidden:
   :maxdepth: 2

   architecture-overview
   cookbook/index
   tutorials
   remote-access
   sandbox
   history
   conda
   fresh-installation
   resources
   internal_index

.. toctree::
   :hidden:
   :caption: Data Collection

   bluesky <https://nsls-ii.github.io/bluesky>
   ophyd <https://nsls-ii.github.io/ophyd>

.. toctree::
   :hidden:
   :caption: Data Access and Management

   databroker <https://nsls-ii.github.io/databroker>
   amostra <https://nsls-ii.github.io/amostra>
   datamuxer <https://nsls-ii.github.io/datamuxer>
   suitcase <https://nsls-ii.github.io/suitcase>

.. toctree::
   :hidden:
   :caption: Data Analysis

   scikit-beam <http://scikit-beam.github.io/scikit-beam>

.. toctree::
   :hidden:
   :caption: GitHub Links

   NSLS-II Repositories <https://github.com/NSLS-II/>
   Wish List <https://github.com/NSLS-II/wishlist/issues>
   Bug Reports <https://github.com/NSLS-II/Bug-Reports/issues>
