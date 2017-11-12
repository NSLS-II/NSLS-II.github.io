************
Installation
************

.. warning

   This page is out of date, see :ref:`bl_installation` instead.

.. highlight:: bash

We distribute binary packages from an internal server using the *conda*
package manager, developed for and by the scientific Python community. The
internal server can be accessed via a web browser at
https://conda.nsls2.bnl.gov from the wired campus network or controls network.

For users outside Brookhaven National Lab, the packages can be built from
source.

Installation Procedure
----------------------

#. The following configuration files in the home directory are touched
   by this procedure ::

     .pyOlog.conf
     .condarc
     .config/
       binstar/
     ipython_ophyd/
       profile_ophyd/
       profile_beamline/
     .bashrc

   If the beamline does not have NFS home directories, then these
   files should be stored on the NFS share (:file:`/nfs/beamlineid/`)
   and sym-linked into the home directory (possibly not for
   :file:`.bashrc`).

#. If needed, fix proxy settings so you can see the Internet ::

    echo 'export https_proxy=https://proxy:8888' >> ~/.bashrc
    echo 'export http_proxy=http://proxy:8888' >> ~/.bashrc
    source ~/.bashrc

#. Set up a configuration file for pyOlog, :file:`pyOlog.conf` in
   the home directory.

#. Install miniconda ::


    wget http://repo.continuum.io/miniconda/Miniconda-3.8.3-Linux-x86_64.sh -O miniconda.sh
    chmod +x miniconda.sh
    ./miniconda.sh -b -p ./mc
    echo "export PATH=`pwd`/mc/bin:\$PATH" >> ~/.bashrc
    source ~/.bashrc

   If the beam line does not have NFS home directories then this
   should be done in the :file:`/nfs/beamline` directory.  This does
   not need to be sym-linked as the path logic in :file:`.bashrc`
   will take care of finding the correct version of conda which will
   take care of finding the correct environments.

#. Configure channels ::

    conda install binstar
    binstar config --set url https://conda.nsls2.bnl.gov/api
    conda config --add channels Nikea
    conda config --add channels BEAMLINE
    conda config --add create_default_packages pip
    conda update --all

   Where ``BEAMLINE`` is the name of the beamline organization you want to
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

=========== ======= ==================================  ==================== ==================
Beamline    Channel List of Packages                    Collection Package   Analysis Package
----------- ------- ----------------------------------  -------------------- ------------------
SRX (05id)  SRX     https://conda.nsls2.bnl.gov/SRX     srx_collection       srx_analysis
CSX (23id1) CSX     https://conda.nsls2.bnl.gov/CSX     csx_collection       csx_analysis
CSX (23id2) CSX2    https://conda.nsls2.bnl.gov/CSX2    csx2_collection      csx2_analysis
XPD (28id)  XPD     https://conda.nsls2.bnl.gov/XPD     xpd_collection       xpd_analysis
HXN (03id)  HXN     https://conda.nsls2.bnl.gov/HXN     hxn_collection       hxn_analysis
CHX (11id)  CHX     https://conda.nsls2.bnl.gov/CHX     chx_collection       chx_analysis
IXS (10id)  IXS     https://conda.nsls2.bnl.gov/IXS     ixs_collection       ixs_analysis
=========== ======= ==================================  ==================== ==================

Upgrade
-------

#. Arrange with beamline scientist to schedule upgrade.
#. Copy the conda packages to the organization.::

    binstar copy --to-owner BEAMLINE latest/PACKAGE_NAME/VERSION_STRING

#. Activate and update the :file:`ophyd` environment::

     source activate ophyd
     conda update --all

#. Make an archival copy of the new environment, named :file:`ophyd-{TODAY'S DATE}` ::

     conda create -n ophyd-`date +"%Y-%m-%d"` --clone ophyd

#. To capture a snap shot of the current code state ::

     conda list --export > installed_packages.txt

#. Create entry in OLog to record the upgrade.

IPython profile
---------------
This section covers the setup of the ipython profile for ophyd.  Realistically
there are three important considerations.

#. Where are you going to put the ipython profile?

   - There is an environmental variable ``IPYTHONDIR`` that changes where the
     `ipython --profile=some_profile` command line argument points.
   - There is a command line argument ``ipython --ipythondir=some_directory``
     that can change

#. Run this command: ``ipython profile create ipython_ophyd``

#. These lines must be added to the ``ipython_config.py`` file which is located
   at ``$IPYTHONDIR/profile_ophyd/ipython_config.py`` ::

      c.StoreMagics.autorestore = True
      c.InteractiveShellApp.extensions = ['ophyd.session',
                                          'pyOlog.cli.ipy']
      c.TerminalIPythonApp.pylab = 'auto'

#. Copy over the README.md file from `here <https://raw.githubusercontent.com/NSLS-II-CSX/ipython_ophyd/master/profile_xf23id1/startup/README>`_
   to ``$IPYTHONDIR/profile_ophyd/startup/README.md``

#. Running ``ipython --profile=ophyd`` should now successfully start up ophyd.
   To check that it is working, run `wh_pos` at the ipython prompt and make
   sure that an error is not thrown.

#. To start adding positioners and detectors, see the currently active
   profiles for `CSX1 <https://github.com/NSLS-II-CSX/ipython_ophyd/tree/master/profile_xf23id1/startup>`_,
   `CSX2 <https://github.com/NSLS-II-CSX/ipython_ophyd/tree/master/profile_xf23id2/startup>`_,
   `SRX <https://github.com/NSLS-II-SRX/ipython_ophyd/tree/master/profile_xf05id1/startup>`_,
   `XPD <https://github.com/NSLS-II-XPD/ipython_ophyd/tree/master/profile_xf28id1/startup>`_,
   `CHX <https://github.com/NSLS-II-CHX/ipython_ophyd/tree/master/profile_xf11id/startup>`_,
   `HXN <https://github.com/NSLS-II-HXN/ipython_ophyd/tree/master/profile_xf03id/startup>`_,
   and `IXS <https://github.com/NSLS-II-IXS/ipython_ophyd/tree/master/profile_xf10id/startup>`_

Potential Pitfalls
------------------

OLog issues
~~~~~~~~~~~
#. The owner of the logbooks in olog should be `ologs-log`.

XServer Issues with ssh
~~~~~~~~~~~~~~~~~~~~~~~
`xhost +`
