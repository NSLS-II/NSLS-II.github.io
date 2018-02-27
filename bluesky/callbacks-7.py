from bluesky import RunEngine
from bluesky.callbacks.fitting import PeakStats
from bluesky.callbacks.mpl_plotting import plot_peak_stats
from ophyd.sim import motor, det
from bluesky.plans import scan

RE = RunEngine({})
ps = PeakStats('motor', 'det')
RE(scan([det], motor, -5, 5, 10), ps)
plot_peak_stats(ps)