.. Packaging Scientific Python documentation master file, created by
   sphinx-quickstart on Thu Jun 28 12:35:56 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Amostra
=======

Amostra is a sample management service for scientific experiments. It is backed
by MongoDB.

Users can connect directly to a MongoDB (suitable for personal use or testing)
or connect to an HTTP server with a RESTful API. Amostra provides a Python
client for each of these modes that present identical interfaces to the user.

.. toctree::
   :maxdepth: 2

   installation
   usage
   data-model
   reference
   release-history
