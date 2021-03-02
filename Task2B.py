
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()

update_water_levels(stations)

lis = stations_level_over_threshold(stations, 0.8)

for tup in lis:
    print("{}: {}".format(tup[0].name, tup[1]))
