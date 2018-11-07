from bluesky import RunEngine
from bluesky.plans import scan
from ophyd.sim import det, motor
from bluesky.callbacks.mpl_plotting import LivePlot
RE = RunEngine({})
RE(scan([det], motor, -5, 5, 30),
   LivePlot('det', 'motor', marker='x', markersize=10, color='red'))