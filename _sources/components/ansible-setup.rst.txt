******************************
NSLS-II DAMA Ansible Playbooks
******************************

Historical Note: This repository began as a fork of
jupyterhub/jupyterhub-deploy-teaching. It has grown from JupyterHub playbook to
a general collection of playbooks for DAMA.

Getting Started
===============

These playbooks use your local SSH configuration (see
https://docs.ansible.com/ansible/latest/faq.html#how-do-i-get-ansible-to-reuse-connections-enable-kerberized-ssh-or-have-ansible-pay-attention-to-my-local-ssh-config-file
for more info) to hop into the BNL network and then into the NSLS-II controls
network. Your ``~/.ssh/config`` must include a host named ``ossh``
("outer ssh") configured like this or similar:

.. code-block:: bash

   Host bnl
       HostName ssh.bnl.gov
       ForwardAgent yes

   Host ossh
        ForwardAgent yes
        ProxyCommand ssh -q bnl nc ssh.nsls2.bnl.gov 22

If instead you are connecting to the NSLS-II controls network after VPNing into
the BNL network then your ``~/.ssh/config`` must include a host named ``issh``
("inner ssh") configured like this or similar:

.. code-block:: bash

   Host issh
        HostName ssh.nsls2.bnl.gov
        user awalter
        ForwardAgent yes

It is recommended, but not required, that you include both. It is also necesary
to update ``playbooks/group_vars/all`` from:

.. code-block:: bash

   ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q ossh"'

to:

.. code-block:: bash

   ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q issh"'


The inventory variables include some encrypted variables, using ansible-vault.
To use any of these playbooks, you will need the vault password, which is stored
in LastPass. As of this writing, Stuart Campbell, Thomas Caswell, and Daniel
Allan have access to it. Stash the password in file named
``vault_password_file`` in the root directory of this repository.

You will also need sudo access on the hosts you want to change if that change
requires privilege escalation.

.. note::

    The ``ansible-conda`` submodule should be copied locally using the
    following command:

    .. code-block:: bash

        git submodule update --init --recursive

.. note::

    You should have a few files in the ``security`` directory, which
    can be found on the jupyterhub server:
    - ``cookie_secret``
    - ``ssl.crt``
    - ``ssl.key``

Organization
============
Inventories
-----------

There are two inventories: staging and production. Currently, the only
staging host is jupyterdev, for testing JupyterHub deployments. There is no
staging host for beamline deployments, but there should be.

Playbooks
---------

As suggested by Ansible best practices(docs.ansible.com/ansible/latest/playbooks_best_practices.html),
there is one playbook per "kind" of machine we deploy to: ``jupyterhub.yml`` and
``beamlines.yml``.

Deploying
=========

A Simple Ping Test to Get Started
---------------------------------

.. code-block:: bash

   ansible -i production beamlines -m ping


where ``production`` refer to an inventory file in this repository,
``beamlines`` is a group of hosts in that inventory, and ``ping`` is a built-in
Ansible module.

JupyterHub
----------

The JupyterHub playbook configures a machine to run the JupyterHub process
and single-user notebook server processes.

Deploy it to the staging inventory first, which updates
https://notebook-dev.nsls2.bnl.gov.

.. code-block:: bash

   ansible-playbook -i staging jupyterhub.yml -bkK

If all works as expected, update https://notebook.nsls2.bnl.gov:

.. code-block:: bash

   ansible-playbook -i production jupyterhub.yml -bkK


Beamlines
---------

The Beamlines playbook installs databroker configuration files and creates
conda environments based on environment files.

.. code-block:: bash

   ansible-playbook -i production beamlines.yml -bkK


Changing default environments
-----------------------------

This should only be used in a targeted way, one beamline at a time.

Update the ``current_env_tag`` under the beamline in question in ``production``
(location in the root of the repo).

Use ``--limit=XXX`` to target the playbook to the servers on one beamline, where
``XXX`` may be for example ``04-ID``.

.. code-block:: bash

   ansible-playbook -i production update_default_vars.yml --limit=XXX -bkK


Where to Make Changes
*********************

Updating conda
--------------

Note that `conda update -n root conda` is not always sufficient because the root
environment way have an old version of Python no longer supported by conda.
Instead, use `conda install -n root python=3.6 conda``. (I use ``python=3.6``, 
the latest version as of this writing, but that should be updated the latest stable
Python.)

.. code-block:: bash

   ansible -i production beamlines -a "/opt/conda/bin/conda install -n root python=3.6 conda" -bkK


New hosts
---------

Edit ``production``.

New databroker configuration
----------------------------

Add a file to ``roles/databroker_config/files/`` and deploy the beamline
playbook.

.. warning::

    This will also update the databroker configuration file for ALL conda
    enviroments, it may render the older enviroments unusable.


New Environments
----------------

Add a file to ``roles/beamline_envs/files/`` and deploy the beamline
playbook.

New kernels
-----------

Add items to the ``kernelspecs`` section in ``group_vars/jupyterhub_hosts`` and
deploy the ``jupyterhub`` playbook. Additional info is given in the comments in
that file.

Fresh installation
------------------

Add keys

.. code-block:: bash

   ssh-copy-id xf18id-ws1
   ssh-copy-id xf18id-ws2


Run the beamlines playbook.

.. code-block:: bash

   ansible-playbook -i production beamlines.yml --limit=18-ID -bkK
