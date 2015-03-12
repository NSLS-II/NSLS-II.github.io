.. NSLS-II arch documentation master file, created by
   sphinx-quickstart on Sun Jan 18 10:00:09 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NSLS-II Beamline Controls Documentation
=======================================

.. raw:: html

   <div class="container-fluid">
   <div class="row">
   <div class="col-md-6">
   <h2>For Users</h2>
   <h3>Colllecting Data</h3>

The user interface to beamline controls and data collection is *ophyd*, a
Python package with a syntax that will be familiar to users of SPEC.

.. toctree::
   :maxdepth: 2

   quick-start
   ophyd/cli_api
   ophyd/scan_api
   pyolog/pyolog

.. raw:: html

   <h3>Viewing, Reducing, and Exporting Data</h3>

.. toctree::
   :maxdepth: 2

   broker/basics

Some of the functionality of Data Broker and Data Muxer is also available
through a simple graphical user interface dubbed *replay.*

.. raw:: html

   <h3>Scientific Data Analysis</h3>

The software tools for analysis X-ray data are collected and distributed
in a sister project, `scikit-xray <http://nikea.github.io/scikit-xray/>`_,
which has its own separate documention.
An important feature of scikit-xray is its generic design, completely
uncoupled for the particulars of data collection at NSLS-II. It can be
used just as easily on data collected at any facility.

.. raw:: html

   <h3>Additional Resources for Scientific Coding</h3>

   <h4>Documentation for the scientific Python "stack"</h4>

* `numpy tutorial <http://wiki.scipy.org/Tentative_NumPy_Tutorial>`_ -- core package for fast array computation in Python
* `pandas <http://pandas.pydata.org/pandas-docs/stable/overview.html>`_ -- pratical data analysis tools (e.g., IO in many formats, handling missing data)
* `scikit-image <http://scikit-image.org/docs/dev/auto_examples/>`_ -- image analysis tools
* `scipy <http://docs.scipy.org/doc/scipy/reference/tutorial/index.html>`_ --
  miscellaneous funcitons and algorithms (special functions,
  linear algebra, etc.)
* `matplotlib <http://matplotlib.org/>`_ -- powerful, publication-quality
  plotting
* `conda <http://conda.pydata.org/docs/>`_ -- a package manager for the
  scientific Python community

.. raw:: html

   <h4>Using Version Control</h4>

* `Noivce-level introduction from Software Carpentry <http://www.software-carpentry.org/v5/novice/git/>`_
* `Intermediate-Level explanation of the git workflow we use <http://nvie.com/posts/a-successful-git-branching-model/>`_

.. raw:: html

   </div>
   <div class="col-md-6">
   <h2>For Beamline Scientists and Python Package Maintainers</h2>
   <h3>Getting Started</h3>

This covers every component of the software that scientists need to use
during setup, configuration, and normal operation of the controls.

.. toctree::
   :maxdepth: 2

   install

.. raw:: html

   <h3>A Technical Grand Tour</h3>

This includes the technical design philosophy and design specifications. It
also includes documentation for the low-level components, the guts that
typical users and beamline scientists will not inteact with during normal
configuration or use of the controls.

.. toctree::
   :maxdepth: 2

   ddinstall
   filestore/index
   arch/arch

.. raw:: html

   </div>
   </div>
   </div>


