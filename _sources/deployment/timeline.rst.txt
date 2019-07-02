Deployment Timeline
*******************

T=0 is defined as the first day that contains a shutdown shift, per the
`NSLS-II Operating Schedule <https://www.bnl.gov/ps/nsls2/opschedule.php>`_.

T - 6 Weeks
===========

* Review open PRs and issues on all projects. Agree on what will and will not
  make it into the release, with 1.5 weeks to push anything over the finishline
  that just needs final touches.

T - 4.5 Weeks
=============

* Defer any unfinished PRs and begin release process.

T - 4 Weeks
===========

* All packages planned for release have had release notes written and tags
  pushed.
* The project-wide documentation has been reviewed and any open issues closed
  or intentionally deferred.

T - 3 Weeks
===========

* The deployment/release manager gathers requirements about beamline-specific packages.
* All of the packages, including beamline-specific ones, have been built.
* The open GitHub issues and PRs on `lightsource2-recipes <https://github.com/NSLS-II/lightsource2-recipes>`_ have been addressed or
  intentionally deferred.

T - 2 Weeks
===========

* Environments have been built and reproducible environments exported.
* The `playbooks <https://github.com/NSLS-II/playbooks>`_ repo has been updated to include new environments and archive
  old ones.

T - 1 Week
==========

* Pushed to all the beamlines and make in-person visit assignments.
* In this final week, handle any unexpected issues.
