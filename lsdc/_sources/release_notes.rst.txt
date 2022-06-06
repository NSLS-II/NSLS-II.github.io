=================
 Release History
=================

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
