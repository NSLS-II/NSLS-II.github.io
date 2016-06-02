Bragg Edge Wavelength Calibration
=================================

1. Scan around the beam center.
2. Detect the first Bragg peak on each side. It will correspond to a dip
   in the transmitted intensity.
3. Locate the theta position of the two peaks and compute the peak-to-peak
   distance.
4. Return the wavelength.



.. code-block:: python

    from bluesky.scientific_callbacks import PeakStats
    from lmfit.models import GaussianModel
    import numpy as np
    

    def verify_wavelength(d_spacing, nominal_energy=30):
        NM_PER_EV = 1.24
        MARGIN = 0.2
        SPACING = 0.2  # degrees

        # Find the beam center by scanning around zero and finding the peak.
        mov(tth_cal, 0)
        ds = DeltaScan([em_ch1], tth_cal, -range, range, 20)
        ps = PeakStats('tth_cal', 'em_ch1')
        ds.subs =  ps
        gs.RE(ds)
        print('Center of beam found to be {0}'.format(ps.cen))
        mov(tth_cal, ps.cen)

        # Scan around the beam center in small increments.
        nominal_λ = NM_PER_EV / nominal_energy
        nominal_θ = np.arcsin(nominal_λ / 2 / d_spacing)
        ds.start = - (1 + MARGIN) * nominal_θ
        ds.stop = (1 + MARGIN) * nominal_θ
        ds.num = 2 * (1 + MARGIN) * nominal_θ / np.deg2rad(SPACING)

        # Fit to two Gaussians.
        last_scan = db[-1]
        data = get_table(last_scan, ['em_ch1'])
        model = GaussianModel(prefix="peak1") + GaussianModel(prefix="peak2")
        result = model.fit(data['em_ch1'])

        # Show the plot so that users are aware if the
        # nonlinear fitting process misses badly.

        # Compute the distance between the two Gaussians' centers.
        two_dθ = result.values['peak1_sigma'] - result.values['peak2_sigma']

        # Compute the wavelength in nanometers and return that value.
        λ = 2 * d_spacing * np.sin(two_dθ / 2)
        return λ
