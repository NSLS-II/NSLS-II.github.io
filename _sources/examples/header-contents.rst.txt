How metadata is organized: understand the contents of the header
****************************************************************

Problem
=======

The databroker provides the metadata in a dictionary of names and values that
we call the *header*. Its organized but rather sprawling contents can be
difficult to navigate.

Approach
========

Here, we explain the overall structure, and we highlight some commonly useful
contents and where to find them.

Structure
---------

A given header ``h`` has three main pieces:

* the 'start' document, ``h['start']``, contains most of the interesting
  metadata --- everything we know before the run starts. (What kind of scan
  are we doing? Why? Who? When?)
* the 'stop' document, ``h['stop']``, contains what we only know when
  the scan is complete --- mainly, did it terminate successfully?
* a list of 'descriptor' documents in ``h['descriptors']`` which serve
  a sort of table of contents, giving metadata about each field
  about each data field in the corresponding event
  document (PV, data type, precision, units) and its configuration (e.g.,
  exposure time).

Common Metadata
---------------

As we said above, most of the useful stuff is found in the 'start' document.
For brevity, let's set ``s = h['start']``.

* Many plans record a human-friendly list of the names of detectors and motors
  in ``s['detectors']`` and ``s['motors']``.
* The start time is always recorded in ``s['time']``.
* The randomly-generated unique ID in ``s['uid']`` is guaranteed to be a
  permanent identifier for the data forever.
* The strings in ``s['plan_name']`` and ``s['plan_type']`` provide a
  human-friendly description of the plan like 'count' or 'relative scan'.
  (These are generated autmoatically by the bluesky RunEngine, which inspects
  the plan at runtime. Depending on how the plan is implemented, one might
  be more informative than the other.)
* Many plans report the arguments they were passed when they we created, in
  ``s['plan_args']``. This is usually a lot of information, but it can be used
  to precisely reconstruct was what done.

In the 'stop' document, we can learn how the run exited.
``h['stop']['exit_status']`` is set to 'success', 'error', or 'abort'.
