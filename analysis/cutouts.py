from spectral_cube import SpectralCube
from astropy import constants, convolution, units as u, table, stats, coordinates, wcs, log; from astropy.table import Table; from astropy.io import fits, ascii; import regions; import radio_beam; import astropy
from spectral_cube import SpectralCube
from source_ids import sources


cube = SpectralCube.read('W51w51n_only.B3.robust0.5.spw2.clarkclean10000.image.pbcor.medsub.fits')
cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=97.980953*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).write('W51n_CS2-1_cutout.fits')

cube = SpectralCube.read('W51w51e2se_only.B3.robust0.5.spw2.clarkclean10000.image.pbcor.medsub.fits')
cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=97.980953*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).write('W51e2se_CS2-1_cutout.fits')

cube = SpectralCube.read('W51w51e2nw_only.B3.robust0.5.spw2.clarkclean10000.image.pbcor.medsub.fits')
cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=97.980953*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).write('W51e2nw_CS2-1_cutout.fits')

cube = SpectralCube.read('W51w51d2_only.B3.robust0.5.spw2.clarkclean10000.image.pbcor.medsub.fits')
cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=97.980953*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).write('W51d_CS2-1_cutout.fits')

for sourcename in sources:
    cube = SpectralCube.read(f'W51{sourcename}_only.B3.robust0.5.spw2.clarkclean10000.image.pbcor.medsub.fits')
    cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=97.980953*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).write(f'{sourcename}_CS2-1_cutout.fits')

for sourcename in sources:
    cube = SpectralCube.read(f'W51{sourcename}_only.B3.robust0.5.spw2.clarkclean10000.image.pbcor.medsub.fits')
    print(f"{sourcename}: {cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=97.980953*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).max()}")

for sourcename in sources:
    cube = SpectralCube.read(f'W51{sourcename}_only.B3.robust0.5.spw2.clarkclean10000.image.pbcor.medsub.fits')
    print(f"{sourcename}: {cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=97.980953*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).max()}")

########################################################
# Started Logging At: 2019-05-07 18:28:57
########################################################

########################################################
# # Started Logging At: 2019-05-07 18:28:58
########################################################
get_ipython().run_line_magic('edit', 'smallcube_cutouts.py')
########################################################
# Started Logging At: 2019-05-07 18:30:34
########################################################

########################################################
# # Started Logging At: 2019-05-07 18:30:34
########################################################
cube = SpectralCube.read('W51w51d2_only.B3.robust0.5.spw0.clarkclean10000.image.pbcor.medsub.fits')
from astropy import constants, convolution, units as u, table, stats, coordinates, wcs, log; from astropy.table import Table; from astropy.io import fits, ascii; import regions; import radio_beam; import astropy
from spectral_cube import SpectralCube
cube = SpectralCube.read('W51w51d2_only.B3.robust0.5.spw0.clarkclean10000.image.pbcor.medsub.fits')
cube.find_lines(chemical_name=' SiO')
get_ipython().run_line_magic('r', '')
get_ipython().run_line_magic('run', 'source_ids.py')
for sourcename in sources:
    cube = SpectralCube.read(f'W51{sourcename}_only.B3.robust0.5.spw0.clarkclean10000.image.pbcor.medsub.fits')
    cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=85.640452*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).write(f'{sourcename}_SiOv=2J=2-1_cutout.fits')

########################################################
# Started Logging At: 2019-05-07 18:31:51
########################################################

########################################################
# # Started Logging At: 2019-05-07 18:31:51
########################################################
import matplotlib
matplotlib.use('agg')
get_ipython().run_line_magic('run', 'smallcube_cutouts.py')
########################################################
# Started Logging At: 2019-05-07 18:34:11
########################################################

########################################################
# # Started Logging At: 2019-05-07 18:34:11
########################################################
from astroquery.splatalogue import Splatalogue, utils
from astropy import constants, convolution, units as u, table, stats, coordinates, wcs, log; from astropy.table import Table; from astropy.io import fits, ascii; import regions; import radio_beam; import astropy
utils.minimize_table(Splatalogue.query_lines(85.550*u.GHz, 85.575*u.GHz, chemical_name='SiO'))
(Splatalogue.query_lines(85.550*u.GHz, 85.575*u.GHz, chemical_name='SiO'))
(Splatalogue.query_lines(85.550*(1+55/3e5)*u.GHz, 85.575*(1+55/3e5)*u.GHz, chemical_name='SiO'))
(Splatalogue.query_lines(85.550*(1+55/3e5)*u.GHz, 85.575*(1+55/3e5)*u.GHz))
(Splatalogue.query_lines(85.550*(1+55/3e5)*u.GHz, 85.575*(1+55/3e5)*u.GHz)).pprint(max_lines=1000)
cube = SpectralCube.read('W51w51d2_only.B3.robust0.5.spw0.clarkclean10000.image.pbcor.medsub.fits')
from astropy import constants, convolution, units as u, table, stats, coordinates, wcs, log; from astropy.table import Table; from astropy.io import fits, ascii; import regions; import radio_beam; import astropy
from spectral_cube import SpectralCube
cube = SpectralCube.read('W51w51d2_only.B3.robust0.5.spw0.clarkclean10000.image.pbcor.medsub.fits')
cube = SpectralCube.read('W51w51e2e_only.B3.robust0.5.spw0.clarkclean10000.image.pbcor.medsub.fits')
mx = cube.max(axis=(1,2))
import pyspeckit
sp = pyspeckit.Spectrum.from_hdu(mx.hdu)
sp.plotter()
pl.draw(); pl.show()
import pylab as pl
pl.draw(); pl.show()
sp.specfit.parinfo
utils.minimize_table(Splatalogue.query_lines(85.566*(1+50/3e5)*u.GHz, 85.568*(1+65/3e5)*u.GHz))
utils.minimize_table(Splatalogue.query_lines(85.566*(1+50/3e5)*u.GHz, 85.568*(1+65/3e5)*u.GHz)).pprint(max_lines=100)
cube.find_lines(chemical_name='Recombination')
sp.specfit.parinfo
(sp.specfit.parinfo[1].value - 85.5739967e10)/85.5739967e10 * 3e5
sp.specfit.parinfo[1]
sp.specfit.parinfo[1].value
(sp.specfit.parinfo[1].value - 85.5739967e9)/85.5739967e9 * 3e5
utils.minimize_table(Splatalogue.query_lines(85.566*(1+50/3e5)*u.GHz, 85.568*(1+65/3e5)*u.GHz)).pprint(max_lines=100)
sp.specfit.parinfo[1].value
utils.minimize_table(Splatalogue.query_lines(85.66*(1+50/3e5)*u.GHz, 85.68*(1+65/3e5)*u.GHz)).pprint(max_lines=100)
utils.minimize_table(Splatalogue.query_lines(85.66*(1+50/3e5)*u.GHz, 85.68*(1+65/3e5)*u.GHz)).pprint(max_lines=200)
utils.minimize_table(Splatalogue.query_lines(85.66*(1+50/3e5)*u.GHz, 85.67*(1+65/3e5)*u.GHz)).pprint(max_lines=200)
for sourcename in sources:
    cube = SpectralCube.read(f'W51{sourcename}_only.B3.robust0.5.spw0.clarkclean10000.image.pbcor.medsub.fits')
    cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=85.68839*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).write(f'{sourcename}_H42a_cutout.fits')

get_ipython().run_line_magic('run', 'smallcube_cutouts.py')
get_ipython().run_line_magic('run', 'source_ids.py')
for sourcename in sources:
    cube = SpectralCube.read(f'W51{sourcename}_only.B3.robust0.5.spw0.clarkclean10000.image.pbcor.medsub.fits')
    cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=85.68839*u.GHz).spectral_slab(-30*u.km/u.s, 130*u.km/u.s).write(f'{sourcename}_H42a_cutout.fits')

exit()
