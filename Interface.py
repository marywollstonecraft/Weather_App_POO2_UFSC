from tkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from City_Data import *
from tkinter.messagebox import showinfo

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

        self.search_buttom = Button(self, bd= 15, command=self.getWeather, background='black' )
        self.search_buttom.place(x=330, y= 880)
        
        #types selection
        self.metrics_list = ('metric', 'imperial', 'standard')
        self.value_inside = StringVar(self)
        self.value_inside.set("Select an Metric Type")
        self.option_metrics = OptionMenu(self, self.value_inside, self.metrics_list[0] *self.metrics_list)
        self.question_menu.place(x=500, y=940)

        #information keys
        inf_font = ('Helvetica', 30, 'bold')
        self.inf_clock = Label(self, font=inf_font, text='Current Time', fg='black', bg='#1ab5ef')
        self.inf_temp = Label(self, text='Temperatura:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_feels_like = Label(self, text='Sensação térmica:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_wind = Label(self, text='Vel. Vento:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_humidity = Label(self, text='Umidade:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_pressure = Label(self, text='Pressão:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_sunrise_time = Label(self, text='Amanhecer:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_sunset_time = Label(self, text='Pôr do Sol:', font=inf_font, fg='white', bg='#1ab5ef')
        self.inf_timezone = Label(self, text='Vel. Vento:', font=inf_font, fg='white', bg='#1ab5ef')
        
        #information keys plots
        self.inf_clock.place(x=500,y=900)
        self.inf_temp.place(x=70, y=70)
        self.inf_feels_like.place(x=70, y=140)
        self.inf_wind.place(x=70, y=210)
        self.inf_humidity.place(x=70, y=280)
        self.inf_pressure.place(x=70, y=350)
        self.inf_sunrise_time.place(x=70, y=420)
        self.inf_sunset_time.place(x=70, y=490)
        self.inf_timezone.place(x=70, y=560)

        # information variables 
        self.var_clock = Label(self, font=inf_font, text='city-clock', fg='black', bg='#1ab5ef')
        self.var_temp = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_feels_like = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_wind = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_humidity = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_pressure = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_sunrise_time = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_sunset_time = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        self.var_timezone = Label(self, text='...', font= inf_font, fg='black', bg='#1ab5ef')
        
        # information variables plots
        self.var_clock.place(x=770,y=900)
        self.var_temp.place(x=330, y=70)
        self.var_feels_like.place(x=425, y=140)
        self.var_wind.place(x=280, y=210)
        self.var_wind.place(x=280, y=210)
        self.var_humidity.place(x=255, y=280)
        self.var_pressure.place(x=240, y=350)
        self.var_sunrise_time.place(x=305, y=420)
        self.var_sunset_time.place(x=290, y=490)
        self.var_timezone.place(x=280, y=560)

    def option_changed(self):
        self.output_label['text'] = f'You selected: {self.option_var.get()}'

    def getWeather(self,METRICS='metric'):
        CITY = self.search_txtfield.get()
        METRICS = self.op
        print('city sucess')
        self.city_data = City_Data(CITY=CITY, METRICS=METRICS)
        print('city data  sucess')
        self.var_clock.config(text=current_time())
        print('var clock sucess 1')
        self.var_temp.config(text=self.city_data.var_temperature)
        print('var temp sucess 1')
        self.var_feels_like.config(text=self.city_data.var_feels_like)
        print('var feels like sucess 1')
        self.var_wind.config(text=self.city_data.var_wind)
        print('var wind like sucess 1')
        self.var_humidity.config(text=self.city_data.var_humidity)
        print('var humidity like sucess 1')
        self.var_pressure.config(text=self.city_data.var_pressure)
        print('var pressure like sucess 1')
        self.var_sunrise_time.config(text=self.city_data.var_sunrise_time)
        print('var sunrise like sucess 1')
        self.var_sunset_time.config(text=self.city_data.var_sunset_time)
        print('var sunset like sucess 1')
        self.var_timezone.config(text=self.city_data.var_timezone)
        print('var timezone like sucess 1')


    
