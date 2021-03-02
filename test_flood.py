
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.station import MonitoringStation

data = []

data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/0503SO",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/0503SO-level-stage-i-15_min-"
                              "mASD",
                              "Stonebridge", (51.132785, 0.453941), (82, 1.78), "River Teise", "Horsmonden", 4))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/0904SO",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/0904SO-level-stage-i-15_min-"
                              "mASD",
                              "Vexour Bridge", (51.189651, 0.160853), (0.603, 2.9), "Eden Tributary  Medway",
                              "Chiddingstone Causeway", 1))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/L0681",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/L0681-level-stage-i-15_"
                              "min-m",
                              "Grimesthorpe", (53.406175, -1.435939), (-0.018, 1.85), "Bagley Dike", "Grimesthorpe",
                              1.8))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/L0812",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/L0812-level-stage-i-15_"
                              "min-m",
                              "Denby Dale Norman Road", (53.571667, -1.657895), (0.186, 1.1), "River Dearne",
                              "Denby Dale Norman Road", 0.2))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/L0691",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/L0691-level-stage-i-15_"
                              "min-m", "Sheffield Carr Brook Screen", (53.380377, -1.409716), (-0.028, 0.093),
                              "Carr Brook", "Sheffield Carr Brook Screen", 0.09))


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
