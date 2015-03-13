.. highlight:: bash
***********
Quick Start
***********

#. Log into your beamline user account, e.g., xf23id.
   
#. Activate the ``ophyd``  conda environment.::

    source activate ophyd

   This command makes the collection software available by adding it
   your UNIX ``$PATH``.

#. Start IPython with a profile.::

    ipython --ipython-dir=~/ipython_ophyd --profile=BEAMLINE

   where ``BEAMLINE`` is the full beamline branch name, like ``xf23id1``.

   A "profile" runs code at startup to define useful variables and
   functions, including the names of motors and detectors.

#. Collect data. For example, list all positioners.::

    In [1]: wh_pos()

    -------------------------------------------------------------------------------------
    | Positioner         | Value              | Low Limit          | High Limit         |
    -------------------------------------------------------------------------------------
    | bpm1_y             |  0.7269 mm         |  0.000000 mm       |  0.000000 mm       |
    | bpm2_ydiode        | -9.9956 mm         |  0.000000 mm       |  0.000000 mm       |
    | bpm2_yfoil         | -30.1198 mm        |  0.000000 mm       |  0.000000 mm       |
    | dlm_c1_bnd_bi      |  85000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c1_bnd_bo      |  88000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c1_bnd_ti      |  85000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c1_bnd_to      |  77000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c1_p           |  0.5465 deg        |  0.000000 deg      |  0.000000 deg      |
    | dlm_c1_xi          |  0 counts          |  0.000000 counts   |  90000.000000 counts |
    | dlm_c1_xo          | -1 counts          |  0.000000 counts   |  0.000000 counts   |
    ...
    -------------------------------------------------------------------------------------


#. In a separate terminal, you can open Replay, a graphical user interface.::

    source activate ophyd
    replay


   Notice that this is not a Python command; it should be typed directly into
   the shell, not into IPython.

   To view the latest scan, automatically updating live as new data is collected,
   use::

    replay --live
