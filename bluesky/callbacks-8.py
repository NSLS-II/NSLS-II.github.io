from bluesky import RunEngine
from bluesky.plans import scan
from ophyd.sim import det, motor
from bluesky.callbacks.best_effort import BestEffortCallback
RE = RunEngine({})
bec = BestEffortCallback()
RE.subscribe(bec)
RE(scan([det], motor, 1, 5, 5))