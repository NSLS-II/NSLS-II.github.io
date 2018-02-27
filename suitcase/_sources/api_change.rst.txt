.. _api_changes:

=============
 API changes
=============


v0.6.0
======


``suitcase.hdf5.export``
------------------------

Replaced input parameter mds with db in ``export`` function. db=None is set as default and put at
the end of the input argument list. This change will facilitate the usage of
other functions of databroker, intead of only those from metadatastore.

The future version of header will include databroker, like hdr.db. This
update will be taken care of later.

``suitcase.spec``
-----------------
Replaced input parameter mds with db in all functions in spec.py. db=None is set as default.

``suitcase.nexus``
-----------------
Replaced input parameter mds with db in all functions in nexus.py. db=None is set as default.
