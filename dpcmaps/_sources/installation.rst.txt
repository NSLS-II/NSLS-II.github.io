============
Installation
============

DPC Maps package may be installed from PyPI, conda-forge or source files located on GitHub.
It is recommended that DPC Maps is installed in a conda environment. DPC Maps is expected
to work with Python 3.7-3.9. Create a conda environment with the desired Python version
(arbitrary environment name may be selected, e.g. ``dpcmaps-env``)::

    $ conda create -n dpcmaps-env python=3.8
    $ conda activate dpcmaps-env

DPC Maps may also be installed in an existing conda environment that contains compatible
Python version and packages. Activate the environment before proceeding to the next
installation steps.

Installation from PyPI
----------------------

.. code-block::

    $ pip install --upgrade pip
    $ pip install PyQt5 dpcmaps

Do not install ``PyQt5`` package if the environment already contains ``pyqt`` package from conda-forge
or default Anaconda channel (list conda packages using ``conda list`` command).
If additional packages are needed (e.g. ``databroker`` or ``hxntools``), they need to be installed
separately from PyPI::

    $ pip install databroker hxntools

Installation from conda-forge
-----------------------------

.. code-block::

    $ conda install dpcmaps -c conda-forge

If additional packages are needed (e.g. ``databroker`` or ``hxntools``), they need to be installed
separately from conda-forge::

    $ conda install databroker hxntools -c conda-forge

Installation from source
------------------------

Clone the GitHub repository in the convenient location on the local disk::

    $ git clone https://github.com/NSLS-II/dpcmaps.git
    $ cd dpcmaps

Install from source (the cloned repository may be deleted after installation)::

    $ pip install .

or perform the develop install (code from the repository is executed)::

    $ pip install -e .
