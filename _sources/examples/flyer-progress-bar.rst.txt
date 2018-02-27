Add a progress bar to a fly scan
********************************

Problem
-------

At the end of a run involving a "flyer" (a fly-scanning device), all the
data from the flyer has to be retrieved from the device and processed. This
can be take a significant amount of time, giving no indication of whether the
process has crashed or is merely working slowly.

Approach
--------

For progress bars in general, we recommend a Python pacakge named
`tqdm <https://github.com/tqdm/tqdm#tqdm>`_ (read "taqadum" or تقدّم, which
means "progress" in Arabic). It is remarkably simple and flexible, and adds
minimal overhead. Follow the link to tqdm for nice demo of tqdm in action.

A "flyer" is implemented as a Python class with a method named ``collect``
that yields all of the data produced by the flyer. By wrapping the output
of collect in ``tqdm``, we create a progress bar that is updated each time
``collect`` yields a new data point.

Example Solution
----------------

Configuration
=============

If tqdm is not already installed, install it with pip.

.. code-block:: bash

    pip install tqdm

Suppose the flyer in question is called ``flyer``, an instance of the class
``Flyer``. Find where ``flyer`` is defined in your IPython profile. Something
like:

.. code-block:: python

    flyer = Flyer(some_arguments)

We can subclass ``Flyer``, customizing its ``collect`` method to incorporate a
progress bar.

.. code-block:: python

    class FlyerWithProgressBar(Flyer):
    
        def collect(self):
            yield from tqdm(super().collect())

    flyer = FlyerWithProgressBar(some_arguments)


If you have some way of knowing in advance how many data points will be
yielded by ``collect``, you can provide that information to ``tqdm`` to make
it more informative. (It can predict the time remaining, for example.)
Suppose we have a flyer that always produces 100 data points. The class
should be defined like:

.. code-block:: python
 
    class FlyerWithProgressBar(Flyer):
    
        def collect(self):
            yield from tqdm(super().collect(), total=100)

Or, add an attribute that can be updated interactively:

.. code-block:: python
 
    class FlyerWithProgressBar(Flyer):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)  # pass arguments to Flyer
            self.total = 100
    
        def collect(self):
            yield from tqdm(super().collect(), total=self.total)

Here is a demo of ``FlyerWithProgressBar``.

.. ipython:: python
    :suppress:

    import time
    from tqdm import tqdm
    from bluesky.examples import NullStatus, Flyer
    from bluesky import RunEngine
    RE = RunEngine({})

    class SlowFlyer(Flyer):
        "add a short sleep to collect()"
        def collect(self):
            for ev in super().collect():
                time.sleep(0.01)
                yield ev

    class FlyerWithProgressBar(SlowFlyer):
        def collect(self):
            yield from tqdm(super().collect(), total=100, leave=True)

    # this code was used to generate the output below, but tqdm does not
    # show up in sphinx, so the :verbatim: directive is used

.. ipython::
    :verbatim:

    In [1]: from bluesky.plans import fly

    In [2]: flyer = FlyerWithProgressBar()

    In [3]: plan = fly([flyer])

    In [4]: RE(plan)
    100%|█████████████████████████████████████████████████| 100/100 [00:01<00:00, 92.35it/s]
    Out[4]: ['3acf0eb7-96bf-4c09-b813-e715dabc7060']
