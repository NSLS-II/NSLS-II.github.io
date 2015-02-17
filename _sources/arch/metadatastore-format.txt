*******************************
Format of Metadatastore Entries
*******************************

Introduction
============

The metadatastore is based on the concept of documents which are either
events, or descriptions of events.  An ``event`` is a quantum of data
stored in the metadata store and represents an *action* at a given time. For
example: "*measurement of 8 scaler chanels*", "*trigger detectors*" or
"*start run*".

Expanding the notion of **events**, these can also be used for derived data.
For example, an event could be the result of a data analysis or reduction
routine which was run at a certain time.

The document schemas in this document are written using ``jsonschema``.  The
full spec http://json-schema.org/ is basically un-readable.  A more readable
introduction https://spacetelescope.github.io/understanding-json-schema/index.html.


.. todo::
    Expand this section




Time
====

One of the cornerstones of this data acquisition and analysis method is the use
of *time* as the method by which data can be aligned and correlated. A single
``event`` should have happened at a certain quantum of time with the
determination of what a time *quantum* is left to the details of the
experiment. Time however, can be horrendously messy. Throughout this
section we use two terms, ``timestamp`` and ``time``. These mean


time
    The date/time as found by the client when an ``event`` is
    created.  This could be a date-time format as determined by the underlying
    storage method (for example a database).

timestamp
   A (usually *float*) representation of the hardware time when a
   certain value was obtained. Wherever possible this should be read from
   hardware. For example, this could be the *EPICS* timestamp from when the
   record processed which provides the value.


We use the literal ``<time>`` to indicate a client side date/time and
``<timestamp>`` to represent the numerical timestamp.

.. todo::
    Add dictionary of reserved keys such as ``timestamp``, ``id``
    Expand for data collection, using event model


Documents
=========

.. xfig:: mds.fig


Events view of the world
========================

Events are the smallest quantum of data stored in the metadatastore. They group
values which are associated with temporally bundled data. The definition of
"temporally identical" is determined by the DAQ system. For example, the 32
channels in a scaler can be considered to be temporally identical because they
are hardware synchronized. Inclusion of a CCD image (with a reference to the
file store) can be included if this event is triggered at the same time, either
by software or hardware.  Each ``event`` contains the data values and a client
side timestamp of when the even was created. The same logic is applied to
``trigger events``. These are grouped with temporally identical triggers (again
determined by the DAQ philosophy).



Event Descriptor Document
=========================
.. highlight:: json

Schema
++++++

.. schema_diff::

    // Proposed
    ev_desc_prop.json
    --
    // as documented
    ev_desc_doc.json
    --

    // As currently (1c2246d) implemented
    ev_desc_impl.json


Definitions
+++++++++++

data_key
~~~~~~~~
{"source": "NAMESPACE:NAME", "external": "NAMESPACE:NAME"}

source
  The reference to the physical piece of hardware that produced this data

external, optional
  The reference to the location where the data is being stored.
  If this key is not present, then the data is stored inside the data
  field of the corresponding ``Event`` document.
  If this key is present, then the ``value`` field of the ``data``
  dictionary inside the ``Event`` document is interpreted as a unique
  key that can be used to retrieve corresponding data from the
  service described by the value of the ``external`` key

The values of both =source= and =external= are (=namespace=, =name=) pairs.
The name is obligatory for source and optional for external

NAMESPACE
   Things like ``PV`` or ``FileStore``.
NAME
   Thing in the name space.



Example
+++++++

Event descriptors are used to describe an array of events which can form an
event stream of a collection of events. For example a run forms
event_descriptors at run start to define the data collected. For the example
above ``event`` is described by the ``event_descriptor``

.. ipython:: python

  import json
  import jsonschema
  ev_desc = {
      "uid": "f05338e0-ed07-4e15-8d7b-06a60dcebaff",
      "keys": {
          "chan1": {"source": "PV:XF:23ID1-ES{Sclr:1}.S1", "dtype": "number", "shape": None},
          "chan2": {"source": "PV:XF:23ID1-ES{Sclr:1}.S2", "dtype": "number", "shape": None},
          "chan3": {"source": "PV:XF:23ID1-ES{Sclr:1}.S3", "dtype": "number", "shape": None},
          "chan4": {"source": "PV:XF:23ID1-ES{Sclr:1}.S4", "dtype": "number", "shape": None},
          "chan5": {"source": "PV:XF:23ID1-ES{Sclr:1}.S5", "dtype": "number", "shape": None},
          "chan6": {"source": "PV:XF:23ID1-ES{Sclr:1}.S6", "dtype": "number", "shape": None},
          "chan7": {"source": "PV:XF:23ID1-ES{Sclr:1}.S7", "dtype": "number", "shape": None},
          "chan8": {"source": "PV:XF:23ID1-ES{Sclr:1}.S8", "dtype": "number", "shape": None},
          "pimte": {"source": "CCD:name_of_detector", "external": "FILESTORE",
                    "dtype": "array", "shape": [1254, 2014]}
      },
      "begin_run_event": "2dc386b5-cfee-4906-98e9-1a8322581a92",
      "time": 1422940263.7583334,
  }
  with open('source/arch/ev_desc_prop.json') as fin:
      schema_prop = json.load(fin)

  jsonschema.validate(ev_desc, schema_prop) is None

Note that ``validate`` returns ``None`` for documents that pass and raises
exceptions for those that do not.

Discussion points
+++++++++++++++++

- Should ``begin_run_event`` be a mandatory?


Event Documents
===============

Schema
++++++
.. schema_diff::
  // As documented
  event.json
  --

  // As implemented

  {
      "definitions": {
          "data": {
              "properties": {
                  "timestamp": {
                      "type": "number"
                  },
                  "value": {
                      "type": [
                          "string",
                          "number"
                      ]
                  }
              },
              "required": [
                  "value",
                  "timestamp"
              ],
              "type": "object"
          }
      },
      "properties": {
          "data": {
              "additionalProperties": {
                  "$ref": "#/definitions/data"
              },
              "type": "object"
          },
          "descriptor": {
              "type": "string"
          },
          "seq_no": {
              "type": "number"
          },
          "time": {
              "type": "number"
          },
          "time_as_datetime": {
              "type": "string"
          }
      },
      "required": [
          "data",
          "time",
          "descriptor",
	  "seq_no"
      ],
      "type": "object"
  }


The field ``seq_num`` is used to order the events in the order in which they were
created.

Example
+++++++

Measure events contain the data measured at a certain instance in time or
explicit point in a sequence. For example::

    {
        "uid": "4609e51f-cf38-4c2a-a6ea-483edc461e43",
        "seq_num": 42,
        "descriptor": "f05338e0-ed07-4e15-8d7b-06a60dcebaff",
        "data": {
            "chan1": [3.14, 1422940467.3101866],
            "chan2": [3.14, 1422940467.3101866],
            "chan3": [3.14, 1422940467.3101866],
            "chan4": [3.14, 1422940467.3101866],
            "chan5": [3.14, 1422940467.3101866],
            "chan6": [3.14, 1422940467.3101866],
            "chan7": [3.14, 1422940467.3101866],
            "chan8": [3.14, 1422940467.3101866],
            "pimte": ["8cad7f02-c3e1-4e76-a823-94a2a7d23f6b",
                      "timestamp": 1422940481.8930786]
        },
        "time": 1422940508.3491018,
    }

Where the keys ``uid``, ``ev_desc``, ``time`` and ``timestamp`` refer to
the unique id, a link to the event descriptor the time and the EPICS timestamp
respectively.


Start Run Events
================


Schema
++++++
.. schema_diff::

  // As documented
  begin_run_event.json
  --

  // As implemented

  {
        "properties": {
          "beamline_config": {
              "type": "object"
          },
          "beamline_id": {
              "type": "string"
          },
          "custom": {
              "type": "object"
          },
          "owner": {
              "type": "string"
          },
          "scan_id": {
              "type": "string"
          },
          "time": {
              "type": "number"
          },
          "time_as_datetime": {
              "type": "string"
          }
      },
      "required": [
         "time",
         "owner",
         "beamline_id"
      ],
      "type": "object"
  }


Example
+++++++

The beginning of a data collection run creates an event which contains
sufficient metadata and information to describe the data collection. For
example, this is where beamline config information is located. The start run
event also serves as a searchable entity which links all data associated by an
event. For example::

    {
        "uid": "2dc386b5-cfee-4906-98e9-1a8322581a92",
        "scan_id": "ascan_52",
        "beamline_id": "CSX",
        "sample": {
            "uid": "0a785292-05c5-4c1b-bd9a-f2dd5b0580c8",
            "id": 9,
            "description": "A small piece of cheese"
        },
        "project": "Cheese_shop",
        "beamline_config": {
            "diffractometer": {
                "geometry": "swiss",
                "xtal_lattice": {
                    "a": 1.1,
                    "b": 2.2,
                    "c": 3.3,
                    "alpha": 4.4,
                    "beta": 5.5,
                    "gamma": 6.6
                },
                "UB": [1, 2, 3, 4]
            }
        },
        "time": 1422940625.2198992,
        "owner": "jcleese",
        "group": "monty"


    }



End Run Events
==============

Schema
++++++

.. schema_diff::

  // As Documented
  end_run_event.json
  --
  // As implemented


  {
      "properties": {
          "begin_run_event": {
              "type": "string"
          },
          "custom": {
              "type": "object"
          },
          "reason": {
              "type": "string"
          },
          "time": {
              "type": "number"
          },
          "time_as_datetime": {
              "type": "string"
          }
      },
      "required": [
          "begin_run_event",
          "time"
      ],
      "type": "object"
  }


Example
+++++++


With the corresponding end run event as::

    {
        "uid": "60bac4c7-e2d3-4c4b-a553-3790a8add866",
        "begin_run_event": "2dc386b5-cfee-4906-98e9-1a8322581a92",
        "reason": "This shop does not contain any cheese",
        "completion_state": "fail",
        "time": 1422940679.72617,
    }

The field ``reason`` can be used to describe why a run ended e.g. was it aborted or
was there an exception during data collection. The field ``begin_run_event`` is a
pointer to the start document.
