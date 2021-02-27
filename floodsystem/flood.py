"""This module contains functions for analysing flood risk"""

from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    """This function, given a list of MonitoringStation objects and a tolerance, returns a list of tuples,
    each containing the station object where the relative water level is above the tolerance,
    and the relative water level at that station. The list is sorted in descending level of relative water level."""

    lst = []
    for station in stations:
        if (station.relative_water_level != None) and (station.relative_water_level >= tol):
            lst.append(station, station.relative_water_level)
    return lst
