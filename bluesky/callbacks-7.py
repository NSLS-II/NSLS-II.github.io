from bluesky import RunEngine
from bluesky.callbacks.scientific import PeakStats, plot_peak_stats
from bluesky.examples import motor, det
from bluesky.plans import scan

RE = RunEngine({})
ps = PeakStats('motor', 'det')
RE(scan([det], motor, -5, 5, 10), ps)
plot_peak_stats(ps)