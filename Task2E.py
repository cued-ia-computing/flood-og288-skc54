
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():

    dt = 10 # Data from up to 10 days ago

    stations = build_station_list()
    update_water_levels(stations)
    At_risk_stations = stations_highest_rel_level(stations, 5)
    for i in At_risk_stations: # Create graphs for each station
        station = i
        station_levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, station_levels[0], station_levels[1])


run()
