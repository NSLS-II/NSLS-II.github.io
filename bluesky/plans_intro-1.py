from bluesky import RunEngine
RE = RunEngine({})
from bluesky.plans import scan
from bluesky.examples import motor, det
from bluesky.callbacks import LivePlot
RE(scan([det], motor, 1, 5, 5), LivePlot('det', 'motor'))