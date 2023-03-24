import json
import datetime as dt

WEATHER_DATA = json.load(open('weather_data.json'))
class CITY:
    def __init__(self, data=WEATHER_DATA):
        self.weather_data = data
        # o codigo 200 apresenta confirmação que a cidade contém nos dados
        if self.weather_data['cod'] == 200:

            # --------------descricoes gerais---------- #
            geral_description = self.weather_data['weather'][0]
            # ---------------------------------------- #
            #id
            self.weather_id = geral_description['main']
            # condicao
            self.condition = geral_description['main']
            # sobre a condicao climatica
            self.description = geral_description['description']
            # icone
            self.icon = geral_description['icon']

            # --------------descricoes---------------- #
            weather_description = self.weather_data['main']
            # ---------------------------------------- #
            #temperatura:
            self.var_temp_kelvin = weather_description['temp']
            self.var_temp_celcius = kelvin_to_celcius(self.var_temp_kelvin)
            self.temp_var_fahrenheit = celcius_to_fahrenheit(self.var_temp_celcius)
            # sensacao de temperatura
            self.var_feels_like_kelvin = weather_description['feels_like']
            self.var_feels_like_celcius = kelvin_to_celcius(self.var_feels_like_kelvin)
            self.var_feels_like_fahrenheit = celcius_to_fahrenheit(self.var_feels_like_celcius)
            #temperaturas maximas e minimas
            self.var_temp_min_kelvin = weather_description['temp_min']
            self.var_temp_max_kelvin = weather_description['temp_max']
            self.var_temp_min_celcius = kelvin_to_celcius(self.var_temp_min_kelvin)
            self.var_temp_max_celcius = kelvin_to_celcius(self.var_temp_max_kelvin)
            self.var_temp_max_fahrenheit = celcius_to_fahrenheit(self.var_temp_max_celcius)
            self.var_temp_min_fahrenheit = celcius_to_fahrenheit(self.var_temp_min_celcius)
            # pressão e umidade:
            self.var_pressure = weather_description['pressure']
            self.var_humidity = weather_description['humidity']
            # vento:
            self.var_wind_speed = self.weather_data['wind']['speed']
            # horarios
            self.sunrise_time = dt.datetime.utcfromtimestamp(
            self.weather_data['sys']['sunrise'] + self.weather_data['timezone'])
            self.sunset_time = dt.datetime.utcfromtimestamp(
            self.weather_data['sys']['sunset'] + self.weather_data['timezone'])

        else:
            print(" City Not Found ")

    def kelvin_to_celcius(self, kelvin):
        celcius = kelvin - 273.15
        return celcius

    def celcius_to_fahrenheit(self, celcius):
        fahrenheit = celcius * (9 / 5) + 32
        return fahrenheit

