Overview of Components
======================

User-Facing Software
--------------------

Python
++++++

.. image:: _static/python-logo.png
   :width: 80px
   :align: right

Python is a programming language that is becoming increasingly popular for
scientific use.

`Python Homepage <https://www.python.org/>`_

For those new to Python, we recommend the book 
`Effective Computation in Physics <http://shop.oreilly.com/product/0636920033424.do>`_,
an excellent primer in scientific Python that starts from the very beginning.

IPython
+++++++

.. image:: _static/ipython-logo.jpg
   :width: 80px
   :align: right

IPython is a powerful interactive command prompt, developed by physicists
for scientific computing. At NSLS-II, we use our data collection packages
from inside an IPython session. There, we can also retrieve, export, and
analyze data.

`IPython Homepage <http://ipython.org/>`_

IPython Notebooks (a.k.a. Jupyter)
++++++++++++++++++++++++++++++++++

.. image:: _static/jupyter-logo.png
   :width: 80px
   :align: right

IPython notebooks (now called "Jupyter notebooks") allow users to interact
with IPython from a web browser. They are a useful new tool for collaboration
and reproducible science.

`Jupyter Homepage <http://jupyter.org/>`_

Conda
+++++

.. image:: _static/anaconda-logo.png
   :width: 80px
   :align: right

Conda is an package manager (i.e., installer). It support "virtual
environments," making it easy to switch between different versions and
combinations of software packages.

It is a free product from Continuum Analytics. At NSLS-II, we use it to
distribute all our collection and analysis software.

`Conda Cheat Sheet <http://conda.pydata.org/docs/_downloads/conda-cheatsheet.pdf>`_

`Full Documentation <http://conda.pydata.org/docs/>`_

Bluesky
+++++++

Bluesky is a Python package for writing and running scans. It contains a
library of built-in scans, a library of utilities for suspending and
resuming scans, a "Run Engine" that executes scans, and a library of simple
live data-viewing and -processing tools.

`Full Documentation <https://nsls-ii.github.io/bluesky>`_

Data Broker
+++++++++++

Data Broker is a Python package that provdies a simple, user-friendly interface
for retireving stored data. Emphatically, it is agnostic to data formats:
however the data is store, Data Broker provides it to the user as data in
memory (RAM).

`Full Documentation <https://nsls-ii.github.io/dataportal>`_

scikit-xray
+++++++++++

scikit-xray is a multi-facility collaboration, aiming to provide Python
software for X-ray data analysis, integrating with other, well-established
scientfiic Python projects like scipy and scikit-image.

`Full Documentation <https://scikit-xray.github.io/scikit-xray>`_

Ophyd
+++++

Ophyd is a Python package with a zoo of Python objects that represent and
communicate with hardware through EPICS. *Documentation for ophyd is
still a work in progress.*

Suitcase
++++++++

Suitcase is a very simple Python package for exporting data from DataBroker
to an HDF5 file that users can take home. *Suitcase is
still in the experimental stage and could be replaced in the future. There
is currently no documentation.*


Album
+++++

Album is a Python-based web app for quickly viewing data from the DataBroker.
It is readonly --- it is not for rich exploration or analysis. *Album is
still in the experimental stage and could be replaced in the future. There
is currently no documentation.*

Core Software
-------------

MongoDB
+++++++

.. image:: _static/mongodb-logo.jpg
   :width: 80px
   :align: right

MongoDB is an open-source document database designed for ease of
development and scaling. It support rich search capability and flexible
document specification, which is ideal for scientific workflows.
At NSLS-II, we store all experiment metadata and "small" data
(i.e., not images) in MongoDB.

`MongoDB Homepage <https://www.mongodb.org/>`_

metadatastore
++++++++++++++

metadatastore is a Python package that interface with MongoDB to store
experiment metadata and some data.

filestore
+++++++++

filestore is Python package that interfaces with MongoDB to maintain a
"directory" of all large-data files produced by experiments, along with
instructions for how to open those files and the data inside them.
