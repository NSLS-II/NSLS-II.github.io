Software Deployment with Conda
------------------------------

Intro
=====

Conda is an open source package management system and environment management
system for installing multiple versions of software packages and their
dependencies and switching easily between them. See the
`conda documentation <http://conda.pydata.org/docs/>`_ for more.

Environments
============

Activating the root environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every beamline workstation has some standard conda environments. All users can
access them, but they can only be installed or updated with root privileges.
You can list the names and locations of the available environments like so:

.. code-block:: bash

    $ conda env list
    # conda environments:
    #
    analysis-17Q2.0          /opt/conda_envs/analysis-17Q2.0
    collection-17Q2.0        /opt/conda_envs/collection-17Q2.0
    root                  *  /opt/conda

To use an environment, active it.

.. code-block:: bash

   $ source activate analysis-17Q2.0
   discarding /opt/conda/bin from PATH
   prepending /opt/conda_envs/analysis-17Q2.0/bin to PATH

You can inspect the packages installed in the current environment using the
command

.. code-block:: bash

   $ conda list
   # packages in environment at /opt/conda_envs/analysis-17Q2.0:
   #
   amostra                   0.2                      py36_0
   anaconda-client           1.6.2                    py36_0
   analysis                  17Q2.0                   py36_4
   attrs                     16.3.0                   py36_1
   bleach                    1.5.0                    py36_0
   bluesky                   0.9.0                    py36_0
   <snip>

Creating custom user environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the standard system conda environments are missing some packges that you
want to use, you can create your own. 

You can copy one of the standard system environments and add some packages.

.. code-block:: bash

    $ conda create -n myenv --clone analysis some_package another_package

Or, you can create a new environment from scratch. (If you plan to use the
environment with Jupyter, you must include the ``ipykernel`` package along with
any others you want.)

.. code-block:: bash

    $ conda create -n myenv ipykernel some_package another_package

Activate the environment.

.. code-block:: bash

    $ source activate myenv

If the package is available from pip but not conda, you can use pip. Make
sure you have activated the environment first, as we did just above. 

.. code-block:: bash

    $ pip install some_other_package

Access custom user environments in NSLS-II's JupyterHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users can connect to their own user-created conda environments through
JupyterHub.

1. Activate your custom environment.

    .. code-block:: bash

        $ source activate myenv


2. Create a new Jupyter kernel for the environment.

    .. code-block:: bash

        $ python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
        Installed kernelspec myenv in /home/dallan/.local/share/jupyter/kernels/myenv

    The ``--name`` value is used by Jupyter internally. These commands will
    overwrite any existing kernel with the same name. ``--display-name`` is
    what you see in the notebook menus. For details see
    `this section of the IPython documentation <https://ipython.readthedocs.io/en/latest/install/kernel_install.html#kernels-for-different-environments>`_

3. Specify a host in the kernel file.

    The kernel requires one simple customization to work on NSLS-II's
    JupyterHub deployment. We need to specify which host to run the kernel on.

    You can check the hostname of the current machine like so:

    .. code-block:: bash

        $ hostname
        xf23id1-srv1

    Open the kernel file that we generated above. You can get its location from
    the output displayed by our kernel creation command in the previous step.
    In our example, recall you that it showed

    .. code-block:: bash

        Installed kernelspec myenv in /home/dallan/.local/share/jupyter/kernels/myenv

    so we will open the file ``kernel.json`` in that directory.

    .. code-block:: json

        {
         "argv": [
         "/home/dallan/conda_envs/myenv/bin/python",
         "-m",
         "ipykernel_launcher",
         "-f",
         "{connection_file}"
         ],
         "display_name": "Python (myenv)",
         "language": "python"
        }

    Add a new item, ``"host"`` mapped to the hostname of the machine to run
    this kernel on.

    .. code-block:: json

        {
         "argv": [
         "/home/dallan/conda_envs/myenv/bin/python",
         "-m",
         "ipykernel_launcher",
         "-f",
         "{connection_file}"
         ],
         "display_name": "Python (myenv)",
         "language": "python",
         "host": "xf23id1-srv1"
        }

    Notice that we added a comma on the second-to-last line, after ``"python"``.
    There is no comma after the last entry. JSON files are strict about this.
    (This often trips up Python users, because Python tolerates trailing commas
    in lists.)

Now, when you create a new notebook in JupyterHub, your new kernel should
appear in the menu. (You may need to refresh the browser, but you should not
need to log out of JupyterHub or restart your server.)

Internal Anaconda Server
========================

We run an internal anaconda server at https://conda.nsls2.bnl.gov.

The ``anaconda`` channel contains the "official" packages distributed by
Continuum Analytics, including widely-used packages like numpy. When
Continuum releases new version of packages, we can vet them before we make
them available to users on this channel. The ``defaults`` channel is not
vetted by us; it should never be used internally.

The ``nsls2-tag`` channel is where we put the latest tagged stable versions of
every package not officially distributed by Continuum. This includes in-house
packages like ophyd and bluesky and other dependencies that don't happen to be
packaged by Continuum yet.  The ``nsls2-dev`` channel is where we put
bleeding-edge development versions of these packages.

