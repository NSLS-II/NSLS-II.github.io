from bluesky.plan_tools import plot_raster_path
from bluesky.examples import motor1, motor2, det
from bluesky.plans import outer_product_scan
import matplotlib.pyplot as plt

true_plan = outer_product_scan([det], motor1, -5, 5, 10, motor2, -7, 7, 15, True)
false_plan = outer_product_scan([det], motor1, -5, 5, 10, motor2, -7, 7, 15, False)

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
plot_raster_path(true_plan, 'motor1', 'motor2', probe_size=.3, ax=ax1)
plot_raster_path(false_plan, 'motor1', 'motor2', probe_size=.3, ax=ax2)
ax1.set_title('True')
ax2.set_title('False')
ax1.set_xlim(-6, 6)
ax2.set_xlim(-6, 6)