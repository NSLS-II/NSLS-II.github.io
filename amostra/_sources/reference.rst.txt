=========
Reference
=========

Clients
=======

.. autoclass:: amostra.http_client.Client
   :members:

.. autoclass:: amostra.mongo_client.Client
   :members:

Objects Representing Documents
==============================

None of these should be directly *instanted* by the user; they should be
returned by a Client.

.. autoclass:: amostra.objects.Sample
   :members:

.. autoclass:: amostra.objects.Container
   :members:

.. autoclass:: amostra.objects.Project
   :members:

.. autoclass:: amostra.objects.Owner
   :members:

.. autoclass:: amostra.objects.Institution
   :members:

API
===

.. openapi:: openapi.json
