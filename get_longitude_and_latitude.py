import requests
import sys

API_KEY = sys.argv[1]

city = input("City: ")
state_code = input("State code: ")
country_code = input("Country Code: ")

long_and_lat_request = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},{country_code}&appid={API_KEY}")
long_and_lat_data = long_and_lat_request.json()

longitude = long_and_lat_data["coordinates"]["longitude"]
latitude = long_and_lat_data["coordinates"]["latitude"]

