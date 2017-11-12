.. highlight:: bash
***************************
Data Collection Quick Start
***************************

.. note::

   Here we are assume that you are sitting at a beamline computer that has
   the software installed and configured. If you are starting from scratch
   and you have administrative access to your machine, see
   :ref:`deployment-details` -- or contact the DAMA group.

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
`bluesky documentation <https://nsls-ii.github.io/bluesky>`_
to learn how to run experiments.
