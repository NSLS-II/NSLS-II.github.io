============
Installation
============

Create and activate Conda environment::

    $ conda create -n xmidas_env python=3.9 -c conda-forge
    $ conda activate xmidas_env

Installation from *conda-forge*::

    $ conda install xmidas -c conda-forge

Installation from *PyPI* in a new environment::

    $ pip install xmidas[all]

Installation into an environment that already has ``PyQt`` and ``opencv`` installed,
for example an environment that has *XMidas* installed from *conda-forge*::

    $ pip install xmidas

Development installation from source is similar. In the new Conda environment use ::

    $ pip install -e .[all]

and if the environment has ``PyQt`` and ``opencv`` installed use ::

    $ pip install -e .

Start the program by typing ::

    $ xmidas

in the command line.
