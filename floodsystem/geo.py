# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def rivers_with_station(stations):
    """ Given a list of station objects, this function returns a set,
    with the names of the rivers with a monitoring station.
    """

    rivers = set()

    for station in stations:
        rivers.add(station.river)

    return rivers


def stations_by_river(stations):
    """ Given a list of station objects, this function returns a dictionary,
    that maps each river with a station on (the keys), to a list of the
    stations on that river"""

    dict = {}

    for station in stations:
        if station.river in dict.keys():
            dict[station.river].append(station.name)
        else:
            dict[station.river] = [station.name]
    return dict


def stations_by_distance(stations, p):
    '''Lists stations by distance'''

    distances = [] # Make an empty list to store the distances from p in

    for station in stations:
        distance = haversine(station.coord, p) # Calculate distance of p from each station
        distances.append(distance) # Add this distance to the distances list

    distances = list(zip(stations, distances)) # Create a list of tuples with stations and their distances

    distances = sorted_by_key(distances, 1) # Sort this list

    return distances
