import datetime as dt
import requests
import json

def get_data(CITY= 'London'):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = 'acccd88416ddb8b9bc489dfdb1ec2972'
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    data_json = requests.get(url).json()
    return data_json

def kelvin_to_celcius_fahrenheit(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit

class API:
    def __init__(self):
        self.weather_data = get_data()

        with open("weather_data.json", "w") as outfile:
            json.dump(self.weather_data, outfile)

        if self.weather_data['cod'] == 200:
            #temperaturas medias:
            self.var_kelvin = self.weather_data['main']['temp']
            self.var_celcius, self.var_fahrenheit = kelvin_to_celcius_fahrenheit(self.var_kelvin)

            # sensacao de temperatura
            self.var_feels_like_kelvin = self.weather_data['main']['feels_like']
            self.var_feels_like_celcius, self.var_feels_like_fahrenheit = kelvin_to_celcius_fahrenheit(self.var_feels_like_kelvin)
            
            #pressão:
            self.var_pressure = self.weather_data['main']['pressure']
            
            #humidade:
            self.var_humidity = self.weather_data['main']['humidity']
            
            #descrição:
            self.var_condition = self.weather_data['weather']['main']
            self.description = self.weather_data['weather'][0]['description']
            
            #vento:
            self.var_wind = self.weather_data['wind']['speed']
            
            # nivel do mar
            self.var_sea_level = self.weather_data['main']['sea_level']
            
            # altitute terrestre
            self.var_grnd_level = self.weather_data['main']['grnd_level']
            
            # nuvens
            self.var_clouds = self.weather_data['clouds']

            #horarios 
            self.sunrise_time = dt.datetime.utcfromtimestamp(self.weather_data['sys']['sunrise'] + self.weather_data['timezone'])
            self.sunset_time = dt.datetime.utcfromtimestamp(self.weather_data['sys']['sunset'] + self.weather_data['timezone'])


        else:
            print(" City Not Found ")

API = API()
