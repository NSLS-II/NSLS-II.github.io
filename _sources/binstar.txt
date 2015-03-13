.. highlight:: bash

.. _binstar_build:

Setting up a machine to be a binstar builder
============================================

#. Install ``binstar-build`` ::

     conda install -c https://conda.binstar.org/binstar binstar-build

#. Create an authentication token to binstar ::

     binstar auth --create --name build-workers --scopes api:build-worker > ~/binstar.token

#. Run the worker::

     binstar-build -t $(<~/binstar.token) worker builder -u Nikea


Configuring a conda package for binstar job submission
======================================================

#. Clone the ``conda-prescriptions`` repo from
   https://github.com/NSLS-II/conda-prescriptions

#. init a binstar build if one doesn't exist already ::

    binstar-build init

.. highlight:: yaml

#. Edit the binstar-build file :file:`.binstar.yml` so that it
   basically looks like this ::

     package: package_name
     user: binstar_user_name # place to upload the file to
     platform:
       - linux-64
       - osx-64
     engine:
       - python=2.7
       - python=3.4
     install:
       - conda config --add channels Nikea
     script:
       - conda build .
     build_targets: conda
     iotimeout: 600

.. highlight:: bash

#. Submit the binstar build with ::

     binstar-build submit


Submitting builds to binstar
============================

#. Login to your binstar ::

     binstar config --set url https://conda.nsls2.bnl.gov/api
     binstar login

#. Configure your binstar account to use Nikea/builders to be the default queue

   #. go to https://conda.nsls2.bnl.gov
   #. go to User Settings (top left)
   #. go to Build Queues
   #. Set the default queue to be ``build/Nikea/builders``

#. Submit the build ::

     binstar-build submit


Current build servers
=====================

+----------+-----------------+-------------------------+
| os       | hostname/ip     | screen                  |
+----------+-----------------+-------------------------+
| osx-64   | 130.199.219.101 |                         |
+----------+-----------------+-------------------------+
| linux-64 | xf23id1-srv1    | screen -x binstar-build |
+----------+-----------------+-------------------------+
