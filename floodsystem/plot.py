''' This module contains functions for plotting graphs'''

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):
    '''Displays a plot of the water level data against time for a station'''

    #station_levels = [] # Make an empty list for the station levels over time
    #times = []
    #levels = fetch_measure_levels(station.id, dates) 

    #for i in levels:
        #station_levels.append(levels[1][i]) # Fill the station_levels list with the levels of the station over the past

    #for t in levels:
        #times.append(levels[0][t])

    plt.plot (dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)

    plt.tight_layout()
    
    plt.show()
