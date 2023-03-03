from API import API

class WeatherApp(App):
    def buld(self):
        return GUI

class MyWidget(Widget):
    def build(self):
        return MyWidget()


if __name__ == "__main__":
    GUI = Builder.load_file('Interface.kv')
    WeatherApp().run()
    WidgetApp().run()