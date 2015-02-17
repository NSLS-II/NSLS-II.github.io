Installation
------------
.. highlight:: bash

We distribute the beamline control and analysis software

The internal binstar server can be accessed via a web browser at https://conda.nsls2.bnl.gov
from the wired campus network or controls network.

#. If needed, fix proxy settings so you can see the internet ::

    echo 'export https_proxy=https://proxy:8888' >> ~/.bashrc
    echo 'export http_proxy=http://proxy:8888' >> ~/.bashrc
    source ~/.bashrc

#. install miniconda ::

    wget http://repo.continuum.io/miniconda/Miniconda-3.8.3-Linux-x86_64.sh -O miniconda.sh
    chmod +x miniconda.sh
    ./miniconda.sh -b -p ~/mc
    echo 'export PATH=~/mc/bin:$PATH' >> ~/.bashrc
    source ~/.bashrc

#. Configure channels ::

    conda install binstar
    binstar config --set url https://conda.nsls2.bnl.gov/api
    conda config --add channels Nikea beamline
    conda update --all

   Where ``beamline`` is the name of the beam-line organization you want to install source
   for (see table at bottom)

#. Install the collection or analysis stacks create a new environment ::

     conda create -n env_name package_name

   For example, to install the data-collection stack for SRX (assuming that you have
   SRX in your channels) ::

     conda create -n SRX srx_collection

   See table at bottom for list of available packages


#. Enable env ::

     source activate env_name

#. Disable env ::

     source deactivate env_name

========== ======= ==================================  ==================== ==================
Beamline   Channel List of Packages                    Collection Package   Analysis Package
---------- ------- ----------------------------------  -------------------- ------------------
SRX (05id) SRX     https://conda.nsls2.bnl.gov/SRX     srx_collection
CSX (23id) CSX     https://conda.nsls2.bnl.gov/CSX
XPD (28id) XPD     https://conda.nsls2.bnl.gov/XPD     xpd_collection
========== ======= ==================================  ==================== ==================
