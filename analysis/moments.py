from spectral_cube import SpectralCube
basepath = '/orange/adamginsburg/w51/2017.1.00293.S'

fns = {sourcename: f'{basepath}/line_cubes/W51{sourcename}_only.B3.robust0.5.spw{spw}.clarkclean1e5.1536.bigpix.image.pbcor.medsub.fits'
       for sourcename in ('w51e5', 'w51e_n', 'w51n', 'w51main', 'w51e8', 'w51sw', 'w51n_mm24')
       for spw in (0, 1, 2, 3)}
