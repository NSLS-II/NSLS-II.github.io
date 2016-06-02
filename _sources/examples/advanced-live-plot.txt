Advanced LivePlot
-----------------

``LivePlot`` plots scalar data. It is meant to be used with bluesky
subscriptions; it takes in a stream of Documents, extracts the relevant data,
and updates a matplotlib plot.

Usage with Object-Oriented Scans
================================

.. ipython:: python

    my_scan = AbsScan([det], motor, 0, 5, 5)
    my_scan.subs = LivePlot('det')  # plots det vs. sequence number
    gs.RE(my_scan)

.. ipython:: python

    my_scan.subs = LivePlot('det', 'motor')  # plots det vs. motor
    gs.RE(my_scan)

Customizing Plot Style
======================

The plotting style is fully customizable, like so:

.. ipython:: python

    my_scan.subs = LivePlot('det', 'motor', color='red', marker='x',
                            linestyle='--')

Any extra arguments to ``LivePlot`` will be passed through to matplotlib's
``plot`` method. Thus, any arguments accepted by ``plot`` are allowed;
``LivePlot`` does not interfere with the style.

Usage with "SPEC-like" simple scans
===================================

The SPEC-style simple scans automatically set up a ``LivePlot`` instance
with minimal input from the user. They use ``motor`` for the x variable. It is
harder to guess the y variable --- they can be many detectors, after all ---
so for that a special setting in the global state is used, ``gs.PLOT_Y``.

To customize the style, we have to take over the process by which the
``LivePlot`` instances are set up. The simple scans have "subscription
factories," functions that take in an instance of a scan, inspect things
like which motor is being used, and use that information to return a 
subscription.

By default, ``ascan`` has two subscription factories, one for ``LivePlot``
and one for ``LivePlot``.

.. ipython:: python

    ascan.sub_factories

We'll define a custom "factory" function. This is similar to the existing one,
but it adds custom style.

.. ipython:: python

    from bluesky.global_state import gs
    def custom_plot(scan):
        return LivePlot(scan.motor, gs.PLOT_Y, linestyle='--')

We'll remove the existing factory function and add our custom one.

.. ipython:: python

    from bluesky.simple_scans import plot_from_motor
    ascan.sub_facotires['all'].remove(plot_from_motor)
    ascan.sub_factories['all'].append(custom_plot)
