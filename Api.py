import json
import requests
import os

class Api:
    def __init__(self):

        self.__BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        self.__API_KEY = 'acccd88416ddb8b9bc489dfdb1ec2972'

    def __write_json(self, weather_data):
        if os.path.exists("data/weather_data.json"):
                os.remove("data/weather_data.json")

        with open("data/weather_data.json", "w", encoding='UTF-8') as outfile:
            json.dump(weather_data, outfile)

    def request_weather_data(self, CITY='London', METRICS='metric'):
        try:
            url = self.__BASE_URL + "appid=" + self.__API_KEY + "&q=" + CITY + "&units=" + METRICS
            self.__weather_data = requests.get(url, timeout=11).json()
        except:
            self.__weather_data = json.dumps(dict())
            
            print("Request Error")
        self.__write_json(self.__weather_data)
    
    def get_data(self):
        if os.path.exists('data/weather_data.json'):
            with open('data/weather_data.json') as datafile:
                return datafile.read()
        else:
            new_json = json.dumps(dict())
            return new_json
    
