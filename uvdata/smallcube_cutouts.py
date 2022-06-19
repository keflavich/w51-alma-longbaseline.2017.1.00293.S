from spectral_cube import SpectralCube
import glob
from astropy import constants, convolution, units as u, table, stats, coordinates, wcs, log; from astropy.table import Table; from astropy.io import fits, ascii; import regions; import radio_beam; import astropy
import pylab as pl

pkdata = {}

for fn in glob.glob("*.image.pbcor.fits"):
    cube = SpectralCube.read(fn)
    cube = cube.mask_out_bad_beams(0.05)
    cube.beam_threshold = 0.1
    mscube = cube - cube.median(axis=0)
    mscube.write(fn.replace(".image.pbcor.fits",".image.pbcor.medsub.fits"), overwrite=True)

    mx = mscube.max(axis=(1,2))
    mx.write(fn.replace("image.pbcor.fits","medsub.max.spectrum.fits"), overwrite=True)

    pl.clf()
    mx.quicklook(fn.replace("image.pbcor.fits","medsub.max.spectrum.png"))

    mxx = mscube.max()
    pkdata[fn] = mxx.value

import json
with open('peaks.json', 'w') as fh:
    json.dump(pkdata, fh)
