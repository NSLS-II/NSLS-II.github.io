from bluesky import RunEngine
from bluesky.plans import adaptive_scan
from bluesky.callbacks import LivePlot
from bluesky.examples import motor, det

RE = RunEngine({})

RE(adaptive_scan([det], 'det', motor,
                 start=-15,
                 stop=10,
                 min_step=0.01,
                 max_step=5,
                 target_delta=.05,
                 backstep=True),
   LivePlot('det', 'motor', markersize=10, marker='o'))