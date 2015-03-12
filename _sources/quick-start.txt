***********
Quick Start
***********

1. Log into your beamline user account, e.g., xf23id.
   
2. Activate the ``ophyd``  conda environment.

.. bash::

   source activate ophyd

This command makes the collection software available by adding it
your UNIX ``$PATH``.

3. Start IPython with a profile.

.. bash::

   ipython --ipython_dir=~/ipython_ophyd --profile=BEAMLINE

where ``BEAMLINE`` is the full beamline branch name, like ``xf23id1``.

A "profile" runs code at startup to define useful variables and
functions, including the names of motors and detectors.

Finally, collect data. For example, list on positioners.::

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
    | dlm_c2_bnd_bi      |  85000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c2_bnd_bo      |  85000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c2_bnd_ti      |  85000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c2_bnd_to      |  84500 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c2_p           | -2.4220 deg        |  0.000000 deg      |  0.000000 deg      |
    | dlm_c2_r           | -2.310 deg         |  0.000000 deg      |  0.000000 deg      |
    | dlm_c2_xi          | -80003 counts      | -85000.000000 counts |  0.000000 counts   |
    | dlm_c2_xo          | -79999 counts      | -85000.000000 counts |  0.000000 counts   |
    | dlm_c2_z           |  240.5002 mm       |  0.000000 mm       |  0.000000 mm       |
    | fltr1_y            |  48.50 mm          |  0.000000 mm       |  0.000000 mm       |
    | fltr6_y            |  0.2063 mm         |  0.000000 mm       |  0.000000 mm       |
    | fs2_y              | -64.3000 mm        |  0.000000 mm       |  0.000000 mm       |
    | fs3_y              | -20.5000 mm        |  0.000000 mm       |  0.000000 mm       |
    | slt_h_i            | -10.0000 mm        |  0.000000 mm       |  0.000000 mm       |
    | slt_h_o            | -10.0000 mm        |  0.000000 mm       |  0.000000 mm       |
    | slt_h_xc           | -12499 None        |  0.000000 None     |  0.000000 None     |
    | slt_h_xg           |  74999 None        |  0.000000 None     |  0.000000 None     |
    | slt_mb1_b          |  1.5503 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb1_i          |  4.9999 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb1_o          |  2.5000 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb1_t          | -0.0502 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb1_xc         | -1.2499 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb1_xg         |  7.4999 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb1_yc         | -0.8002 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb1_yg         |  1.5001 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb2_b          | -2.2000 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb2_i          | -10.2670 mm        |  0.000000 mm       |  0.000000 mm       |
    | slt_mb2_o          | -9.8165 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb2_t          | -3.0000 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb2_xc         | -10.0415 mm        |  0.000000 mm       |  0.000000 mm       |
    | slt_mb2_xg         |  0.4505 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb2_yc         | -2.6000 mm         |  0.000000 mm       |  0.000000 mm       |
    | slt_mb2_yg         | -0.8000 mm         |  0.000000 mm       |  0.000000 mm       |
    | tth                |  5030000.0000 deg  |  0.000000 deg      |  0.000000 deg      |
    | vfm_bnd            | -131010000 None    |  0.000000 None     |  0.000000 None     |
    | vfm_bnd_d          |  720000 cts        |  670000.000000 cts |  670000.000000 cts |
    | vfm_bnd_ofst       |  727920000 None    |  0.000000 None     |  0.000000 None     |
    | vfm_bnd_u          |  660000 cts        |  700000.000000 cts |  700000.000000 cts |
    | vfm_p              |  1.379 mrad        |  0.000000 mrad     |  0.000000 mrad     |
    | vfm_r              | -25.997 mrad       |  0.000000 mrad     |  0.000000 mrad     |
    | vfm_y              | -0.4002 mm         |  0.000000 mm       |  0.000000 mm       |
    | vfm_yd             |  0.7166 mm         |  0.000000 mm       |  0.000000 mm       |
    | vfm_yui            |  2.3295 mm         |  0.000000 mm       |  0.000000 mm       |
    | vfm_yuo            | -4.9497 mm         |  0.000000 mm       |  0.000000 mm       |
    -------------------------------------------------------------------------------------

