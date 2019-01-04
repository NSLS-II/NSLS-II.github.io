**************************
Deploying New Environments
**************************

This section describes how to define and deploy a new software (conda)
environment to beamlines. We typically do this during the downtime between
operating cycles. In the future, as cycles become longer and the deployment
process becomes more streamlined, we will probably also deploy "patch releases"
during maintenance windows in the middle of an operating cycle.

Deploying the environment just makes it *available*; it does not actually
affect beamline operations; i.e. the default behavior of ``bsui`` is
unchanged. We'll address that in the next section.

See :doc:`../conda` for background on the function and location of the
components involved here.

Overview
========

We will update the requirements list in the **metapackages**, a human-friendly
specification of our direct requirements. From the metapackages we will
generate **environment files**, an explicit, pinned specification of all the
requirements including indirect dependencies. The environment files will serve
as the canonical definition of software environments.

Updating the Metapackages
=========================

#. Update the requirements listed in the ``analysis`` and ``collection``
   metapackages. Also update any beamline-specific metapackages if the
   beamlines' requirements have changed.

#. Notice that certain requirements have minimum versions specified to ensure
   that conda resolves the right version. We do this selectively (not on _all_
   packages) to reduce the maintenace burden. Update these specifiers as
   needed.

#. Finally, when you are ready to publish the new metapackages, submit a PR
   that bumps the version numbers in the recipes. The metapackages have the
   versioning scheme ``{{ year }}C{{ cycle }}.{{ version }}``, such as
   ``2018C3.0``.  The ``{{ version }}`` is used for mid-cycle patch rollouts.

As with :doc:`software releases <releasing-software>`, the builder
will detect the change and make the new metapackage available on the conda
server.

Revoking a Bad Metapackage
--------------------------

We often discover a mistake in a metapackage shortly after publishing it. If
the metapackage has already been deployed to beamlines, it should not be
deleted; instead a new version should be released. But if we catch the error
early, during deployment, we remove the bad metapackage and re-publish under
the same version number.

#. Delete the package from the public conda channel. Visit
   https://anaconda.org/lightsource2-tag/analysis/files and/or
   https://anaconda.org/lightsource2-tag/collection/files. Log in. Delete the
   offending files.

#. Delete the package from the internal conda channel: ssh to ``alexandria``
   (which is inside the Controls network) and run:

   .. code-block:: bash

      sudo rm -f /www/conda/nsls2-tag/linux-64/analysis-XXX-0.tar.bz2
      sudo rm -f /www/conda/nsls2-tag/linux-64/collection-XXX-0.tar.bz2

   where ``XXX`` is a version like ``2018C3.0``.

The order is important because the "mirroring" agent that copies packages from
the public conda channel to the internal one can undo your work! To avoid this,
we deleted the external/public copy first.

Defining Environments
=====================

#. Log in to any server on the Controls network that has conda installed (e.g
   xf23id1-srv1)

#. Create an analysis environment:

   .. code-block:: bash

      conda create -y -p /tmp/analysis-YYYY-X.V analysis=YYYYCX.V --override-channels -c http://alexandria/conda/nsls2-tag -c http://alexandria/conda/defaults


   where ``YYYYCX.V`` is a version like ``2018C3.0``. This resolves the
   specifications encoded in the metapackage into a specific set of packages.

#. Export the set of packages into an environment file:

   .. code-block:: bash

      conda env export -p /tmp/analysis-YYYY-X.V -f ~/analysis-YYYY-X.V.yml --override-channels -c http://alexandria/conda/nsls2-tag -c http://alexandria/conda/defaults

#. Repeat the above, substituting ``collection`` for ``analysis``.

#. Manually edit the files to delete the ``prefix: /tmp/...`` entry and to sort
   the ``dependencies:`` section alphabetically. This makes it easier to
   compare diffs.

We don't bother creating environments out of the other, beamline-specific
metapackages, purely to save time and effort. This means they are less strictly
defined and not as perfectly reproducible as the base ``analysis`` and
``collection`` environments. In the future this could be made practical through
automation.

Deploying the Environments
==========================

#. Copy the environment files into the ``beamline_envs`` Ansible role.

   .. code-block:: bash

      cd playbooks/roles/beamline_envs/files
      scp <host>:~/analysis-YYYY-X.V.yml .
      scp <host>:~/collection-YYYY-X.V.yml .

#. We typically keep the two newest environments in ``beamline_envs/files`` and
   move anything else to ``beamline_envs/archived``. The old environments will
   thus not be deployed to new systems, but they remain easy to discover and
   reference.

   .. code-block:: bash

      git mv <old environment file> ../archived

#. Commit the changes and open a pull request against the playbooks repository.

#. Use ansible to copy the environment file onto all beamline workstations and
   servers and create an environment from it. Start by testing it on one
   beamline using ``--limit=02-ID``

   .. code-block:: bash

      ansible-playbook -i production beamlines.yml -kK --limit=02-ID

   If that completes successfully, log into the machine and check that the
   environment can be activated and that the expected versions of a couple
   libraries are importable.

   .. code-block:: bash

      conda activate analysis-YYYY-X.V
      python

   .. code-block:: python 

      import bluesky
      bluesky.__version__  # Check that you get the right version.

   If all looks good, deploy to all machines.

   .. code-block:: bash

      ansible-playbook -i production beamlines.yml -kK

   Keep a record of any failures.  The most common failure mode is a server
   being temporarily offline or inaccessible on the network. When that happens,
   try again later, using ``--limit`` to target the missed machines.
