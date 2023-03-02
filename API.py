import datetime as dt
import requests
import json
from pprint import pprint

data = {"defaut":"acadd25a0f2a9c1c0350a18778c600d6"}

# """
# with open('all_keys.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
# """

class API:
    def __init__(self, API = data['defaut'], city='Manaus'):
        self.__API_key = API
        self.city = city
        self.__base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + self.__API_key + "&q=" + self.city
        self.weather_data = requests.get(self.__base_url).json()
        self.temp_kelvin = self.weather_data['main']['temp']
        self.temp_celcius = self.kelvin_to_celsius()
        self.temp_fahrenheit = self.celcius_fahrenheit()

    def kelvin_to_celsius(self):
        return self.temp_kelvin - 273.15
    
    def celcius_fahrenheit(self):
        return self.temp_celcius * (9/5) + 32

    def change_API_key(self, new_API_key):
        self.__change_API_key(new_API_key)

API = API()
