# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town, l_level=None):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = l_level

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """This class method checks whether the high/low range data is,
        firstly, available, and secondly that the high is larger than the low."""
        try:
            if self.typical_range[0] < self.typical_range[1]:
                return True
            else:
                return False
        except TypeError:
            return False

    def relative_water_level(self):
        """This class method returns the latest water level as a fraction of the typical range.
        If the required data is unavailable or inconsistent it returns 'None'."""
        if self.typical_range_consistent():
            return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
        else:
            return None


def inconsistent_typical_range_stations(stations):
    """Given a list of station objects, this function returns a list of those with inconsistent range data"""
    lst = []
    for station in stations:
        if not station.typical_range_consistent():
            lst.append(station.name)
    return lst
