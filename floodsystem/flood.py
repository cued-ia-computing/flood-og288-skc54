"""This module contains functions for analysing flood risk"""

from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """This function, given a list of MonitoringStation objects and a tolerance, returns a list of tuples,
    each containing the station object where the relative water level is above the tolerance,
    and the relative water level at that station. The list is sorted in descending level of relative water level."""

    lst = []
    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() >= tol:
                lst.append((station, station.relative_water_level()))
    return sorted_by_key(lst, 1, True)


def stations_highest_rel_level(stations, N):
    """This function return a list of the N station objects with the highest relative water level.
    The list ids sorted in descending order of relative water level"""

    lst = stations_level_over_threshold(stations, -10 ** 9)
    if N <= 0:
        return None
    lst1 = lst[:N]
    lst2 = []
    for station_tup in lst1:
        lst2.append(station_tup[0])
    return lst2
