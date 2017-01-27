from bluesky.plan_tools import plot_raster_path
from bluesky.examples import motor1, motor2, det
from bluesky.plans import inner_product_scan
import matplotlib.pyplot as plt

plan = inner_product_scan([det], 5, motor1, 1, 5, motor2, 10, 50)
plot_raster_path(plan, 'motor1', 'motor2', probe_size=.3)