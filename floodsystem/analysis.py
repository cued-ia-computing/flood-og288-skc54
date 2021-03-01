'''This module contains functions for analysing data'''

import numpy as np
import matplotlib.dates


def polyfit(dates, levels, p):
    '''Creates a least-squares fit of a polynomial of degree p given time and level data.
    Returns a tuple of the polynomial and the shift'''

    for i in levels:  # Check that water level data is in the correct form
        if type(i) == float:
            pass
        else:
            return print("Error with water level data for this station.")

    if type(dates) == list and type(levels) == list:  # Check the data is given in the right form
        if len(dates) > 2 and len(levels) > 2:  # Check there are enough data points to work with
            x = matplotlib.dates.date2num(dates)  # The time data is converted to a list of floats
            y = levels
            if type(x) == np.ndarray and type(y) == list:
                p_coeff = np.polyfit(x - x[0], y, p)
                # Time data is shifted so it does not go above 1000, which would cause errors to build up

                poly = np.poly1d(p_coeff)

                d0 = 0

                for i, n in zip(x, y):
                    difference = n - poly(i - x[0])
                    d0 += difference**2

                return (poly, d0)
            else:
                return print("Error with water level data for this station.")  # Error message
        else:
            return print("Error with water level data for this station.")
    else:
        return print("Error with water level data for this station")
