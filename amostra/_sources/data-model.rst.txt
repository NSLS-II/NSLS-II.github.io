==========
Data Model
==========

The data model includes:

* Sample
* Container

For each type we document here the formal schema, given as a
`JSON schema <https://json-schema.org/understanding-json-schema/>`_.
When objects are created or updated, the proposed change is validated against
the corresponding schema and rejected if it fails to satify it.

Sample
======

.. literalinclude:: ../../amostra/schemas/sample.json

Container
=========

.. literalinclude:: ../../amostra/schemas/container.json

Project
=======

.. literalinclude:: ../../amostra/schemas/project.json

Owner
=====

.. literalinclude:: ../../amostra/schemas/owner.json

Institution
===========

.. literalinclude:: ../../amostra/schemas/institution.json
