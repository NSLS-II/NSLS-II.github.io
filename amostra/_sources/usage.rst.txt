=====
Usage
=====

Setup
=====

Users can connect directly to a MongoDB (suitable for personal use or testing)
or connect to an HTTP server with a RESTful API. Amostra provides a Python
client for each of these modes that present identical interfaces to the user.

Direct Connection to MongoDB
----------------------------

For direct connection to MongoDB without an HTTP server in the middle, use
:class:`amostra.mongo_client.Client`.

.. code:: python

   import amostra.mongo_client
   client = amostra.mongo_client.Client('mongodb://localhost:27017/amostra_demo')

HTTP Server and Client
----------------------

On a machine with access to the MongoDB server, start amostra's HTTP server.
There is only one required option: the URI for a MongoDB database. Note that a
database name must be included in the URI, as in ``test_amostra`` below. Any
database name may be used, and it will be created if it does not yet exist.

.. code:: bash

   $ python -m amostra.server --mongo_uri='mongodb://localhost:27017/test_amostra'
   [I 190802 15:24:41 server:62] Listening on 0.0.0.0:5000, path None

See ``python -m amostra.server --help`` for more options, including SSL support
and a custom base URL.

On any machine that can see that server, use
:class:`amostra.http_client.Client`.

.. code:: python

   import amostra.mongo_client
   client = amostra.http_client.Client('http://localhost:5000')

.. ipython:: python
   :suppress:

   import amostra.mongo_client
   URI = 'mongodb://localhost:27017/amostra_demo'
   client = amostra.mongo_client.Client(URI)
   # Drop the demo database to clean data from any previous builds.
   client._db.client.drop_database('amostra_demo')

Using the Client
================

Create a new Sample.

.. ipython:: python

   s = client.samples.new(name='peanut butter')
   s
   s.name

Update a trait of the sample.

.. ipython:: python

   s.name = 'jelly'
   s

And again.

.. ipython:: python

   s.name = 'grape jelly'
   s

All revisions are automatically persisted in the database and can be accessed.
The most recent revisions are given first.

.. ipython:: python

   list(s.revisions())

.. note::

   The Sample has two read-only traits that are used internally:

   .. ipython:: python

      s.uuid
      s.revision

   A Sample is automatically given a uuid when it is created. All revisions of
   that Sample share that same uuid, but the combination of uuid and revision
   number is globally unique. The revision is incremented on each update.

Create several more samples, and then search to find one.

.. ipython:: python

   client.samples.new(name='coffee')
   client.samples.new(name='tea')
   client.samples.new(name='water')
   s = client.samples.find_one({'name': 'tea'})
   s

Searches that are expected to return potentially more than one result, such as
a search for *all* samples, look like this.

.. ipython:: python

   results = client.samples.find({})
   results

The search results are given as a *generator*, a lazy object that pulls data on
demand, to avoid clobbering the system if the set of results is large. To pull
just one result we can use ``next``.

.. ipython:: python

   s = next(results)
   s

To pull them all we can use ``list``.

.. ipython:: python

   results = client.samples.find({})
   list(results)

Note that the ``revisions`` result above worked in the same way.
