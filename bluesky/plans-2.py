from bluesky import RunEngine
from bluesky.plans import scan
from ophyd.sim import det, motor
from bluesky.callbacks import LivePlot
RE = RunEngine({})
RE(scan([det], motor, 1, 5, 5), LivePlot('det', 'motor'))