.. highlight:: bash

Releases and Deployment
***********************

Creating a Release Version
==========================
#. Decide what the new new version number will be
#. Write release notes / collapse whats_new and api_changes folders
#. Create a new commit, version bumping as needed. Commit
   message should be truncated release notes.
#. create annotated tag on release commit, text should be truncated release
   notes.  Tag format is `vX.Y.Z`
#. create new commit version bumping back to dev version pattern as needed
#. check to make sure everything looks right
#. push to master branch
#. push tag
#. create new conda recipe in conda-prescriptions/releases, updating
   as needed
#. use build server or beamline computer to build conda package
#. upload to proper internal binstar organization(s)
#. rebuild (all) the docs

Decide on version number
------------------------

We are using `semantic versioning`_ guidelines and :pep:`440`.  Each
tagged version number is of the form ``vMajor.Minor.Patch``.  Roughly,
versions bumping the ``Major`` version can make backwards incompatible
API changes, versions bumping ``Minor`` can add backwards-compatible
new features and versions bumping ``Patch`` can make
backwards-compatible bug fixes.  Bumping a version component re-sets
everything to the right to 0.  So long as the ``Major`` version is 0, the
rules do not apply.

PEP440 defines a way of adding qualifiers to a version string to
ensure proper sorting of development releases.  The rules are quite
general and specify how to sort multiply stacked pre- and post-
releases.  We will only be using a very simple case and all of our
development releases should look like ``vX.Y.Z.postN+gHEXVAL`` which
say that this the ``N`` commit after release ``vX.Y.Z`` and with the
git SHA1 ``HEXVAL``.  This should mostly be dealt with automatically
by the build tools.

In the future we may have the need to do release candidates.

.. _semantic versioning: http://semver.org/

Release notes/ API changes
--------------------------

The release notes should be a succinct document which
summarizes the accumulated changes sense the last version.
It is particularly important to document **all** API changes.

Each repository should have a folder in the docs directory for new
features (:file:`whats_new`) and for api changes (:file:`api_changes`).
Collect all of the files into this folder into the top-level
:file:`*.rst`.


An abbreviated version of the release notes will go in the release
commit message + the tag annotation.


Version bump / Release commit
-----------------------------
On the branch you plan to cut the release off do the version bumping
as needed.  Currently this require changing

- version number in ``setup.py``
- ``__version__`` in ``__init__.py``

This will be simplified if/when we adopt ``versioneer``.

The commit message should look something like::

   REL : v0.1.0

   This releases fixes a number of bugs in the Aardvark
   and adds new features to whizbang class.

   Bugs fixed:
     - Aardvarks can eat ants again
     - tunnels no longer list to the left

   Features added:
     - Color of ``whizbang`` explosion is now tunable


Create Tag
----------

Create an annotated tag on the release commit. The annotation should
match that of the commit you are tagging.


Version bump back to dev versions
---------------------------------

Bump the version in :file:`setup.py` and :file:`__init__.py` to
``v.X.Y.Z.post0``.  This step can be eliminated if/when we adopt
``versioneer``.


Check your work
---------------

Take some time to consider what you have just done and make sure
everything looks right.  Run some local tests, install off the tagged
commit to make sure the versions are ok.  Run the tests locally.  Make
sure that the dev version of the conda package still builds.

Once a tag is made public it can not be taken back!

Push everything
---------------

Push the branch with your new commits + the tag up to the canonical
repository.

Create conda recipe for release
-------------------------------

In `conda-prescriptions
<https://github.com/NSLS-II/conda-prescriptions>`_ create a new recipe
in :file:`releases/project/vX.Y.Z`.  This is most easily done by
copying and updating the recipe from the previous version.  You will
need to update at least the ``version`` string ande the ``git_rev``.
In addition you may need to update the imports that are tested and the
dependencies if they have changed between versions.


Build and upload new binaries
-----------------------------

Use either the :ref:`binstar build server <binstar_build>` or by using
``conda build`` on one of the beam line computers to build the conda
package off of your newly created recipe.  ::

  cd conda-prescriptions
  conda build releases/project/vX.Y.Z

Before uploading this file to the internal binstar you should make
sure it installs locally.  Once you are satisfied that everything
is working correctly, upload it to the internal binstar ::

  binstar upload `conda build releases/project/vX.Y.Z --output` -u USER

where ``USER`` is the user or organization you want to upload the
binary to.  To upload to more than one beamline either simply run
the above command more than once, or use :prog:`binstar` to move
the files between organizations ::

  binstar copy --to-owner USER2 USER1/project/vX.Y.Z

Rebuild all of the documentation
--------------------------------

Rebuild both the project specific documentation and the over-all
NSLS-II documentation and push to the correct github.io locations.



Building an Untagged Commit
===========================

It is possible to build and upload a conda package from an untagged
commit.  The recipes in the project repositories are set up so that
the version reported to conda will be the last tag with
`.postN+gHEXVAL` appended to the end.  This will allow conda to
correctly sort versions so long as all of the builds are off of the same
branch.  However, these binaries should only be deployed to beamlines
in exceptional circumstances.
