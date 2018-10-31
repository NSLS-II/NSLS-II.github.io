Re-syncing Conda
****************

Our internal conda server maintains a separate copy of all the packages
provided by "upstream" Anaconda: Python, numpy, conda itself, etc. We
intentionally do not pull in updated versions of these packages during an
operating cycle, to help isolate users from changes that might break things
mid-cycle due to some unintended upgrade.

Before the start of each cycle, we re-synchronize our internal collection of
packages with the latest packages available from Anaconda.

The internal Anaconda server runs on the ``pergamon`` host, inside the Controls
netowork, and it runs as a service account user ``anacodna-server``.

.. code-block:: bash

ssh pegramon
sudo su anaconda-server
cd
export https_proxy=http://proxy:8888
export HTTPS_PROXY=http://proxy:8888

The configuration file ``~/anaconda.yaml`` controls which packages are synced.
Edit it to, for example, update which version(s) of Python we want packages for
this cycle.

Finally, the command to sync is:

.. code-block:: bash

    /opt/continuum/anaconda_server/bin/anaconda-server-sync-conda --mirror-config anaconda.yaml | tee /tmp/update.txt

We have teed the log file into ``/tmp/update.txt``. Download that file using
``scp`` and share it (e.g. in a Basecamp post) in case something goes wrong and
we need to investigate later.
