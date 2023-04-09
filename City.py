from API import Api

class City(Api):
    def __init__(self):
        super().__init__()
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
                {self.var_temperature}
                {self.var_description}"""
            