from bluesky.plans import list_grid_scan
from ophyd.sim import det4, motor1, motor2
dets = [det4]
RE(list_grid_scan(dets,
                  motor1, [1, 1, 2, 3, 5],
                  motor2, [25, 16, 9]))