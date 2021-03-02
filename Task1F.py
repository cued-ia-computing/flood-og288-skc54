
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

names = inconsistent_typical_range_stations(build_station_list())
names.sort()
print(names)
