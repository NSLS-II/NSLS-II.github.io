DataBroker mini-hackathon
=========================


Dates: Feb 26 - Mar 2

1000 - 1800 M-Th
1000 - 1600 Fri

Goals
*****

 - produce planning artifacts to support DOE hackathon in June:

   1. high level design documents (requirements, goals) for modules
      - use cases
   2. low level design documents (proposed API documentation)

 - sort out priority and interdependence of high

   - where do we have duplicate effort between facilities?
   - where do we have gaps in effort?
   - what can we get 'good enough' un-block other work
   - where can we work in parallel?
   - where must we work serially?


High-level Requirements
***********************

1. \*-as-a-service

   - as first pass, preserve python API, rip out guts

     - worry about nice REST/RPC interface later

   - wire protocol for small data

     - json, bson, msgpack

   - wire protocol for big data

     - msgpack, epics (v3 or v7), custom, h5serv

   - ops

     - ansible / kubernetties

2. authorization

   - do we need to look at how 'role based' auth work?
   - probably want to develop a common set of nouns / tools for our
     use and then shim against home institution systems
   - user groupings

     - user (ex 1 person)
     - proposal (application to get beam time)

       - one or more PI
       - zero or more 'users'

     - beamtime (actually data collection period)

       - one or more PI
       - zero or more 'users'
       - 1 or more beamtime per proposal
       - exactly one proposal per beamtime

   - where to do authorization at?

     - proposal or beamtime?

   - filter at runstart / header level

     - once you have header object, assume you _should_ have it
     - if get pickled and shipped, maybe re-validate on first access?
     - authorize on each call to header methods / attributes

   - integration with filesystem users / groups?
   - how much to segment data?

     - database per ACL entity?

   - rely on external tools for authentication

3. slicing (by stream / field / event)

   - streaming-by-chunks

4. alternate implementations

   - diverse backends

     - bucket-of-files
       - single point-of-entry for ingest
       - hdf5 / cbf / tiff / ...
     - databases
       - sqlite / mongo / postgres / elastic/ cloud databases?
     - arrow?
   - fully local implementations
5. catalog services
   - related to federated storage
   - related to provenance
   - integration with simulation data
6. user annotations and tags
   - fully mutable
   - fully searchable
   - local or remote
   - shareable or private
7. integration with GUI / web
   - Xicam
   - glueviz
   - databrokerbrowser
   - BEC-as-a-service

8. federated storage systems
   - a given Broker object may have more than one (\*Source)
9. provenance
   - derived-data storage
   - naming schemes
   - related to federated storage
   - there is an on-going LDRD about this at BNL
10. data 'muxing'
    - align multiple streams in one header
    - merge events from multiple headers
    - split events from one stream in one header into multiple streams (?)
    - pivot "event with a time series" to "series of events"
    - stack "series of events" to "event with a time series"
    - resampling
11. pipelines
    - how do they interact with the databases?
    - what goes between the edges?
12. search
    - maintaining rich start search across implementations

      - graphql `<http://graphql.org/>`_
      - mongo `<https://docs.mongodb.com/manual/tutorial/query-documents/>`_
      - postgress `<https://www.postgresql.org/docs/10/static/functions-json.html>`_
      - fuzzy-search?

    - search into stop documents?
    - search into descriptors

      - use of particular hardware
      - configuration of detector

        - "all runs where

    - search in data sets

      - "show me all runs where the theta motor was between [0, 5]"
      - "show me all runs where the sum of the fccd images > 1000"

    - first-class query object?

      - provide & and | operators for building complex queries
      - manage turning user intent into input to different HeaderSource implementations
      - manage serialization of query for re-use later
      - support GUI based search tools

13. name standardization
    - use nexus dictionary

14. alternative returns
    - xarray?
    - numpy array?
    - dask?
    - VTK/ITK primitives?

15. configuration management
    - some progress, but needs to be richer

16. feeding computation services
    - dask
    - SHED
    - paws
    - staging to traditional HPC

17. data export
    - suitcase
    - round-trip with 'common' formats
    - write nexus definition
    - publish to MDF / what ever



Agenda
******
- Day 1

 - current architecture and API (60 minute talk by DAMA)

   - Document types
     - Start
     - Stop
     - Descriptor
     - Event
     - Resource
     - Datum
     - BulkEvent
     - BulkDatum

   - concept of 'stream'

   - Header class

     - holds aggregated meta-data (Start, Stop, Descriptor, Resource)
     - access method to full data set
     - manages filling

   - top-level Broker class

     - search, direct header access, 'most recent' access

   - storage factoring

     - HeaderSource
     - EventSource
     - AssetRegistry

 - high level requirements

 - work planning
   - break into 2-3 person cross-facility teams


- Day 2

 - Philip Cloud visit

   - he presents arrow / pandas 2
   - present to him what we are doing

     - applications of arrow to \*-as-a-service?
     - arrow as a column store?
     - are we using pandas right?

 - Facility tour
 - working in groups


- Day 3/4

 - working in groups

- Day 5

 - working in groups
 - presentation of progress made (1200-1400)
 - wrap-up by 1400-1600
