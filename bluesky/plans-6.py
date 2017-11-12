from bluesky.simulators import plot_raster_path
from ophyd.sim import motor1, motor2, det
from bluesky.plans import spiral

plan = spiral([det], motor1, motor2, x_start=0.0, y_start=0.0, x_range=1.,
              y_range=1.0, dr=0.1, nth=10)
plot_raster_path(plan, 'motor1', 'motor2', probe_size=.01)