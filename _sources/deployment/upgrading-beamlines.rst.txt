Upgrading Beamlines
*******************

Once a new environment has been deployed to a beamline, we visit in person to
test the new environment and "move" the default behavior of ``bsui`` to point
to the new environment.

Test the new environment
========================

For testing, use the ``BS_ENV`` environment variable to temporarily override
the default behavior for ``bsui``.

.. code-block:: bash

   BS_ENV=collection-YYYY-X.V bsui

where ``YYYY-X.V`` is a version such as ``2018-3.0``.

Change bsui's default environment
=================================

We do this from ansible, affecting all machines at a beamline together. It is
important to do this using ansible so that our centralized record of which
environment a given beamline is using remains accurate.

In the ``production`` inventory file, located in the root directory of the
NSLS-II/playbooks repository, find the beamline of interest and update its
``curent_env_tag`` variable and then open a PR to NSLS-II/playbooks so that the
change is recorded in the master branch. Here is an excerpt:

.. code-block:: ini

   ### SIX ###

   [02-ID-1:vars]
   current_env_tag="2018-3.0"

Now deploy the change using the ``update_default_vars.yml`` playbook. Use
``--limit=XXX`` to target the playbook to the servers on the beamline of
interest. This is important! This step can occur prior to the PR opened above
being merged, as it will use the local version of ``production``.

.. code-block:: bash

   ansible-playbook -i production update_default_vars.yml --limit=XXX -kK

where ``XXX`` may be for example ``02-ID-1``.
