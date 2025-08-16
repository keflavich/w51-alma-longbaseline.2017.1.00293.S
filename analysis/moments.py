from spectral_cube import SpectralCube
from astropy import units as u
from astropy.io import fits
from astropy.visualization import simple_norm
import numpy as np
import pyavm
import os
from PIL import Image
basepath = '/orange/adamginsburg/w51/2017.1.00293.S'

fns = {(sourcename, spw): f'{basepath}/line_cubes/W51{sourcename}_only.B3.robust0.5.spw{spw}.clarkclean1e5.1536.bigpix.image.pbcor.medsub.fits'
       for sourcename in ('w51e5', 'w51n', 'w51e_n',  'w51main', 'w51e8', 'w51sw', 'w51n_mm24')
       for spw in (0, 1, 2, 3)}

lines = {'SiO2-1_v=0':  86846.96*u.MHz,
         'SiO2-1_v=1': 86243.4277*u.MHz,
         'SiO2-1_v=2': 85640.453*u.MHz,
         '29SiO2-1_v=0': 85759.194*u.MHz,
         'HCN1-0_v=0': 88630.4157*u.MHz,
         'CS2-1_v=0': 97980.953*u.MHz,
         'SO32-21': 99299.87*u.MHz,
         'SO22-11': 86093.95*u.MHz,
         'HC15N_1-0': 88630.4157*u.MHz,
         'H13CN_1-0': 86340.1666*u.MHz,
         'SO2_835-928': 86639.095*u.MHz,
         'SO2_220-313': 100878.105*u.MHz,
}

vrange_blue = (30, 51)*u.km/u.s
vrange_green = (51, 69)*u.km/u.s
vrange_red = (69, 95)*u.km/u.s

outdir_mom = f'{basepath}/moments'
os.makedirs(outdir_mom, exist_ok=True)

for (sourcename, spw), fn in fns.items():
    cube = SpectralCube.read(fn)
    cube.beam_threshold = 0.1
    for line, freq in lines.items():

        if (freq > cube.spectral_axis.min()) & (freq < cube.spectral_axis.max()):
            vcube = cube.with_spectral_unit(u.km/u.s, velocity_convention='radio', rest_value=freq)

            blue_fn = f'{outdir_mom}/{sourcename}_{line}_v=0_blue.fits'
            red_fn = f'{outdir_mom}/{sourcename}_{line}_v=0_red.fits'
            green_fn = f'{outdir_mom}/{sourcename}_{line}_v=0_green.fits'

            vcube.spectral_slab(*vrange_blue).moment0(axis=0).write(blue_fn, overwrite=True)
            vcube.spectral_slab(*vrange_red).moment0(axis=0).write(red_fn, overwrite=True)
            vcube.spectral_slab(*vrange_green).moment0(axis=0).write(green_fn, overwrite=True)

            r = fits.getdata(red_fn)
            g = fits.getdata(green_fn)
            b = fits.getdata(blue_fn)
            header = fits.getheader(red_fn)

            r_scaled = simple_norm(r, stretch='asinh', max_percent=99.5)(r)
            g_scaled = simple_norm(g, stretch='asinh', max_percent=99.5)(g)
            b_scaled = simple_norm(b, stretch='asinh', max_percent=99.5)(b)

            # dstack puts the extra dimension at the end instead of the beginning
            # stands for 'depth stack'
            rgb_scaled = np.dstack([r_scaled, g_scaled, b_scaled])

            outdir_rgb = f'{basepath}/moments/pngs'
            os.makedirs(outdir_rgb, exist_ok=True)
            out_png = f"{outdir_rgb}/{sourcename}_{line}_moments_rgb.png"

            img_uint8 = (rgb_scaled * 255).astype('uint8')
            Image.fromarray(img_uint8, mode='RGB').save(out_png)

            avm = pyavm.AVM.from_header(header)
            avm.embed(out_png, out_png)
