Export images as TIFF files
***************************

Problem
=======

Export a series of images as sequentally-numbered TIFF files. Include metadata
in the filenames.

Approach
========

Write a filepath template. Create an *exporter*, and feed it data from the
databroker.

Example Solution
================

Configuration
-------------

This part only need be set up once. It can be including the IPython profile
for future reuse, if applicable.

Define a "template string," a file path that includes pieces in curly brackets
that will be filled in with metadata. Example:

.. code-block:: python

    template = "path/to/directory/{start.scan_id}_step{event.seq_num}.tif"

(For more available fields, read up on :doc:`header-contents`.)

Next, you will need to know the field with which the image data is labeled.
(See :doc:`retrieving-data`.) Common choices are 'image' or
'detector_name_image'.

.. code-block:: python

    from bluesky.broker_callbacks import LiveTiffExporter

    exporter = LiveTiffExporter('image_field_name', template)

Finally, import the databroker if it is not already imported.

.. code-block:: python

    from databroker import db

Execution
---------

To export after a scan has finished, use this method:

.. code-block:: python

    uids = RE(your_scan_here)
    db.process(db[uids], exporter)

To perform export live during a scan, add ``exporter`` as a subscription.

.. code-block:: python

    RE(your_scan_here, exporter)

Export can also be done much later. Obtain the header(s) for the runs of
interest (see :doc:`/examples/retrieving-data`) and export like so:

.. code-block:: python

    db.process(headers, exporter)

Extra Credit: Processing Before Export
--------------------------------------

This subclass of ``LiveTiffExporter`` subtracts a "dark frame" from each image
before saving it.

.. code-block:: python

    class SubtractedTiffExporter(LiveTiffExporter):
        """
        Intercept images before saving and subtract dark image

        Runs are expected include a custom metadata field, 'dark_frame',
        pointing to the unique ID of a run that captured a dark frame to be
        used for subtraction.

        def start(self, doc):
            "Load the dark frame we will use for this run."

            # The metadata is expected to contain a reference to the uid
            # of a run with a dark frame image.
            if 'dark_frame' not in doc:
                raise ValueError("No dark_frame was recorded.")
            uid = doc['dark_frame']
            dark_header = db[uid]
            self.dark_img, = get_images(db[uid], 'pe1_image')
            super().start(doc)

        def event(self, doc):
            "For each image, subtract the dark frame."

            img = doc['data'][self.field]
            subtracted_img = img - self.dark_img
            doc['data'][self.field] = subtracted_img
            super().event(doc)


Usage example:

.. code-block:: python

    from bluesky.plans import count, relative_list_scan
    import time

    template = "/home/xf28id1/xpdUser/tiff_base/UO2_23_8/{start.sa_name}_{start.scan_id}_step{event.seq_num}.tif"
    exporter = SubtractedTiffExporter('pe1_image', template)

    def take_dark():
        print('closing shutter...')
        shctl1.put(0)  # close shutter
        sleep(2)
        print('taking dark frame....')
        uid, = RE(count([pe1c]))
        print('opening shutter...')
        shctl1.put(1)
        sleep(2)
        return uid


    def run(motor, x, start, stop, num_steps, loops, *, exposure=1,  **metadata):
        print('moving %s to initial position' % motor.name)
        subs = [LiveTable(['pe1_stats1_total', motor.name]),
                LivePlot('pe1_stats1_total', motor.name)]
        motor.move(x)
        pe1c.images_per_set.put(exposure // 0.1)
        dark_uid = take_dark()
        steps = loops * list(np.linspace(start, stop, num=num_steps, endpoint=True))
        plan = relative_list_scan([pe1c], motor, steps)
        uid = RE(plan, subs, dark_frame=dark_uid, **metadata)
        time.sleep(3)  # wait to ensure all images are available
        process(db[uid], exporter)
