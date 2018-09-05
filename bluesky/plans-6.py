from bluesky import RunEngine
from bluesky.plans import adaptive_scan
from bluesky.callbacks.best_effort import BestEffortCallback
bec = BestEffortCallback()
from ophyd.sim import motor, det

RE = RunEngine({})
RE.subscribe(bec)

RE(adaptive_scan([det], 'det', motor,
                 start=-15.5,
                 stop=10,
                 min_step=0.01,
                 max_step=5,
                 target_delta=.05,
                 backstep=True))