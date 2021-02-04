
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()

rivers = list(rivers_with_station(stations))
rivers.sort()

print("{} rivers. First 10 - {}".format(len(rivers), rivers[:10]))

dict = stations_by_river(stations)

Aire = dict["River Aire"]
Aire.sort()
print(Aire)

Cam = dict["River Cam"]
Cam.sort()
print(Cam)

Thames = dict["River Thames"]
Thames.sort()
print(Thames)
