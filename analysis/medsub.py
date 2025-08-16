from spectral_cube import SpectralCube
import os
basepath = '/orange/adamginsburg/w51/2017.1.00293.S'

fns = {(sourcename, spw): f'{basepath}/line_cubes/W51{sourcename}_only.B3.robust0.5.spw{spw}.clarkclean1e5.1536.bigpix.image.pbcor.fits'
       for sourcename in ('w51n', 'w51e5', 'w51e_n', 'w51main', 'w51e8', 'w51sw', 'w51n_mm24', 'w51noutflow')
       for spw in (0, 1, 2, 3)}


from statcont.cont_finding import c_sigmaclip_scube
from astropy.io import fits
for fn in fns.values():

    cube = SpectralCube.read(fn)
    if not os.path.exists(fn.replace('.fits', '.medsub.fits')):
        print(f"Median subtracting {fn}")
        cube.beam_threshold = 0.1
        cube.allow_huge_operations = True
        med = cube.median(axis=0)
        medsub = cube - med
        medsub.write(fn.replace('.fits', '.medsub.fits'))


for fn in fns.values():
    outfn = fn.replace('.fits', '.cont.fits')
    if os.path.exists(outfn):
        cont = fits.getdata(outfn)
    else:
        print(f"Finding continuum for {fn}")
        cube = SpectralCube.read(fn, use_dask=True)
        noise = cube.std()
        result = c_sigmaclip_scube(cube, noise,
                                    verbose=True,
                                    save_to_tmp_dir=True)
        data_to_write = result[1].compute()
        cont = data_to_write.value

        print(f"Writing to FITS {outfn}", flush=True)
        fits.PrimaryHDU(data=cont,
                        header=cube[0].header).writeto(outfn, overwrite=True)

    outfn = fn.replace('.fits', '.contsub.fits')
    if not os.path.exists(outfn):
        print(f"Subtracting continuum for {fn}")
        cube = SpectralCube.read(fn, use_dask=True)
        try:
            cube.allow_huge_operations = True
        except Exception as ex:
            print(f"Failed to set allow_huge with exception={ex} [this is expected b/c we're trying to load as a dask cube]")
        contsub = cube - u.Quantity(cont, cube.unit)
        contsub.write(outfn)
