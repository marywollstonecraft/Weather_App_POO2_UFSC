import datetime as dt
import requests
import json

class Api:
    def __init__(self, CITY= 'manaus', METRICS= 'metric'):
        #extraindo dados da API
        self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        self.API_KEY = 'acccd88416ddb8b9bc489dfdb1ec2972'
        url = self.BASE_URL + "appid=" + self.API_KEY + "&q=" + CITY + "&metrics=" + METRICS
        self.weather_data = requests.get(url, timeout=10).json()
        
        with open("data/weather_data.json", "w", encoding='UTF-8') as outfile:
            json.dump(self.weather_data, outfile)

        self.weather_data_request_sucess = self.weather_data['cod'] == 200

        if self.weather_data_request_sucess:

            self.var_temperature = self.weather_data['main']['temp']
            self.var_feels_like = self.weather_data['main']['feels_like']
            self.var_pressure = self.weather_data['main']['pressure']
            self.var_humidity = self.weather_data['main']['humidity']
            self.var_description = self.weather_data['weather'][0]['description']
            self.var_wind = self.weather_data['wind']['speed']
            self.var_clouds = self.weather_data['clouds']
            self.var_sunrise_time = dt.datetime.utcfromtimestamp(self.weather_data['sys']['sunrise'] + self.weather_data['timezone'])
            self.var_sunset_time = dt.datetime.utcfromtimestamp(self.weather_data['sys']['sunset'] + self.weather_data['timezone'])

        else:
            print(" City Not Found ")

api= Api()