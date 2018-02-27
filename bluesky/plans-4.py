from bluesky.simulators import plot_raster_path
from ophyd.sim import motor1, motor2, det
from bluesky.plans import spiral_fermat

plan = spiral_fermat([det], motor1, motor2, x_start=0.0, y_start=0.0,
                     x_range=2.0, y_range=2.0, dr=0.1, factor=2.0, tilt=0.0)
plot_raster_path(plan, 'motor1', 'motor2', probe_size=.01, lw=0.1)