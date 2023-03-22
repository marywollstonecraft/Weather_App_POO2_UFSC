import datetime as dt
import requests
import json
from pprint import pprint

KEYAPI = 'acccd88416ddb8b9bc489dfdb1ec2972'

CITY = 'Manaus'

class API:
    def __init__(self, API = KEYAPI, city=CITY):
        self.__API_key = API
        self.__city = city
        self.request_data()

    def request_data(self):
        self.__base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + self.__API_key + "&q=" + self.city
        self.weather_data = requests.get(self.__base_url).json()
        if weather_data['cod'] != '404':
            #temperaturas:
            self.__var_kelvin = self__.weather_data['main']['temp']
            self.__var_celcius = self__.var_kelvin - 273.15
            self.__var_fahrenheit = self__.self.var_celcius * (9/5) + 32
            #pressão:
            self.__var_pressure = self__.weather_data['main']['pressure']
            #humidade:
            self.__var_humidity = self__.weather_data['main']['humidity']
            #descrição:
            val_weather = self.__weather_data['main']['weather']
            self.__description = val_weather[0]['description']
        else:
            print(" City Not Found ")

    def change_city(self, new_city):
        self.__city = new_cityelse:
        self.request_data()

API = API()
