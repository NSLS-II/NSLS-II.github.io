2018-08-07 Incompatible Qt Binaries
***********************************

Summary
=======

In a the first trial deployment of a new environment at LIX,
``from PyQt5 import QtCore`` segfaulted.  There was a qt binary from
conda-forge in the ``nsls2-tag`` channel. It is binary incompatible with the
pyqt from the ``anaconda`` channel. Having picked that version of qt pinned a
bunch of other compiled dependencies, we can not install any other version of
qt.

Timeline
========

The offending files were removed from the conda servers. We
re-generated the enviroment yml files (using the same metapackages).

The broken environments were removed from the two beamlines where they had been
deployed:

.. code-block:: bash

   ansible -i production beamlines -a "rm -rf /opt/conda_envs/collection-2018-3.0" --limit=16-ID -kKb
   ansible -i production beamlines -a "rm -rf /opt/conda_envs/analysis-2018-3.0" --limit=16-ID -kKb
   ansible -i production beamlines -a "rm -rf /opt/conda_envs/analysis-2018-3.0" --limit=08-BM -kKb
   ansible -i production beamlines -a "rm -rf /opt/conda_envs/collection-2018-3.0" --limit=08-BM -kKb

The new environments were pushed out in the standard way.

Lessons Learned
===============

What went well
--------------

#. Our acceptance test process led us to catch the problem before we walked
   away from the beamline.
#. We tested at LIX and TES before a wide rollout.

What went wrong
---------------

#. We didn't have clarity that conda-forge binaries containing any native
   extensions should not be copied into ``nsls2-tag``.

Where we got lucky
------------------

Action items
============

These are only sample subheadings. Every action item should have a GitHub issue
(even a small skeleton of one) attached to it, so these do not get forgotten.

Process improvements
--------------------

1. {{ summary }} [link to github issue]
2. {{ summary }} [link to github issue]

Documentation improvements
--------------------------

1. {{ summary }} [link to github issue]
2. {{ summary }} [link to github issue]

Technical improvements
----------------------

1. {{ summary }} [link to github issue]
2. {{ summary }} [link to github issue]
