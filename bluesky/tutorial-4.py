from bluesky.simulators import plot_raster_path
from ophyd.sim import motor1, motor2, det
from bluesky.plans import grid_scan
import matplotlib.pyplot as plt

snaked = grid_scan([det], motor1, -5, 5, 10, motor2, -7, 7, 15, snake_axes=True)
not_snaked = grid_scan([det], motor1, -5, 5, 10, motor2, -7, 7, 15)

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
plot_raster_path(snaked, 'motor1', 'motor2', probe_size=.3, ax=ax1)
plot_raster_path(not_snaked, 'motor1', 'motor2', probe_size=.3, ax=ax2)
ax1.set_title('True')
ax2.set_title('False')
ax1.set_xlim(-6, 6)
ax2.set_xlim(-6, 6)