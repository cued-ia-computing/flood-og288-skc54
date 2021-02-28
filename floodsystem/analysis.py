'''This module contains functions for analysing data'''

import numpy as np
import matplotlib.dates
import itertools

def polyfit(dates, levels, p):
    '''Creates a least-squares fit of a polynomial of degree p given time and level data. Returns a tuple of the polynomial and the shift'''

    x = matplotlib.dates.date2num(dates) # the time data is converted to a list fo floats
    y = levels

    p_coeff = np.polyfit(x-x[0], y, p) # time data is shifted so it does not go above 1000, which would cause errors to build up

    poly = np.poly1d(p_coeff)
    
    d0 = 0

    for i,n in zip(x, y):
        difference = n - poly(i-x[0])
        d0 += difference**2

    return (poly, d0)
