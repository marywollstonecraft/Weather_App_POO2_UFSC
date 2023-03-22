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
        self.__base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + self.__API_key + "&q=" + self.__city
        self.__weather_data = requests.get(self.__base_url).json()
        if self.__weather_data['cod'] == 200:
            #temperaturas medias:
            self.__var_kelvin = self.__weather_data['main']['temp']
            self.__var_celcius = self.__var_kelvin - 273.15
            self.__var_fahrenheit = self.__var_celcius * (9/5) + 32
            
            # sensacao de temperatura
            self.__var_feels_like_kelvin = self.__weather_data['main']['feels_like']
            self.__var_feels_like_celcius = self.__var_feels_like_kelvin - 273.15
            self.__var_feels_like_fahrenheit = self.__var_feels_like_celcius * (9/5) + 32
            
            #pressão:
            self.__var_pressure = self.__weather_data['main']['pressure']
            
            #humidade:
            self.__var_humidity = self.__weather_data['main']['humidity']
            
            #descrição:
            self.__var_condition = self.__weather_data['weather']['main']
            self.__description = self.__weather_data['weather'][0]['description']
            
            #vento:
            self.__var_wind = self.__weather_data['wind']['speed']
            
            # nivel do mar
            self.__var_sea_level = self.__weather_data['main']['sea_level']
            
            # altitute terrestre
            self.__var_grnd_level = self.__weather_data['main']['grnd_level']
            
            # nuvens
            self.__var_clouds = self.__weather_data['clouds']


        else:
            print(" City Not Found ")

    def change_city(self, new_city):
        self.__city = new_city

API = API()
