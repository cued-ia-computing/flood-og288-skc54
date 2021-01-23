
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station

data = []

data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/0503SO", "http://environment.data.gov.uk/flood-monitoring/id/measures/0503SO-level-stage-i-15_min-mASD", "Stonebridge", (51.132785, 0.453941), (0.082, 1.78), "River Teise", "Horsmonden"))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/0904SO", "http://environment.data.gov.uk/flood-monitoring/id/measures/0904SO-level-stage-i-15_min-mASD", "Vexour Bridge", (51.189651, 0.160853), (0.603, 2.9), "Eden Tributary  Medway", "Chiddingstone Causeway"))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/L0681", "http://environment.data.gov.uk/flood-monitoring/id/measures/L0681-level-stage-i-15_min-m", "Grimesthorpe", (53.406175, -1.435939), (-0.018, 1.85), "Bagley Dike", "Grimesthorpe"))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/L0812", "http://environment.data.gov.uk/flood-monitoring/id/measures/L0812-level-stage-i-15_min-m", "Denby Dale Norman Road", (53.571667, -1.657895), (0.186, 1.1), "River Dearne", "Denby Dale Norman Road"))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/L0691", "http://environment.data.gov.uk/flood-monitoring/id/measures/L0691-level-stage-i-15_min-m", "Sheffield Carr Brook Screen", (53.380377, -1.409716), (-0.028, 0.093), "Carr Brook", "Sheffield Carr Brook Screen"))


def test_rivers_with_station():

    # Check function provides the same output for a fixed dataset
    assert(rivers_with_station(data) == {'River Teise', 'Bagley Dike', 'Eden Tributary  Medway', 'Carr Brook', 'River Dearne'})

    # Get list of station objects
    stations = build_station_list()

    # Get list of rivers
    rivers = rivers_with_station(stations)

    # Check number of rivers
    assert(len(rivers) <= len(stations))
