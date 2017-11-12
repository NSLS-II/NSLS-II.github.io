from bluesky import RunEngine
from bluesky.plans import count
from ophyd.sim import noisy_det
from bluesky.callbacks import LivePlot
RE = RunEngine({})
RE(count([noisy_det], num=5), LivePlot('noisy_det'))