=================
 Release History
=================

2.0.3 (2024-01-22, a.k.a. 2024-1)
=================================

Fixes and other changes
-----------------------

* GUI

  * For users, do not show pucks that do not belong to their proposal
  * Speed up dewar tree refresh
  * Refresh dewar tree button
  * Albula now running in a separate instance
  * No more automatic pre-fill of parameters upon request click - user option to do the pre-fill
  * Moved unmount cold to the button panel. Added "End Visit" button, only unmounts warm currently

* Server

  * Datapath fix
  * Fix ISPyB processing population and crystal snapshot creation problems
  * Remove population of ISPyB database while infrastructure to update user proposal membership for SynchWeb is being developed

* Server and GUI security improvements

  * White-listing functions that can be called on the server to prevent execution of arbitrary code

2.0.2 (2023-09-12, a.k.a. 2023-3)
=================================

Fixes and other changes
-----------------------

* GUI

  * GUI code split up into its own module
  * Fixes for lifetime calculation
  * Improve Albula handling

* Server and GUI security improvements

  * Use external file to determine visit directory
  * Use same visit directory location for server and GUI, and force all files acquired by LSDC to be written to that directory
  * Enforce GUI and server starting in the visit directory
  * Ensure server is started as one of the known LSDC service users (as opposed to a staff member in n2sn-inststaff-<tla>)


* Improved synchronization of detector and governor
* Re-enable ISPyB storage of data collections and processing results
* Standardize handling of FMX towards AMX when mounting a sample
* Move storage of raster results in ISPyB onto server, to remove ISPyB dependence in GUI
* Save FMX flux reference after energy change

* NYX-specific (2023-2-nyx) - not merged into master due to significant differences

  * GUI improvements

    * General layout
    * NYX-specific changes

2.0.1 (2023-04-20, a.k.a. 2023-2)
=================================

Fixes and other changes
-----------------------

* one-branch-to-rule-them-all and derived branches will be merged into master permanently because the Bluesky collections are all working satisfactorily

  * This is why we are reporting all changes here as for this version, not for any particular version.


* Make fastDP logging identifiable
* GUI change to level 2 upon sample mount
* Prevent gonio movements in certain circumstances, such as when another sample is loaded or an experiment is in progress
* GUI

  * Startup checks including correct beamline and directory
  * Overlay improvements
  * Validation for more input fields
  * Collect Queue button now green
  * NYX-specific disabling of some buttons
  * Validate HDF5 files #link
  * Change albula image change method that improves stability
  * Remove XRF Spectrum tab
  * Changes to queue collect behavior, requests added to mounted sample if off else add to selected sample

* FMX: start fastDP/Dimple result gathering script
* FMX: Run raddose3d based on changes to transmission set point and remove "Calc Lifetime" button
* Protocol harmonization and fixing after using LSDC2

  * Remove screen and specRaster protocols https://github.com/NSLS-II/lsdc/pull/270
  * MultiCol improvements including rastering region selector, addition of transmission and oscillation range for data collections #links SB-317
  * Get ednaCol working (requires local EDNA fixes as well) SB-319
  * Remove eScan from list of selectable protocols - only available from its tab in the GUI

* Improve sample information handling to prevent problems with collection requests with empty sample IDs
* Enable old-style detector initialization - still need while remaining data collection protocols are converted to full Bluesky
* Energy scans can only be done for elements within 20 eV of current energy
* Improve handling of sample info to prevent requests with empty sample name showing up on all beamlines
* Ensure RobotControlLib is available in LSDC server and remote
* Fixed automated collection
* Docs - collection priority notes
* setE function added for FMX #link
* Fix detector distance value set in Eiger master file with rasters SB-266


2.0.0 (2023-01-18, a.k.a. 2023-1)
=================================

Fixes and other changes
-----------------------
* AMX/FMX branch (master)

  * GUI updates - right-click options on collection and close shutter button is now the main experiment "stop" button
  * Startup check added - including not allowing startup in home directory
  * Annealer working on both beamlines
  * Vector tweak - more intuitive editing of vector start/end points 
  * Puck list in order of modification
  * Crashes in puck/dewar position dialog boxes fixed
  * c3d location fixed
  * Hutch cameras run on independent QThreads, shows message when feed is unavailable

* AMX/FMX branch (one-branch)

  * Check for detector arming (part of SB-166)
  * Fix issues with governor moves at beginning and toward end of collections SB-165
  * Always stop the detector acquisition at the end of standard, vector, and raster collections SB-166
  * Fix energy being incorrect for rasters SB-184
  * Rastering looks like it is now working - will be tested once beam is available SB-168

* NYX branch (nyx-one-branch)

  * Isara robot (in nyxtools)
  * Isara robot integration into LSDC

* Documentation

  * Architecture diagram and description added
  * Graphviz files can now be used in documentation and are compiled during the build process

1.0.3 (2022-09-06, a.k.a. 2022-3)
=================================

Fixes and other changes
-----------------------
* AMX/FMX branch (master)

  * Make a copy of the lysozyme PDB file for Raddose instead of a symlink to prevent Globus issues
  * More handling of ValueErrors from bad input on GUI fields
  * Remove extra popup dialog on startup (progress bar)
  * Add beamCheck box to GUI
  * Add DewarRefill function on the server-side
  * Refactor hutch camera code to stop GUI from crashing when cameras are broken/absent and to update quicker

* AMX/FMX branch (amx-fmx-one-branch-fixes)

  * Calculate wavelength from energy on all beamlines
  * Add Bluesky logging
  * Use new ISPyB database hostname
  * Fix detector distance in flyer
  * Vector data collection working on AMX/FMX
  * Initial code for rastering for AMX/FMX
  * Use system Kafka configuration

* NYX branch (nyx-one-branch)

  * Do not update gain/acquire time for sample camera upon zoom change on NYX
  * Ensure correct VectorProgram used for NYX
  * Generally make sure vector collection works for NYX
  * Longer total exposure time (1000 sec) for NYX
  * Fix detector Z value going into Eiger metadata

Note
----
AMX/FMX will still be using the master branch (instead of a one-branch derivative) as rastering was not fully transitioned to Bluesky before the end of the cycle - note that additional testing time will be necessary once rastering is complete before being suitable for production.

1.0.2 (2022-05-25, a.k.a. 2022-2)
=================================

Fixes
-----
* AMX/FMX branch (master)

  * Improve handling of GUI spreadsheet file selection and spreadsheet import errors
  * Detector distance update when unmounting a sample for AMX
  * Fix incorrect number of steps in energy scan and allow non-integer steps
  * Improve handling when no Chooch output during energy scan
  * Ensure startup files point to code deployed on Lustre (/nsls2/software/mx/daq)
  * Prevent using 777 permissions for visit directory to prevent overriding of
    folder security

* NYX branch (nyx-one-branch)

  * Based on combined code (one-branch)
  * Vector scans now available
  * Publish Bluesky documents to Kafka
  * xlsx spreadsheet files can now be read in

Changes
-------
* Do not move main detector when collecting energy scan or spec raster

1.0.1 (2022-03-11)
==================

This is the version actually deployed onto AMX/FMX.

Fixes
-----

Changes
-------
* New version numbering system details - starting with 2.0 for fully Bluesky release (expected summer 2022). Working backwards, 1.0 for this version.
* AMX/FMX branch (master)

  * Remove ordering of pucks by time (DK) - could not be made to fully work as intended.
  * Use clean conda environments generated via conda-pack-template and deployed with Explorer using Ansible
  * Speed up rastering by simplifying lastOnSample() check
  * FMX annealer code fixed


1.0.0 (2022-02-08)
==================

This version was intended to be the new release but testing could not be completed, resulting in old code 2021-3 being used for the start of the cycle.

Fixes
-----

Changes
-------

* Adding documentation that gets published to the NSLS-II site.
* New version numbering system
* NYX branch (nyx_ophyd) - not yet merged into master

  * LSDC GUI and server starting 
  * Sample exchange through LSDC GUI 
  * Sample centering through LSDC GUI - low and high mag 
  * Standard collection using http://blueskyproject.io/ controlled through LSDC GUI

* AMX/FMX branch (master)

  * complete changeover to cluster processing including all types of processing
  * Ordering of pucks by time for easier selection (DK)

* additional work during the last cycle

  * Use https://github.com/NSLS-II/mx-processing where processing scripts are now centralized, which will run processing software installed on configuration-managed computing nodes (named uranus-cpu<xxx> where <xxx> is a 3-digit number)
  * Update GUI code that allows user to control nodes that will run fast DP and raster processing for new naming scheme of computing nodes
  * FMX annealer – use in and out status PVs 
  * Albula opens with LSDC GUI 
  * Fast DP always runs, control option moved to Staff on GUI 
  * GUI - +/- 1 degree buttons 
  * Kafka encryption set up as central cluster had it enabled 
