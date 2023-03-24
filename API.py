import requests
import json

class API:
    def __init__(self, city= 'London'):
        self.__city = city
        self.__base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.__api_key = 'acccd88416ddb8b9bc489dfdb1ec2972'
        self.__url = self.__base_url + "appid=" + self.__api_key + "&q=" + self.__city
        self.weather_data = requests.get(self.__url).json()

        with open("weather_data.json", "w") as outfile:
            json.dump(self.weather_data, outfile)


