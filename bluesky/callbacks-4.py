from bluesky import RunEngine
from bluesky.plans import outer_product_scan
from bluesky.examples import det5, jittery_motor1, jittery_motor2
from bluesky.callbacks import LiveMesh
RE = RunEngine({})
RE(outer_product_scan([det5],
                      jittery_motor1, -3, 3, 6,
                      jittery_motor2, -5, 5, 10, False),
   LiveMesh('jittery_motor1', 'jittery_motor2', 'det5',
            xlim=(-3, 3), ylim=(-5, 5)))