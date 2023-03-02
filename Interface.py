from kivy.app import App
from kivy.lang import Builder
from API import API

GUI = Builder.load_file('Interface.kv')

class WeatherApp(App):
    def buld(self):
        return GUI

    




WeatherApp().run()