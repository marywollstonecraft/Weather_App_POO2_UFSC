import datetime as dt
import requests
import json
from Api import *
class City_Data:
    def __init__(self, CITY='London', METRICS='metric'):
        Api.request_weather_data(CITY=CITY, METRICS=METRICS)
        self.weather_data = Api.get_data()

        if  self.weather_data['cod'] == 200:
            self.var_lon = self.weather_data['coord']['lon']
            self.var_lat = self.weather_data['coord']['lat']

            self.var_city = self.weather_data['name']
            self.var_flag = self.weather_data['sys']['country']
            self.var_main = self.weather_data['weather'][0]['main']
            self.var_description = self.weather_data['weather'][0]['description']
            self.var_icon = self.weather_data['weather'][0]['icon']

            self.var_temperature = self.weather_data['main']['temp']
            self.var_temperature_min = self.weather_data['main']['temp_min']
            self.var_temperature_max = self.weather_data['main']['temp_max']
            self.var_feels_like = self.weather_data['main']['feels_like']
            self.var_pressure = self.weather_data['main']['pressure']
            self.var_humidity = self.weather_data['main']['humidity']

            self.var_wind = self.weather_data['wind']['speed']
            self.var_clouds = self.weather_data['clouds']['all']
            self.var_timezone = self.weather_data['timezone']
            self.var_sunrise_time = dt.datetime.utcfromtimestamp(self.weather_data['sys']['sunrise'] + self.var_timezone)
            self.var_sunset_time = dt.datetime.utcfromtimestamp(self.weather_data['sys']['sunset'] + self.var_timezone)

        else:
            print(" City Not Found ")

    def __str__(self):
                return f"""{self.var_city}, {self.var_flag}
                {self.var_temperature}
                {self.var_main}, {self.var_description}"""

