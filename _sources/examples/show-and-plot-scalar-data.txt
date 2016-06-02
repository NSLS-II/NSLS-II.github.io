Show and Plot Scalar Data
-------------------------

.. ipython:: python
    :suppress:

    import matplotlib.pyplot as plt
    from bluesky.examples import motor, det
    from bluesky.spec_api import dscan
    from bluesky.standard_config import *
    from bluesky.global_state import gs
    # from bluesky.run_engine import RunEngine
    # RE = RunEngine({})
    # gs.RE = RE
    from databroker import DataBroker as db, get_table
    gs.RE.md['owner'] = 'docs'
    gs.RE.md['group'] = 'docs'
    gs.RE.md['beamline_id'] = 'docs'
    gs.DETS = [det]

We'll generate some sample data with a basic scan using the SPEC-style
interface.

.. ipython:: python

    dscan(motor, -1, 1, 5)

Now we'll look up the most recent scan. This returns a "header" containing
metadata but no data.

.. ipython:: python

    header = db[-1]

We can get the data as a table.

.. ipython:: python

    table = get_table(header)
    table

We can plot one field against another.

.. ipython:: python

    plt.plot('det', 'motor', data=table)

Or simply plot one field against sequence number.

.. ipython:: python

    plt.plot('det', data=table)

To extract a column of data.

.. ipython:: python

    det_data = table['det']
    det_data

Now we can use normal mathematical or statistical operations from the numpy
and pandas packages. For example, sum the column.

.. ipython:: python

    det_data.sum()
    np.sum(det_data)  # equivalent

``det_deta`` is a pandas Series, which behaves very much like a numpy array.
To make it explicitly a numpy array, simply call ``np.array(det_data)``. The
``table`` object is a pandas DataFrame, which you can loosely think of as a
dictionary of numpy arrays. Both DataFrame and Series support many useful
analytical and I/O operations. For example, this exports the table as CSV.

.. ipython:: python

    table.to_csv('my_data.csv')

See pandas documentation for more.
