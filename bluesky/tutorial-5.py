from bluesky.plans import grid_scan
from ophyd.sim import motor1, motor2, det4
dets = [det4]
RE(grid_scan(dets,
             motor1, -1.5, 1.5, 3,  # scan motor1 from -1.5 to 1.5 in 3 steps
             motor2, -0.1, 0.1, 5))  # scan motor2 from -0.1 to 0.1 in 5 steps