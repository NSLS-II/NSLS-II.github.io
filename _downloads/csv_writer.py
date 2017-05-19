# -*- coding: utf-8 -*-
"""
========================================
A Minimal CSV writer for data collection
========================================

Problem
-------

Write (a subset of) the data to a CSV file during data collection.

Approach
--------

Write a callback function that integrates Python's built-in csv module with
bluesky.

Example Solution
----------------

"""


###############################################################################
# Boiler plate imports and configuration


import path
import os
import bluesky as bs
import bluesky.plans as bp
import bluesky.callbacks as bc
import csv
from bluesky.examples import motor, det

import matplotlib.pyplot as plt


# Do this if running the example interactively;
# skip it when building the documentation.
import os
if 'BUILDING_DOCS' not in os.environ:
    from bluesky.utils import install_qt_kicker  # for notebooks, qt -> nb
    install_qt_kicker()
    plt.ion()
    det.exposure_time = .1  # simulate detector exposure time

RE = bs.RunEngine({})


###############################################################################
# Define a callback class which writes out a CSV file


class CSVWriter(bc.CallbackBase):
    def __init__(self, fields, fname_format, fpath):
        self._path = path.Path(fpath)
        os.makedirs(self._path, exist_ok=True)
        self._fname_fomat = fname_format
        self._fields = fields
        self._writer = None
        self._fout = None

    def close(self):
        if self._fout is not None:
            self._fout.close()
        self._fout = None
        self._writer = None

    def start(self, doc):
        self.close()

        fname = self._path / self._fname_fomat.format(**doc)

        self._fout = open(fname, 'xt')
        self._writer = csv.writer(self._fout)

    def descriptor(self, doc):
        if self._writer is not None:
            self._writer.writerow(self._fields)

    def event(self, doc):
        data = doc['data']
        if self._writer is not None:
            self._writer.writerow(data[k] for k in self._fields)

    def stop(self, doc):
        self.close()

###############################################################################
# Set up some callbacks


def create_cbs():
    return [bc.LiveTable([motor, det]), bc.LivePlot('det', 'motor')]

fmt = '{user}_{uid:.6s}.csv'
export_path = '/tmp/export_demo'
csv_writer = CSVWriter(('motor', 'det'), fmt, export_path)

# send all documents to the CSV writer
RE.subscribe('all', csv_writer)

###############################################################################
# run the scan

uid, = RE(bp.scan([det], motor, -5, 5, 11),
          create_cbs(), user='tcaswell')

###############################################################################
# check file


fname = os.path.join(export_path,
                     '{user}_{uid:.6s}.csv'.format(user='tcaswell', uid=uid))

print("--- {} ---".format(fname))
with open(fname, 'r') as fin:
    for ln in fin:
        print(ln.strip())
