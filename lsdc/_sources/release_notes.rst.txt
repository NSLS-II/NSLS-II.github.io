=================
 Release History
=================

1.0.0 (2022-02-08)
==================

Fixes
-----

Changes
-------

* Adding documentation that gets published to the NSLS-II site.
* New version numbering system.
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
