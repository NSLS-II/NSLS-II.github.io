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

.. todo:
    Expand this section

Time
----

One of the cornerstones of this data acquisition and analysis method is the use
of *time* as the method by which data can be aligned and correlated. A single
``event`` should have happened at a certain quantum of time with the
determination of what a time *quantum* is left to the details of the
experiment. Time however, can be horrendously messy. Throughout this
section we use two terms, ``timestamp`` and ``time``. These mean:

- ``time`` : The date/time as found at the client side when an ``event`` is
  created. This could be a date-time format as determined by the underlying
  storage method (for example a database)

- ``timestamp`` : A (usually *float*) representation of the hardware time when a
  certain value was obtained. Wherever possible this should be read from
  hardware. For example, this could be the *EPICS* timestamp from when the
  record processed which provides the value. 

We use the literal ``<time>`` to indicate a client side date/time and
``<timestamp>`` to represent the numerical timestamp.

Event Type
----------

In order to allow the **event** concept to be applied to many different events,
events must have a *type*. 
These event types are:

- ``measure`` : A measurement of data from external sources. For example,
  reading a scaler or taking a CCD image. 
- ``analyze`` : The result of a data analysis output.
- ``start_run`` : An event which is created when a data collection run starts.
- ``end_run`` : An event which is created when a data collection run ends. 

.. todo::
    Add dictionary of reserved keys such as ``timestamp``, ``id``
    Expand for data collection, using event model

Events
======

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

Start and End Run Events
------------------------

The beginning of a data collection run creates an event which contains
sufficient metadata and information to describe the data collection. For
example, this is where beamline config information is located. The start run
event also serves as a searchable entity which links all data associated by an
event. For example::

    {
        "uid" : <unique_id>,
        "scan_id" : <non-unique-id>,
        "beamline_id: : <string>,
        "sample" : {
            "uid" : <unique_id>
            "id" : <number>,
            "description" : <string>
        }
        "project" : <string>,
        "beamline_config" : {
            "diffractometer" : {
                "geometry" : <string>,
                "xtal_lattice" : {
                    "a" : <float>,
                    "b" : <float>,
                    "c" : <float>,
                    "alpha" : <float>,
                    "beta" : <float>,
                    "gamma" : <float>
                }
                "UB" : [...]
            }
        },
        "time" : <time>
    }

With the corresponding end run event as::

    {
        "uid" : <id>,
        "run_hdr" : <id>,
        "reason" : <string>,
        "time" : <time>,
        "start_id" : <unique_id>
    }

The field ``reason`` can be used to describe why a run ended e.g. was it aborted or
was there an exception during data collection. The field ``start_id`` is a
pointer to the start event. 

.. _measure_events:

Measure Events and Event Descriptors
------------------------------------

Measure events contain the data measured at a certain instance in time or
explicit point in a sequence. For example ::

    {
        "uid" : <unique_id>,
        "seq_num" : <integer>,
        "ev_desc" : <unique_id>,
        "data" : {
            "chan1" : {"value" : <value>, "timestamp" : <ts>},
            "chan2" : {"value" : <value>, "timestamp" : <ts>},
            "chan3" : {"value" : <value>, "timestamp" : <ts>},
            "chan4" : {"value" : <value>, "timestamp" : <ts>},
            "chan5" : {"value" : <value>, "timestamp" : <ts>},
            "chan6" : {"value" : <value>, "timestamp" : <ts>},
            "chan7" : {"value" : <value>, "timestamp" : <ts>},
            "chan8" : {"value" : <value>, "timestamp" : <ts>},
            "pimte" : {"value" : <unique_id>, "timestamp" : <ts>}
        }
        "time" : <time>
    }

Where the keys ``uid``, ``ev_desc``, ``time`` and ``timestamp`` refer to 
the unique id, a link to the event descriptor the time and the EPICS timestamp 
respectively.

The field ``seq_num`` is used to order the events in the order in which they were
created.

Event descriptors are used to describe an array of events which can form an
event stream of a collection of events. For example a run forms
event_descriptors at run start to define the data collected. For the example
above ``event`` is described by the ``event_descriptor`` ::

    {
        "uid" : <unique_id>,
        "type" : "measure",
        "keys" : {
            "chan1" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S1"},
            "chan2" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S2"},
            "chan3" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S3"},
            "chan4" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S4"},
            "chan5" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S5"},
            "chan6" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S6"},
            "chan7" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S7"},
            "chan8" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S8"}, 
            "pimte: : {"source" : "FILESTORE:<...>"}
        },
        "run_hdr" : <unique_id>,
        "time" : <time>
    }

