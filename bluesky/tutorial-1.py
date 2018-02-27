from bluesky.plans import scan
from ophyd.sim import det, motor
dets = [det]
RE(scan(dets, motor, -1, 1, 10))