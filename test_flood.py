
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from test_geo import data


def test_stations_level_over_threshold():
    assert(stations_level_over_threshold(data, 0.8)[0][0].name == "Sheffield Carr Brook Screen")
    assert(stations_level_over_threshold(data, 0.8)[0][1] == 0.9752066115702479)
    assert(stations_level_over_threshold(data, 0.8)[1][0].name == "Grimesthorpe")
    assert(stations_level_over_threshold(data, 0.8)[1][1] == 0.9732334047109208)


def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    assert(len(stations_highest_rel_level(stations, 20)) == 20)
    assert(stations_highest_rel_level(data, 5)[0].name == "Sheffield Carr Brook Screen")
    assert(stations_highest_rel_level(data, 5)[1].name == "Grimesthorpe")
    assert(stations_highest_rel_level(data, 5)[2].name == "Vexour Bridge")
    assert(stations_highest_rel_level(data, 5)[3].name == "Denby Dale Norman Road")
