# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def stations_by_distance(stations, p):
    '''Lists stations by distance'''

    distances = [] # Make an empty list to store the distances from p in

    for station in stations:
        distance = haversine(station.coord, p) # Calculate distance of p from each station
        distances.append(distance) # Add this distance to the list of distances
    
    distances = list(zip(stations, distances)) # Create a list of tuples with stations and their distances
 
    distances = sorted_by_key(distances, 1) # Sort this list

    return distances


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


def rivers_by_station_number(stations, N):
    """Given a list of station objects, and a value N, this function
    returns a list of tuples with the N rivers with the largest number
    of stations. If there is more than one river with the same number
    of stations as the Nth river, they will be included as well"""

    dict = stations_by_river(stations)
    lst = []
    for river in dict.keys():
        lst.append((river, len(dict[river])))

    new = sorted_by_key(lst, 1, True)
    n = N
    if N > len(new):
        return new
    while True:
        try:
            if new[n - 1][1] != new[n][1]:
                break
        except IndexError:
            break
        n += 1
    return new[:n]


def stations_within_radius(stations, centre, r):
    '''Returns a list of stations within a specified distance of a coordinate'''

    list_of_stations = [] # Make an empty list

    for station in stations: # Iterate over the stations and add the ones which are within the radius to the list
        distance = haversine(station.coord, centre, unit=Unit.KILOMETERS)
        if distance < r:
            list_of_stations.append(station.name)
        else:
            pass

    return list_of_stations