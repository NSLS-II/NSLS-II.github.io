import numpy as np
import lmfit
from bluesky.plans import scan
from ophyd.sim import motor, noisy_det
from bluesky.callbacks import LiveFit
from bluesky.callbacks.mpl_plotting import LivePlot, LiveFitPlot
from bluesky import RunEngine

RE = RunEngine({})

def gaussian(x, A, sigma, x0):
    return A*np.exp(-(x - x0)**2/(2 * sigma**2))

model = lmfit.Model(gaussian)
init_guess = {'A': 2,
              'sigma': lmfit.Parameter('sigma', 3, min=0),
              'x0': -0.2}

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
lf = LiveFit(model, 'noisy_det', {'x': 'motor'}, init_guess)
lfp = LiveFitPlot(lf, ax=ax, color='r')
lp = LivePlot('noisy_det', 'motor', ax=ax, marker='o', linestyle='none')

RE(scan([noisy_det], motor, -1, 1, 50), [lfp, lp])
plt.draw()