from bluesky import RunEngine
from bluesky.plans import grid_scan
from ophyd.sim import det4, motor1, motor2
from bluesky.callbacks.mpl_plotting import LiveGrid
motor1.delay = 0
motor2.delay = 0
RE = RunEngine({})
RE(grid_scan([det4], motor1, -3, 3, 6, motor2, -5, 5, 10, False),
   LiveGrid((6, 10), 'det4'))