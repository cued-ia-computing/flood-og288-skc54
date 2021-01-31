from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    '''Requirements for task 1B'''

    stations = build_station_list() # Make a list of stations
    p = 52.2053, 0.1218 # Insert coordinates
    
    station_names = [] # Make empty lists for the station names, towns they are nearest to, and their distances from the coordinates
    towns = []
    distances_from_p = []

    x=0 # Set counting variable to go through list

    for station in stations_by_distance(stations, p)[:10]: # Goes through the list created by the stations_by_distance command and takes data to add to the 3 lists created previously
        
        station_names.append(stations_by_distance(stations, p)[x][0].name)
        towns.append(stations_by_distance(stations, p)[x][0].town)
        distances_from_p.append(stations_by_distance(stations, p)[x][1])

        x+=1 # Counting variable increases with each loop


    nearest = list(zip(station_names, towns, distances_from_p)) # Create list of tuples for nearest stations
    print(x , "nearest are:" , nearest) # Print list

    # Second half of the code is similar to the first half, but displays data for the furthest stations

    station_names.clear() # Clear previous lists
    towns.clear()
    distances_from_p.clear()

    y = 0 # Set new counting variable

    furthest_stations = stations_by_distance(stations, p)[-10:] # Create list of 10 furthest stations

    for station in furthest_stations: # Take data from this list as before to add to the 3 lists.
        
        station_names.append(furthest_stations[y][0].name)
        towns.append(furthest_stations[y][0].town)
        distances_from_p.append(furthest_stations[y][1])

        y+=1


    furthest = list(zip(station_names, towns, distances_from_p)) # Create list of tuples for furthest stations
    print(y , "furthest are:" , furthest) # Print furthest stations

        
run()