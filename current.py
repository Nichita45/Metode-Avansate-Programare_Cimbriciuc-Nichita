from dotenv import load_dotenv
import os
import requests
load_dotenv()
os.system('cls')
weather_api = os.getenv("API_KEY")
oras = input("Introduceti orasul: ")
url = "https://api.openweathermap.org/data/2.5/weather?"
url_geocoding = "http://api.openweathermap.org/geo/1.0/direct?"

response_geocoding = requests.get(url_geocoding, params={
    'q': oras, 
    'appid': weather_api}).json()

lat = response_geocoding[0]['lat']
lon = response_geocoding[0]['lon']

response = requests.get(url, params={
    'lat': lat, 
    'lon': lon, 
    'appid': weather_api,
    'units': 'metric',
    'lang': 'ro'
    }).json()


print(f"Lat: {lat}, Lon: {lon}")
print(f"Temperatura: {response['main']['temp']}")
print(f"Descriere: {response['weather'][0]['description']}")