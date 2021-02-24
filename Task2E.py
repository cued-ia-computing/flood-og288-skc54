'''This is a preliminary test to see if the pllot_water_levels function for 2E works, it does not fill the objectives listed'''

from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta

def run():

    dt = 10
    stations = build_station_list()
    station = stations[0]
    station_levels = fetch_measure_levels(station.id, dt=datetime.timedelta(days=dt))
    plot_water_levels(station, station_levels[0], station_levels[1])

run()
