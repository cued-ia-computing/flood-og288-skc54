
from floodsystem.flood import stations_level_over_threshold
from test_geo import data


def test_stations_level_over_threshold():
    assert(stations_level_over_threshold(data, 0.8)[0][0].name == "Sheffield Carr Brook Screen")
    assert(stations_level_over_threshold(data, 0.8)[0][1] == 0.9752066115702479)
    assert(stations_level_over_threshold(data, 0.8)[1][0].name == "Grimesthorpe")
    assert(stations_level_over_threshold(data, 0.8)[1][1] == 0.9732334047109208)


test_stations_level_over_threshold()
