Re-syncing Conda
****************

Our internal conda server maintains a separate copy of all the packages
provided by "upstream" Anaconda: Python, numpy, conda itself, etc. We
intentionally do not pull in updated versions of these packages during an
operating cycle, to help isolate users from changes that might break things
mid-cycle due to some unintended upgrade.

Before the start of each cycle, we re-synchronize our internal collection of
packages with the latest packages available from Anaconda (``defaults`` channel).

The internal Anaconda server runs on the ``alexandria`` host, inside the Controls
network, and it runs as root.

.. code-block:: bash

    ssh alexandria
    sudo su
    bash /opt/builds/bootstrap-mirror-nsls2anaconda-local-folder
    bash /opt/builds/run_conda_index

To modify which packages to synchronize, modify the script found in
`bootstrap-tag-build <https://github.com/NSLS-II/lightsource2-recipes/blob/master/scripts/bootstrapping/bootstrap-tag-build>` and
`nsls2-tag-build-local <https://github.com/NSLS-II/lightsource2-recipes/blob/master/scripts/nsls2-tag-build-local.sh>`_.

.. note::
    ``bash /opt/builds/run_conda_index`` needs to run every time new package is
    added. Information about ``conda index`` can also be found at
    `create-custom-channels <https://conda.io/docs/user-guide/tasks/create-custom-channels.html>`_.

.. note::
    A Token needs to be provided in the script.
    (`creating-access-tokens <https://docs.anaconda.com/anaconda-cloud/user-guide/tasks/work-with-accounts/#creating-access-tokens>`)

Moreover, a sync of ``lightsouce2-tag`` to ``nsls2-tag`` follows a similar process:

.. code-block:: bash

    bash /opt/builds/bootstrap-mirror-nsls2tag-local-folder

We have teed the log file into, ``/root/tmp/mirror-logs/``,
i.e, ``/root/tmp/mirror-logs/2019/01/03/14.25-mirror-nsls2-tag``.
Download that file using ``scp`` and share it (e.g. in a Basecamp post)
in case something goes wrong and we need to investigate later.

This mirroring job for ``nsls2-tag`` is running on ``alexandria`` as a cronjob
every 5 mins. ``conda index`` is also included in a cronjob for every 6 mins.
