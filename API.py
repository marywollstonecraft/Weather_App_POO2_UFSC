import datetime as dt
import requests
import json
from pprint import pprint

KEYAPI = ''

CITY = ''

class API:
    def __init__(self, API = KEYAPI, city=CITY):
        self.__API_key = API
        self.__city = city
        self.__base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + self.__API_key + "&q=" + self.city
        
        
        self.weather_data = requests.get(self.__base_url).json()
        if weather_data['cod'] != '404':
            #temperaturas:
            self.var_kelvin = self.weather_data['main']['temp']
            self.var_celcius = self.var_kelvin - 273.15
            self.var_fahrenheit = self.self.var_celcius * (9/5) + 32
            #pressão:
            self.var_pressure = self.weather_data['main']['pressure']
            #humidade:
            self.var_humidity = self.weather_data['main']['humidity']
            #descrição:
            val_weather = self.weather_data['main']['weather']
            self.description = val_weather[0]['description']

    def change_city(self, new_city):
        self.__city = new_city


API = API()
