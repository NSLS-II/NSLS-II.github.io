.. highlight:: bash
***************************
Data Collection Quick Start
***************************

.. note::

   Here we are assume that you are sitting at a beamline computer that has
   the software installed and configured. If you are starting from scratch
   and you have administative access to your machine, see
   `this script <https://gist.github.com/danielballan/c02c17f92650e21488a3>`_.

#. You should be logged in as a "beamline user" (e.g., ``xf23id1``). Open a
   terminal.
   
#. Activate the ``collection`` conda environment.::

    source activate collection

   This command makes the data collection software available by adding it
   your UNIX ``$PATH``.

#. Start IPython with a profile.::

    ipython --profile=collection

   A "profile" runs code at startup to define useful variables and
   functions, including the names of motors and detectors.

You are ready to work. See the
`bluesky documentaion <https://nsls-ii.github.io/bluesky>`_
to learn how to run experiments.
