from bluesky import RunEngine
from bluesky.plans import scan
from ophyd.sim import det, motor
RE = RunEngine({})
from bluesky.callbacks.best_effort import BestEffortCallback
bec = BestEffortCallback()
RE.subscribe(bec)
RE(scan([det], motor, 1, 5, 5))