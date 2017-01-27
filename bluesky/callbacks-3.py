from bluesky import RunEngine
from bluesky.plans import outer_product_scan
from bluesky.examples import det4, motor1, motor2
from bluesky.callbacks import LiveRaster
motor1._fake_sleep = 0
motor2._fake_sleep = 0
RE = RunEngine({})
RE(outer_product_scan([det4], motor1, -3, 3, 6, motor2, -5, 5, 10, False),
   LiveRaster((6, 10), 'det4'))