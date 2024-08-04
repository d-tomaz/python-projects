from geopy.geocoders import Nominatim
from haversine import haversine, Unit

geolocator = Nominatim(user_agent = "distance_between_cities")

def get_coordinates(city):
    location = geolocator.geocode(city)
    return (location.latitude, location.longitude)

def calculate_distance(city1, city2, unit):
    coords1 = get_coordinates(city1)
    coords2 = get_coordinates(city2)

    if unit == "km":
        distance = haversine(coords1, coords2)
    elif unit == "miles":
        distance = haversine(coords1, coords2, unit = Unit.MILES)
    else:
        raise ValueError("Invalid unit. Please, use 'km' or 'miles'.")

    return distance

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")
unit = input("Enter the unit of distance (km/miles): ").lower()

try:
    distance = calculate_distance(city1, city2, unit)
    print(f"The distance between {city1} and {city2} is {distance:.2f} {unit}.")
except ValueError as e:
    print(e)