==================================
Data collection request priorities
==================================

The priorities attached to data collection requests are important for knowing which collections should be visible in the GUI, their order, and which exact collection is currently active.
 * 99999 - currently active
 * 0 - used by strategy protocols (characterize and ednaCol) for creating the second collection
 * 6000 - default priority of multiCol request
 * 5000 - default priority of several types of requests - raster, escan, std using centering marks, interactive or automated centering
 * -1 - completed request

The LSDC GUI tree views use priorities to color the collections. The following list shows the key for colors.
 * 99999 - green
 * > 0 (and not 999999) - white
 * < 0  - cyan

How changing priority works when using the interactive move up/down and to top/bottom buttons in the LSDC GUI.
 * use the average priority of the next two entries above - if clashes with the next one above, increase priority by 20
 * use the average priority of the next two entries below - if clashes with the next one below, decrease priority by 20
 * to move to the top, find the highest priority and add 100
 * to move to the bottom, find the lowest priority and decrease by 100

