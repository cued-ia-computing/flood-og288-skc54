# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


def rivers_with_station(stations):
    """ Given a list of station objects, this function returns a set,
    with the names of the rivers with a monitoring station.
    """

    rivers = set()

    for station in stations:
        rivers.add(station.river)

    return rivers

