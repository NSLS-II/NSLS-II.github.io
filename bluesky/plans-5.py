from bluesky.simulators import plot_raster_path
from ophyd.sim import motor1, motor2, det
from bluesky.plans import spiral_square

plan = spiral_square([det], motor1, motor2, x_center=0.0, y_center=0.0,
                     x_range=1.0, y_range=1.0, x_num=11, y_num=11)
plot_raster_path(plan, 'motor1', 'motor2', probe_size=.01)