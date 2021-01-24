# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine

def stations_by_distance(stations, p):
    '''Lists stations by distance'''

    distances = [] # Make an empty list to store the distances from p in

    for station in stations:
        distance = haversine(station.coord, p) # Calculate distance of p from each station
        distances.append(distance) # Add this distance to the distances list
    
    distances = list(zip(stations, distances)) # Create a list of tuples with stations and their distances
 
    distances = sorted_by_key(distances, 1) # Sort this list

    return distances

