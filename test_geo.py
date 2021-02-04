
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.geo import stations_by_distance
from haversine import haversine
from floodsystem.geo import stations_within_radius

data = []

data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/0503SO",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/0503SO-level-stage-i-15_min-"
                              "mASD",
                              "Stonebridge", (51.132785, 0.453941), (0.082, 1.78), "River Teise", "Horsmonden"))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/0904SO",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/0904SO-level-stage-i-15_min-"
                              "mASD",
                              "Vexour Bridge", (51.189651, 0.160853), (0.603, 2.9), "Eden Tributary  Medway",
                              "Chiddingstone Causeway"))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/L0681",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/L0681-level-stage-i-15_"
                              "min-m",
                              "Grimesthorpe", (53.406175, -1.435939), (-0.018, 1.85), "Bagley Dike", "Grimesthorpe"))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/L0812",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/L0812-level-stage-i-15_"
                              "min-m",
                              "Denby Dale Norman Road", (53.571667, -1.657895), (0.186, 1.1), "River Dearne",
                              "Denby Dale Norman Road"))
data.append(MonitoringStation("http://environment.data.gov.uk/flood-monitoring/id/stations/L0691",
                              "http://environment.data.gov.uk/flood-monitoring/id/measures/L0691-level-stage-i-15_"
                              "min-m", "Sheffield Carr Brook Screen", (53.380377, -1.409716), (-0.028, 0.093),
                              "Carr Brook", "Sheffield Carr Brook Screen"))


def test_rivers_with_station():

    # Check function provides the same output for a fixed dataset
    assert(rivers_with_station(data) == {'River Teise', 'Bagley Dike', 'Eden Tributary  Medway', 'Carr Brook',
                                         'River Dearne'})

    # Get list of station objects
    stations = build_station_list()

    # Get list of rivers
    rivers = rivers_with_station(stations)

    # Check number of rivers
    assert(len(rivers) <= len(stations))


def test_stations_by_river():

    # Check function provides the same output for a fixed dataset
    assert(stations_by_river(data) == {'River Teise': ['Stonebridge'], 'Eden Tributary  Medway': ['Vexour Bridge'],
                                       'Bagley Dike': ['Grimesthorpe'], 'River Dearne': ['Denby Dale Norman Road'],
                                       'Carr Brook': ['Sheffield Carr Brook Screen']})

    # Get a list of station objects
    stations = build_station_list()

    # Get a list of rivers
    rivers = rivers_with_station(stations)

    # Check number of river keys
    assert(len(rivers) == len(stations_by_river(stations).keys()))

    # Get a list of station names
    names = []
    for station in stations:
        names.append(station.name)
    names.sort()
    # Check number of stations
    func_names = []
    for names1 in stations_by_river(stations).values():
        for name in names1:
            func_names.append(name)
    func_names.sort()

    assert(func_names == names)


def test_rivers_by_station_number():
    return


def test_stations_by_distance():

    p = 51.132785, 0.453941  # This coordinate is the same as the coordinate
    # of the first station in the list called data.

    assert stations_by_distance(data, p)[0][1] == 0.0

    assert len(stations_by_distance(build_station_list(), p)) == len(build_station_list())  # Check if the function
    # gives values for every station

    distance = haversine(data[0].coord, p)
    stations = [data[0]]
    assert stations_by_distance(stations, p)[0][1] == distance  # Test to see if the function gives an accurate value


test_stations_by_distance()


def test_stations_within_radius():

    stations = build_station_list()
    centre = 51.132785, 0.453941  # This coordinate is the same as the coordinate
    # of the first station in the list called data.
    r = 0.0000001  # Small radius ensures only one station is given by the function

    test_station = []
    test_station.append(data[0].name)  # Make a list consisting of only the name of a station
    assert stations_within_radius(stations, centre, r) == test_station  # Function should give a list which consists
    # of the name of the station

    assert len(stations_within_radius(stations, centre, 1000)) == len(build_station_list())  # Test that


test_stations_within_radius()
