import datetime as dt
import requests
import json

class Api:
    def __init__(self, 
                 CITY= 'London',
                 METRICS= 'metric',
                 BASE_URL="http://api.openweathermap.org/data/2.5/weather?",
                 API= 'acccd88416ddb8b9bc489dfdb1ec2972'):

        self.BASE_URL = BASE_URL
        self.API_KEY = API
        self.CITY = CITY
        self.METRICS = METRICS
        url = self.BASE_URL + "appid=" + self.API_KEY + "&q=" + self.CITY + "&metrics=" + self.METRICS
        self.weather_data = requests.get(url, timeout=5).json()

        with open("data/weather_data.json", "w", encoding='UTF-8') as outfile:
            json.dump(self.weather_data, outfile)

        self.weather_data_request_sucess = self.weather_data['cod'] == 200

        if self.weather_data_request_sucess:
            self.var_icon = self.weather_data['weather'][0]['icon']
            self.var_temperature = self.weather_data['main']['temp']
            self.var_feels_like = self.weather_data['main']['feels_like']
            self.var_pressure = self.weather_data['main']['pressure']
            self.var_humidity = self.weather_data['main']['humidity']
            self.var_description = self.weather_data['weather'][0]['description']
            self.var_wind = self.weather_data['wind']['speed']
            self.var_clouds = self.weather_data['clouds']
            self.var_timezone = self.weather_data['timezone']
            self.var_sunrise_time = dt.datetime.utcfromtimestamp(self.weather_data['sys']['sunrise'] + self.var_timezone)
            self.var_sunset_time = dt.datetime.utcfromtimestamp(self.weather_data['sys']['sunset'] + self.var_timezone)

        else:
            print(" City Not Found ")
        
        def __str__(self):
            return f"""{self.CITY}
            {self.METRICS}
            {self.weather_data}"""
