from bluesky.plans import scan
from ophyd.sim import det4, motor1, motor2
dets = [det4]
RE(scan(dets,
        motor1, -1.5, 1.5,  # scan motor1 from -1.5 to 1.5
        motor2, -0.1, 0.1,  # ...while scanning motor2 from -0.1 to 0.1
        11))  # ...both in 11 steps