"""
A dictionary of source names and their locations
"""
raise NotImplementedError("Use W51_ALMA_2013.1.00308.S version instead")

from astropy import coordinates, units as u

sources = {'w51e2e': (290.9331907, 14.50958333),
           'w51e8': (290.9329337, 14.50784566),
           'w51e2se': (290.9336503, 14.50930947),
           'w51e2w': (290.93295, 14.509592),
           'w51e2nw': (290.93282, 14.510005),
           'w51n': (290.9168748, 14.51818126),
           'w51d2': (290.9159067, 14.51800749),
           'w51n_mm24': (290.9164773, 14.51814722),
           'w51n_123': (290.9171007, 14.51825111),
           'w51noutflow': ('19:23:39.7352296972', '14:31:18.4960179735'),
          }
units = {'w51noutflow': (u.h, u.deg)}

source_field_mapping = {'w51e2e': 'w51e2',
                        'w51e8': 'w51e2',
                        'w51e2se': 'w51e2',
                        'w51e2w': 'w51e2',
                        'w51e2nw': 'w51e2',
                        'w51n': 'w51n',
                        'w51d2': 'w51n',
                        'w51n_mm24': 'w51n',
                        'w51n_123': 'w51n',
                        'w51noutflow': 'w51n',
                       }

def casafmt(crd, unit=(u.deg, u.deg)):
    center = coordinates.SkyCoord(*crd, frame='icrs', unit=unit)

    return 'ICRS {} {}'.format(center.ra.to_string(unit=u.hour),
                               center.dec.to_string())

sources_fmtd = {key: casafmt(val, unit=units.get(key, (u.deg, u.deg))) for key, val in sources.items()}
