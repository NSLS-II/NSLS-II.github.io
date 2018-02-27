from bluesky import RunEngine
from bluesky.plans import count
from ophyd.sim import noisy_det
from bluesky.callbacks.best_effort import BestEffortCallback
bec = BestEffortCallback()
RE = RunEngine({})
RE.subscribe(bec)
RE(count([noisy_det], num=5))