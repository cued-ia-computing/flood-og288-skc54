from test_geo import data
from floodsystem.analysis import polyfit
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def test_polyfit():

    dt = 2

    update_water_levels(data)
    for i in data:
        station = i
        station_levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        assert(polyfit(station_levels[0], station_levels[1], 4)[1]) >= 0  # Check that the difference is positive
