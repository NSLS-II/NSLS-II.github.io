Architecture Overview
=====================

.. graphviz:: ../images/graphviz/overview.dot
    :caption: Overview of the LSDC system

LSDC consists of a number of components. These include:

LSDC GUI
    The graphical user interface that allows a users or staff to interact with all the systems involved with the data acquisition systems 

LSDC Server
    The server script that runs on specific machines that co-ordinates with the GUI and other systems. 

Microservices
    A set of microservices that support LSDC with sample management (Amostra) and configuration management (Conftrak)


Microservices
-------------

Amostra
    .. graphviz:: ../images/graphviz/amostra_schemas.dot
       :caption: Amostra Schema

    Amostra is sample management web app that connects to a MongoDB instance. 
    The server is a thin tornado instance that associates requests made by LSDC to existing
    projects. For more documentation, `see amostra docs <https://nsls-ii.github.io/amostra/>`_

Conftrak
    Configuration management tool for beamlines based on Amostra. For more information, `see conftrak docs <https://github.com/NSLS-II/conftrak>`_

Analysisstore
    Used to store analysis results. For example, raster results and Chooch (energy scan) results go in here. For more information, `see analysisstore docs <https://nsls-ii.github.io/analysisstore/>`_

LSDC Server
-----------
The LSDC server is a continuously running process in a server node that reads specific EPICs command PVs and runs them.
Currently, the server script is started using `daq_main2.py`

.. graphviz:: ../images/graphviz/server_overview.dot


MX Processing
-------------
.. graphviz:: ../images/graphviz/mx-processing-software.dot

Edna
    Details of Edna here...

FastDP
    Details of Fast DP here...


mxtools
--------

mxtools
    This library contains scripts that are to be shared between AMX and FMX, but are not common with NYX, which has its own nyxtools.
    Scripts initially developed for the Jupyter notebooks can be brought into mxtools then made available in both Jupyter notebooks and LSDC.
    The other main use case is for defining Ophyd objects and Bluesky scan objects that are different between AMX/FMX and NYX due to hardware differences.
    This library is made available by adding it to the `PYTHONPATH` when starting up LSDC. By adding mxtools in front of LSDC in `PYTHONPATH`, scripts and definitions defined in mxtools have priority over the default ones in LSDC.


ISPyB
-------


