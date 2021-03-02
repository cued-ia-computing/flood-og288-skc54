from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for task 1C"""

    stations = build_station_list()  # Specify stations, coordinate of centre and radius (in kilometers)
    centre = 52.2053, 0.1218
    r = 10

    station_names = []  # Create an empty list

    for station in stations_within_radius(stations, centre, r):  # Add to the empty list
        station_names.append(station)

    station_names.sort()  # Sort the list

    print(station_names)  # Print the sorted list


run()
