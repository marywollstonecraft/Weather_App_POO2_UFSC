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

    def __str__(self):
                return f"""{self.CITY}
                {self.METRICS}
                {self.weather_data}"""

