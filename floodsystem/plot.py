''' This module contains functions for plotting graphs'''

import matplotlib.pyplot as plt
import datetime
from floodsystem.analysis import polyfit
import numpy as np
import matplotlib.dates


def plot_water_levels(station, dates, levels):
    '''Displays a plot of the water level data against time for a station'''

    if station.station_id == 'http://environment.data.gov.uk/flood-monitoring/id/stations/2830':
        print("Error in the station", station.name, "so it has been blacklisted.")
        raise TypeError

    else:
        pass

    plt.plot (dates, levels)
    plt.axhline(station.typical_range[0]) # Horizontal line for typical low end of range
    plt.axhline(station.typical_range[1]) # Horizontal line for typical high end of range
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    

    plt.tight_layout()
    
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    '''Displays a plot of the water level data and the best fit polynomial'''

    if station.station_id == 'http://environment.data.gov.uk/flood-monitoring/id/stations/2830':
        print("Error in the station", station.name, "so it has been blacklisted.")
        raise TypeError

    else:
        pass

    plt.plot (dates, levels, '.') # Plot of water level data
    plt.axhline(station.typical_range[0]) # Horizontal line for typical low end of range
    plt.axhline(station.typical_range[1]) # Horizontal line for typical high end of range

    x = matplotlib.dates.date2num(dates) # the time data is converted to a list fo floats
    y = levels
    p_coeff = np.polyfit(x-x[0], y, p) # time data is shifted so it does not go above 1000, which would cause errors to build up
    poly = np.poly1d(p_coeff)
    plt.plot(dates, poly(x-x[0])) # Plot of polynomial of best fit

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    

    plt.tight_layout()
    
    plt.show()
