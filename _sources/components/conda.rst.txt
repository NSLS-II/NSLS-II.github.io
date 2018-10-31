*****
Conda
*****

Conda Installation
==================

We provide a system-wide installation of conda, which enables us to provide it
to all users by default and to configure it in certain ways. Note that this is
different from how individuals usually work with conda, installing it into
their home directories (``~/miniconda3``). We strongly advise users *not* to
install conda on beamline machines, but to use the binary provided by us
at ``/opt/conda/bin/conda``.

Conda Server
============

We deploy our own internal conda server, akin to anaconda.org, where we
store copies of our own packages and mirrored copies of external packages. We
only ever mirror "official" packages built by Anaconda. Anything we else need,
we build ourselves.

We configure conda to use our internal server instead of anaconda.org. We
provide copies of our packages on anaconda.org *as well* as a convenience for
users and collaborators, but we do not use anaconda.org for any machines inside
the Controls network.

Conda Configuration Files
=========================

The system-wide installation of conda looks for its configuration file in
``/opt/conda/.condarc``. Users *should not* create their own configuration
files in ``~/.condarc``; that would override the system configuration, and
conda may not work.

A second configuration file located at ``/etc/xdg/binstar/config.yaml`` tells
conda's web client where to look for packages. Again, we aim it at our internal
conda server instead of anaconda.org.

Conda Environments
==================

Conda is configured to look for packages in two places:

* ``/opt/conda_envs/`` (system)
* ``~/conda_envs`` (user)

The system location requires superuser privileges to change, so we use it to
store stable packages deployed and managed by us. Any user can run them, but
users are not allowed to change them. Users who want to create their own custom
conda environments can put them in the user location.

Conda Environment Files
=======================

An environment file fully specifies a conda environment, including the specific
versions and builds of the all the packages and the channels from which they
were obtained. For each software deployment, we create an ``analysis``
environment file and ``collection`` environment file. We store them in version
control in the ``roles/beamline_envs/files`` directory of the
`NSLS-II/playbooks <https://github.com/NSLS-II/playbooks>`_ repository
(private).

Conda Metapackages
==================

A `metapackage <https://conda.io/docs/glossary.html#metapackage>`_
is a conda package that contains only a list of dependencies but not functional
code itself.

We maintain several metapackages:

* ``analysis``, which depends on libraries for data analysis (e.g.
  scikit-beam), data acess (e.g. databroker) and simulation (e.g. bluesky)
* ``collection``, which depends on ``analysis``, so it includes a superset of
  those dependencies, adding some additional ones only needed for data
  acquisition (e.g. nslsii)
* several beamline-specific packages, with names like ``11-id-chx-analysis`` or
  ``11-id-chx-collection`` that depend on the general ``analysis`` or
  ``collection`` package and add some beamline-specific requirements

They are located in the ``recipes-tag`` directory of
`NSLS-II/lightsource2-recipes <https://github.com/NSLS-II/lightsource2-recipes>`_.
