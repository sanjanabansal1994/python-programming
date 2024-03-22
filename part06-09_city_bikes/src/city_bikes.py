# tee ratkaisu tänne
# Write your solution here
import math
def get_station_data(filename: str):
    with open(filename) as file:
        station={}
        for line in file:
            part=(line.split(";"))
            if part[3]=='name':
                continue
            else:
                station[part[3]]=(float(part[0].strip()), float(part[1].strip()))
    return (station)


def distance(stations: dict, station1: str, station2: str):
    x= abs(float(stations[station1][0])-float(stations[station2][0]))*55.26
    y= abs(float(stations[station1][1])-float(stations[station2][1]))*111.2
    distance_km = math.sqrt(x**2 + y**2)
    return distance_km


def greatest_distance(stations: dict):
    max=0
    for station1 in stations.keys():
        for station2 in stations.keys():
            d= distance(stations, station1,station2)
            if d > max:
                res=(station1, station2,d)
                max=d

    return res




# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)
