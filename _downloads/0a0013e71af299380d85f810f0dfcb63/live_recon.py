"""
Streaming Tomographic Reconstruction
************************************

Problem
-------

Reconstruct a 2D cross-section of a sample from projections, as if it were
rotated in place in front of a strip detector.

This example uses the library `tomopy <https://tomopy.readthedocs.io>`_.

Approach
--------

Create a simulated detector coupled to a simulated motor, standing in for the
strip detector and the rotating sample holder. Scan the motor from zero to pi,
and use tomopy to generate simulated projections of a sample at several angles.
This provides our simulated dataset.

Now, use tomopy to reconstruct the sample "density" from these projections.
To give tomopy live access to the data, wrap it in a class that acts as a
bluesky callback, an interface between tomopy and bluesky's document model.

Also make a callback for visualizing the projections side by side (a sinogram).

Example Solution
----------------
"""
import glob
import imageio
import matplotlib.pyplot as plt
import numpy as np

import tomopy

import bluesky.plans as bp
from bluesky import RunEngine
from bluesky.callbacks import LiveTable, CallbackBase
from bluesky.utils import install_qt_kicker
from ophyd import Device, Signal, Component as Cpt
from ophyd.sim import SynAxis, NullStatus

L = 64
obj = tomopy.cameraman(L)
# obj = tomopy.checkerboard(L)
# obj = tomopy.baboon(L)
# obj = tomopy.lena(L)

class TomoDet(Device):
    image = Cpt(Signal)
    def trigger(self):
        super().trigger()
        self.image.put(tomopy.project(obj, angle.read()['angle']['value']))
        return NullStatus()

det = TomoDet(name='det')
angle = SynAxis(name='angle')

RE = RunEngine({})

# Do this if running the example interactively;
# skip it when building the documentation.
import os
if 'BUILDING_DOCS' not in os.environ:
    from bluesky.utils import install_qt_kicker  # for notebooks, qt -> nb
    install_qt_kicker()
    plt.ion()
    angle._fake_sleep = 0.001  # simulate slow motor movement


class LiveRecon(CallbackBase):
    SMALL = 1e-6

    def __init__(self, name, x, y, ax=None, **recon_kwargs):
        if ax is None:
            ax = plt.gca()
        ax.set_title('Reconstruction using Tomopy')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        self.im = ax.imshow(np.zeros((y, x)), origin='upper')
        recon_kwargs.setdefault('num_gridx', x)
        recon_kwargs.setdefault('num_gridy', y)
        self._name = name
        self._x, self._y = x, y
        self._recon_kwargs = recon_kwargs

    def start(self, doc):
        self._partial = self.SMALL * np.ones((self._y, self._x))

    def event(self, doc):
        data = doc['data'][self._name]
        angle = doc['data']['angle']
        self._partial = tomopy.recon(data, angle, **self._recon_kwargs,
                                     init_recon=self._partial)
        self.im.set_data(self._partial)
        self.im.set_clim((np.min(self._partial), np.max(self._partial)))
        self.im.figure.canvas.draw_idle()

class LiveSinogram(CallbackBase):
    def __init__(self, name, width, ax=None):
        if ax is None:
            ax = plt.gca()
        ax.set_title('Sinogram')
        ax.set_xlabel('sequence number')
        ax.set_ylabel('detector position')
        self.im = ax.imshow(np.zeros((1, width)), aspect='auto')
        ax.figure.colorbar(self.im, ax=ax)
        self._name = name
        self._width = width

    def start(self, doc):
        self._cache = []

    def event(self, doc):
        self._cache.append(doc['data'][self._name][0][0])
        arr = np.asarray(self._cache)
        self.im.set_data(arr.T)
        self.im.set_extent((0, len(self._cache), 0, self._width))
        self.im.set_clim((arr.min(), arr.max()))
        self.im.figure.canvas.draw_idle()


class LiveSaving(CallbackBase):
    def __init__(self, fig=None):
        self._fig = fig

    def event(self, doc):
        angle = doc['data']['angle']
        if self._fig:
            self._fig.savefig(f'recon_{angle:3.3f}.png')


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

lt = LiveTable([angle])
ls = LiveSinogram(f'{det.name}_image', 94, ax=ax1)
lr = LiveRecon(f'{det.name}_image', L, L, algorithm='art', ax=ax2)
lsv = LiveSaving(fig=fig)

RE(bp.scan([det], angle, 0, np.pi, 100), [lt, ls, lr, lsv])

with imageio.get_writer('recon.gif', mode='I') as writer:
    for fn in sorted(glob.glob('recon_*.png')):
        image = imageio.imread(fn)
        writer.append_data(image)
