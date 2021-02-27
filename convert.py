import numpy as np

def to_rect(mag, deg):
    '''
    USAGE: to_rect(magnitude of wave, angle in degrees)
    '''
    return mag * np.exp(1j*np.deg2rad(deg))

def to_polar(num):
    '''
    USAGE: to_polar(complex number)
    '''
    mag = round(abs(num), 3)
    deg = round(np.rad2deg(np.angle(num)), 3)
    return str(mag) + "<" + str(deg)