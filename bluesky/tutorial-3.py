from bluesky.plans import list_scan
from ophyd.sim import det4, motor1, motor2
dets = [det4]
RE(list_scan(dets,
             motor1, [1, 1, 3, 5, 8],
             motor2, [25, 16, 9, 4, 1]))