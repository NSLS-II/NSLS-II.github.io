from bluesky import RunEngine
from bluesky.plans import grid_scan
from ophyd.sim import det5, jittery_motor1, jittery_motor2
from bluesky.callbacks.mpl_plotting import LiveScatter
RE = RunEngine({})
RE(grid_scan([det5],
                      jittery_motor1, -3, 3, 6,
                      jittery_motor2, -5, 5, 10, False),
   LiveScatter('jittery_motor1', 'jittery_motor2', 'det5',
            xlim=(-3, 3), ylim=(-5, 5)))