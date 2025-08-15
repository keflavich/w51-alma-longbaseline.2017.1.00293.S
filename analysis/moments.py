from spectral_cube import SpectralCube
basepath = '/orange/adamginsburg/w51/2017.1.00293.S'

fns = {sourcename: f'{basepath}/line_cubes/W51{sourcename}_only.B3.robust0.5.spw{spw}.clarkclean1e5.1536.bigpix.image.pbcor.medsub.fits'
       for sourcename in ('w51e5', 'w51e_n', 'w51n', 'w51main', 'w51e8', 'w51sw', 'w51n_mm24')
       for spw in (0, 1, 2, 3)}

lines = {'SiO2-1_v=0':  86846.96*u.MHz,
         'SiO2-1_v=1': 86243.4277*u.MHz,
         'SiO2-1_v=2': 85640.453*u.MHz,
         '29SiO2-1_v=0': 85759.194*u.MHz,
         'HCN1-0_v=0': 88630.4157*u.MHz,
         'CS2-1_v=0': 97980.953*u.MHz,
         'SO32-21': 99299.87*u.MHz,
}

vrange_blue = (30, 51)*u.km/u.s
vrange_red = (69, 95)*u.km/u.s

for sourcename, fn in fns.items():
    cube = SpectralCube.read(fn)
    cube.beam_threshold = 0.1
    for line, freq in lines.items():
        vcube = cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=freq)
        vcube.spectral_slab(*vrange_blue).moment0(axis=0).write(f'{basepath}/moments/{sourcename}_{line}_v=0_blue.fits')
        vcube.spectral_slab(*vrange_red).moment0(axis=0).write(f'{basepath}/moments/{sourcename}_{line}_v=0_red.fits')