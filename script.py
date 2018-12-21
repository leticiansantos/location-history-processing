from geopy.geocoders import Nominatim
import time

MAX = 5

def toGPS(ie7Value):
    return ie7Value / 1e7

def formatIe7Coord(lat, lon):
    return str(toGPS(lat)) + ", " + str(toGPS(lon))

def getLocation(lat, lon):
    geolocator = Nominatim()
    count = 0
    while(count < MAX):
        print(count)
        try:
            location = geolocator.reverse(formatIe7Coord(lat, lon), addressdetails=True)
            return {
                "city" : location.raw['address']['city'],
                "county" : location.raw['address']['county'],
                "state" : location.raw['address']['state'],
                "country" : location.raw['address']['country'],
                "suburb" : location.raw['address']['suburb'],
                "neighbourhood" : location.raw['address']['neighbourhood']
            }
            break
        except Exception as e:
            print(e)
            time.sleep(10)
            count += 1
            pass

lat = 476179045
lon = -1223445753
loc = getLocation(lat, lon)
print(loc)
