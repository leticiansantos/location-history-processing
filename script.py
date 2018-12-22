from geopy.geocoders import Nominatim
import time
import json

MAX = 5

def toGPS(ie7Value):
    return ie7Value / 1e7

def formatIe7Coord(lat, lon):
    return str(toGPS(lat)) + ", " + str(toGPS(lon))

def getLocation(lat, lon):
    geolocator = Nominatim()
    count = 0
    while(count < MAX):
        # print(count)
        try:
            location = geolocator.reverse(formatIe7Coord(lat, lon), addressdetails=True)
            # print(location.raw)
            return {
                "city" : location.raw['address']['city'],
                "county" : location.raw['address']['county'],
                "state" : location.raw['address']['state'],
                "country" : location.raw['address']['country'],
                "suburb" : location.raw['address']['suburb']
                # "neighbourhood" : location.raw['address']['neighbourhood']
            }
            break
        except Exception as e:
            # print(e)
            time.sleep(10)
            count += 1
            pass

def parseJsonFile(filename):
    with open(filename, 'r') as f:
        return json.load(f)

obj = parseJsonFile("sample.json")
for loc in obj['locations']:
    place = getLocation(loc['latitudeE7'], loc['longitudeE7'])
    print(place)
