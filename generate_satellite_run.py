from astropy import units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
import numpy as np

altitude = 500
a = (6371 + altitude) << u.km
ecc = 0.004 << u.one
inc = 97.7 << u.deg
raan = 200 << u.deg
argp = 0 << u.deg
nu = 0 << u.deg

orb = Orbit.from_classical(Earth, a, ecc, inc, raan, argp, nu)

times = np.linspace(0,1000,10001)

outfile = './satellite_100_highres.csv'

with open(outfile, 'w') as f:
    for t in times:
        vector = (orb.propagate(t << u.s).r << u.m).value
        f.write(f'{t}, {vector[0]}, {vector[1]}, {vector[2]}\n')
