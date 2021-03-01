from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime


def run():
    stations = build_station_list()
    update_water_levels(stations)
    dt = 2  # Number of days
    nonworking_stations = []  # Create a list for stations with erroneous data
    for i in stations:
        if type(i.relative_water_level()) == float:  # Check to see if the data is corrct and can be used
            station_levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
            if type(polyfit(station_levels[0], station_levels[1], 1)) == tuple:
                p = polyfit(station_levels[0], station_levels[1], 1)[0][0]
                # This takes the coefficient of the polynomial produced by polyfit.
                # As it is order one, the coefficient is the slope. This tells us if the water level is rising or not
                if i.relative_water_level() > 3 and p > 0:
                    # If the relative water level is above 3, the risk is SEVERE
                    print("Risk is SEVERE at", i.name, "and the water level has been RISING")
                elif i.relative_water_level() > 3 and p < 0:
                    print("Risk is SEVERE at", i.name, "and the water level is DECREASING")
                elif i.relative_water_level() > 2 and p > 0:
                    # If the relative water level is above 2, the risk is HIGH
                    print("Risk is HIGH at", i.name, "and the water level is RISING")
                elif i.relative_water_level() > 2 and p < 0:
                    print("Risk is HIGH at", i.name, "and the water level is DECREASING")
                elif i.relative_water_level() > 1 and p > 0:
                    # If the relative water level is above 1, the risk is MODERATE
                    print("Risk is MODERATE at", i.name, "and the water level is RISING")
                elif i.relative_water_level() > 1 and p < 0:
                    print("Risk is MODERATE at", i.name, "and the water level is DECREASING")
                else:
                    # If the relative water level is under 1, the risk is LOW
                    print("Risk is LOW at", i.name)
            else:
                nonworking_stations.append(i.name)
        else:
            pass
    print("The following stations are returning erroneous data:", nonworking_stations)


run()
