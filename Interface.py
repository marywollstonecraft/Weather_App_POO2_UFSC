from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


class TELA_PRINCIPAL(Tk):
    def __init__(self):
        super().__init__()

        #configurando a janela principal
        self.geometry("1600x1000")
        self.resizable(False, False)
        self.title("Weather-App - UFSC POO2")
        self.iconbitmap = "images/icon.png"
        
        #background image
        self.bg_image = PhotoImage(file = 'images/background.png')
        self.label_bg = Label(self, image=self.bg_image)
        self.label_bg.place(x = 0, y = 0)

        #search area
        self.search_txt_label = Label(self, text='Digite a cidade:', font=('Helvetica', 30, 'bold'), fg='white', bg='#1ab5ef')
        self.search_txt_label.place(x=100, y=820)
        self.search_img = PhotoImage(file="images/searchbar.png")
        
        self.search_label = Label(image=self.search_img)
        self.search_label.place(x=100,y=870)
        self.search_txtfield = Entry(self, justify='center', width=10, font=("poppsins", 25, 'bold'), bg='white', border=0, fg='black')
        self.search_txtfield.place(x=110, y=890)
        self.search_txtfield.focus()

        #information keys
        inf_font = ('Helvetica', 30, 'bold')
        self.inf_temp = Label(self, text='Temperatura:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_feels_like = Label(self, text='Sensação térmica:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_wind = Label(self, text='Vel. Vento:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_humidity = Label(self, text='Umidade:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_pressure = Label(self, text='Pressão:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_sunrise_time = Label(self, text='Amanhecer:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_sunset_time = Label(self, text='Pôr do Sol:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_timezone = Label(self, text='Vel. Vento:', font=inf_font, fg='white', bg='#1ab5ef')
        
        #information keys plots
        self.inf_temp.place(x=70, y=70)
        self.inf_feels_like.place(x=70, y=140)
        self.inf_wind.place(x=70, y=210)
        self.inf_humidity.place(x=70, y=280)
        self.inf_pressure.place(x=70, y=350)
        self.inf_sunrise_time.place(x=70, y=420)
        self.inf_sunset_time.place(x=70, y=490)
        self.inf_timezone.place(x=70, y=560)

        # information variables 
        self.var_temp = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_feels_like = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_wind = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_humidity = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_pressure = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_sunrise_time = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_sunset_time = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_timezone = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        
        # information variables plots
        self.var_temp.place(x=330, y=70)
        self.var_feels_like.place(x=425, y=140)
        self.var_wind.place(x=280, y=210)
        self.var_wind.place(x=280, y=210)
        self.var_humidity.place(x=255, y=280)
        self.var_pressure.place(x=240, y=350)
        self.var_sunrise_time.place(x=305, y=420)
        self.var_sunset_time.place(x=290, y=490)
        self.var_timezone.place(x=280, y=560)

        def getWeather(self):
            city = textfield.get()
            geolocator = Nominatim(user_agent='geopiExercises')
            location= geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime('%I:%M %p')

w = TELA_PRINCIPAL()
w.mainloop()
