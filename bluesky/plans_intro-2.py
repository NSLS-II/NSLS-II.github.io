from bluesky.simulators import plot_raster_path
from ophyd.sim import motor1, motor2, det
from bluesky.plans import grid_scan
import matplotlib.pyplot as plt

plan = grid_scan([det], motor1, -5, 5, 10, motor2, -7, 7, 15, True)
plot_raster_path(plan, 'motor1', 'motor2', probe_size=.3)