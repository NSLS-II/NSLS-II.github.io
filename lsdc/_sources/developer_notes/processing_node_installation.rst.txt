============================
Processing Node Installation
============================

Processing nodes need access to the data, as well as being able to run a processing script via ssh given LSDC collection ID and additional parameters, retrieve relevant experimental metadata, then run processing using standard data reduction programs.

--------------
Pre-requisites
--------------

1. The most recent RHEL should be installed
2. The following directories should be visible:

   - /nsls2/software/mx/daq
   - /nsls2/data/<tla> where <tla> = three-letter acronym for beamline (amx/fmx/nyx)

---------
Procedure
---------

Use the "Schedule Remote Job" item in Explorer for the selected node(s) to run the following roles:

 - Conda/"Conda - Install custom conda env (lsdc-processing)"
 - Miscellaneous/"mx_software"

If this computer has not been set up before, firewall configuration may be necessary for communication to happen to the amostra, analysisstore, and conftrak services on xf17id2-srv2.

 - Test this by doing the following while on the NSLS-II network - if a connection is made, then port is already available:

   telnet xf17id2-srv2 7770

 - Ask your AST lead to update firewall settings to allow communication from your new node to ports 7770, 7771, 7773 on xf17id2-srv2
