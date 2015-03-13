************
Installation
************

.. highlight:: bash

We distribute binary packages from an internal server using the *conda*
package manager, developed for and by the scientific Python community. The
internal server can be accessed via a web browser at
https://conda.nsls2.bnl.gov from the wired campus network or controls network.

For users outside Brookhaven National Lab, the packages can be built from
source.

Installation Procedure
----------------------

#. If needed, fix proxy settings so you can see the internet ::

    echo 'export https_proxy=https://proxy:8888' >> ~/.bashrc
    echo 'export http_proxy=http://proxy:8888' >> ~/.bashrc
    source ~/.bashrc

#. Set up all of the configuration files.  In the home directory the
   following files are used ::

     pyOlog.conf
     .condarc
     .config/
       filestore/
         connection.yml
       metadatastore/
         connection.yml
       binstar/
     ipython-ophyd/
       profile-ophyd/
       profile-beamline/
     .bashrc

   If the beamline does not have nfs home directories, then these
   files should be stored on the nfs share (:file:`/nfs/bealmineid/`)
   and sym-linked into the home directory (possibly not for
   :file:`.bashrc`).

#. install miniconda ::


    wget http://repo.continuum.io/miniconda/Miniconda-3.8.3-Linux-x86_64.sh -O miniconda.sh
    chmod +x miniconda.sh
    ./miniconda.sh -b -p ./mc
    echo "export PATH=`pwd`/mc/bin:\$PATH" >> ~/.bashrc
    source ~/.bashrc

   If the beam line does not have nfs home directories then this
   should be done in the :file:`/nfs/beamline` directory.  This does
   not need to be sym-linked as the path logic ind :file:`.bashrc`
   will take care of finding the correct version of conda which will
   take care of finding the correct environments.

#. Configure channels ::

    conda install binstar
    binstar config --set url https://conda.nsls2.bnl.gov/api
    conda config --add channels Nikea
    conda config --add channels BEAMLINE
    conda config --add create_default_packages pip
    conda update --all

   Where ``BEAMLINE`` is the name of the beam-line organization you want to
   install source for (in uppercase -- see the table at bottom)

#. Install the collection or analysis stacks create a new environment ::

     conda create -n env_name package_name

   For example, to install the data-collection stack for SRX (assuming that
   you have SRX in your channels) into an environment named ``ophyd``::

     conda create -n ophyd srx_collection

   See table at bottom for list of available packages

#. Enable env ::

     source activate env_name

#. Disable env ::

     source deactivate env_name

Package sources
---------------

========== ======= ==================================  ==================== ==================
Beamline   Channel List of Packages                    Collection Package   Analysis Package
---------- ------- ----------------------------------  -------------------- ------------------
SRX (05id) SRX     https://conda.nsls2.bnl.gov/SRX     srx_collection
CSX (23id) CSX     https://conda.nsls2.bnl.gov/CSX
XPD (28id) XPD     https://conda.nsls2.bnl.gov/XPD     xpd_collection
HXN (03id) HXN     https://conda.nsls2.bnl.gov/HXN     hxn_collection
CHX (11id) CHX     https://conda.nsls2.bnl.gov/CHX     chx_collection
IXS (10id) IXS     https://conda.nsls2.bnl.gov/IXS     ixs_collection
========== ======= ==================================  ==================== ==================

Upgrade
-------

#. Arrange with beamline scientist to schedule upgrade
#. Copy the conda packages to the organization
#. Remove the :file:`ophyd-backup` environment
#. Copy the current :file:`ophyd`  environment to :file:`ophyd-backup` ::

     conda create -n ophyd-backup --clone ophyd

#. Activate and update the :file:`ophyd` environment::

     source activate ophyd
     conda update --all

#. To capture a snap shot of the current code state ::

     conda list --export > installed_packages.txt

   This can (should?) be logged to OLog

#. Create entry in OLog to record the upgrade
