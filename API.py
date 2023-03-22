import requests

CITY = 'Manaus'
APIkey = 'acccd88416ddb8b9bc489dfdb1ec2972'

class API:
    def __init__(self, api, city):
        self.API_key = api
        self.city = city
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + self.API_key + "&q=" + self.city
        self.weather_data = requests.get(self.base_url).json()
        if self.weather_data['cod'] == 200:
            #temperaturas medias:
            self.var_kelvin = self.weather_data['main']['temp']
            self.var_celcius = self.var_kelvin - 273.15
            self.var_fahrenheit = self.var_celcius * (9/5) + 32

            # sensacao de temperatura
            self.var_feels_like_kelvin = self.weather_data['main']['feels_like']
            self.var_feels_like_celcius = self.var_feels_like_kelvin - 273.15
            self.var_feels_like_fahrenheit = self.var_feels_like_celcius * (9/5) + 32
            
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


        else:
            print(" City Not Found ")

    def change_city(self, new_city):
        self.city = new_city

API = API(APIkey, CITY)
