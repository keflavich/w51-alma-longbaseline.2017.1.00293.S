import numpy as np
import os
import json
import copy
import glob
import shutil
import subprocess
import datetime
from astropy.io import ascii
import sys
from astropy import log
from aces.retrieval_scripts.mous_map import get_mous_to_sb_mapping
from aces.imaging.parallel_tclean import parallel_clean_slurm
from aces.pipeline_scripts.merge_tclean_commands import get_commands
from aces import conf

BASEPATH='/orange/adamginsburg/w51/2017.1.00293.S'
PROJCODE='2017.1.00293.S'
SOUS=""
GOUS=""
MOUS=""

vis = [
]
datadir = ''


for spw in (0,1,2,3):
    tcpars = {
        "perchanweightdensity": True,
        "gridder": "mosaic",
        "pblimit": 0.2,
        "deconvolver": "hogbom",
        "scales": [],
        "nterms": 2,
        "smallscalebias": 0.0,
        "restoration": True,
        "restoringbeam": "common",
        "pbcor": True,
        "weighting": "briggsbwtaper",
        "niter": 20000000,
        "gain": 0.1,
        "cyclefactor": 2.0,
        "minpsffraction": 0.05,
        "maxpsffraction": 0.8,
        "interactive": 0,
        "usemask": "auto-multithresh",
        "mask": "",
        "pbmask": 0.0,
        "sidelobethreshold": 2.0,
        "noisethreshold": 4.25,
        "lownoisethreshold": 1.5,
        "negativethreshold": 15.0,
        "smoothfactor": 1.0,
        "minbeamfrac": 0.3,
        "cutthreshold": 0.01,
        "growiterations": 50,
        "dogrowprune": True,
        "minpercentchange": 1.0,
        "restart": True,
        "savemodel": "none",
        "psfcutoff": 0.35,
        "threshold": "0.01mJy",
        "imsize": [2048, 2048],
        "cell": ['0.25arcsec'],
        "restfreq": '97.981GHz',
        "robust": 0.5,
        "start": 0,
        "vis": [os.path.join(datadir, v) for v in vis],
    }
    # parallel_clean handles the splitting (but it is forced to assume all MSes have the same spw)
    # tcpars['spw'] = [str(spw)] * len(vis)
    field = tcpars['field'] = 'TODO'
    tcpars['phasecenter'] = 'TODO'
    # nchan must be given to tclean; we can't use -1 (TODO: implement -1->all introspection)
    #tcpars['nchan'] = -1
    tcpars['width'] = 1
    tcpars['specmode'] = 'cube'
    tcpars['niter'] = 1000000
    tcpars['imagename'] = f'{field}_spw{spw}_cube'

    qos = os.getenv('QOS')
    if qos:
        account = os.environ['ACCOUNT'] = 'adamginsburg' if 'adamginsburg' in qos else 'astronomy-dept'
        if 'astronomy-dept' not in qos and 'adamginsburg' not in qos:
            raise ValueError(f"Invalid QOS {qos}")
    else:
        account = 'astronomy-dept'
        qos = 'astronomy-dept-b'
    logpath = os.environ['LOGPATH'] = conf.logpath
    qos_ = qos

    jobtime = '96:00:00'
    jobname = f'W51TODO_2017.1.TODO_{spw}'
    workdir='/blue/adamginsburg/adamginsburg/ACES/working/2017.1.TODO/'

    savedir='/orange/adamginsburg/ACES/ancillary/data/2017.1.TODO/science_goal.uid___A002_X6444ba_Xc/group.uid___A002_X6444ba_Xd/member.uid___A002_X6444ba_Xe/calibrated/workdir/'
    tempdir_name = 'W51TODO_2017.1.TODO'

    nchan = 3880
    parallel_clean_slurm(nchan=nchan,
                         imagename=os.path.basename(tcpars.pop('imagename')),
                         spw=spw,
                         start=tcpars.pop('start') or 0,
                         width=tcpars.pop('width') or 1,
                         field=tcpars.pop('field'),
                         jobname=jobname,
                         workdir=f'{workdir}/{tempdir_name}',
                         qos=qos_,
                         account=account,
                         jobtime=jobtime,
                         dry=False,
                         ntasks=16,
                         nchan_per=16,
                         mem_per_cpu='4gb',
                         savedir=savedir,
                         remove_incomplete_psf=False,
                         remove_incomplete_weight=False,
                         **tcpars
                         )