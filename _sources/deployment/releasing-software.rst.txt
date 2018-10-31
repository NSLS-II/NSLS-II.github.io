Releasing Software
******************

In preparation for a deployment, we typically tag new releases of software,
including major shared projects like bluesky and beamline specific packages
like pyCHX or csxtools.

Obtain access to the project on PyPI
====================================

For a given project, such as `bluesky <https://pypi.org/project/bluesky/>`_,
the list of maintainers is shown on the left of the project page. Ask one of
these people to be added as a maintainer so that you can publish a new release
to PyPI.

Tag and release
===============

We refer you to the
`Publishing Releases <https://nsls-ii.github.io/scientific-python-cookiecutter/publishing-releases.html>`_
section of the Scientific Python Cookiecutter Documentation, which will walk
you through the release process starting with choosing a version number and
ending with publishing the release on PyPI.

Update NSLS-II Conda Recipes
============================

We keep conda recipes for our projects and external projects that we build in
`NSLS-II/lightsource2-recipes <https://github.com/NSLS-II/lightsource2-recipes>`_.
There are two copies of every recipes, one under the ``recipes-tag`` directory
that is pinned to a specific tagged release, and one under the ``recipes-dev``
directory that builds from the ``master`` branch.

We will open a pull request to update the tag and dev recipes for the latest
release. Fork the lightsource2-recipes repo and check out the master branch.

Find the project you have just tagged under ``recipes-tag``. Update the tag
and, if present, the SHA hash. Remember to reset the ``build`` field to 0.

If the project's dependencies have changed since the last release update those
as well. The copy of the recipe under ``recipes-dev`` should be updated to
keeps its dependencies in sync with those in ``recipes-tag``. Since it always
targets ``master``, no other changes are necessary to the dev recipe.

Submit your updates as a pull request. When the PR is merged, our package
builder will automatically find the changes, build the packages, and publish
them. We publish conda packages for each of our projects on an external,
public conda channel https://anaconda.org/lightsource2-tag and on an internal
conda channel ``nsls2-tag``. The name discrepancy is historical. Also be
advised that there is an _abandoned_ public channel
https://anaconda.org/lightsource2 which has very old versions of some packages
and can cause confusion.
