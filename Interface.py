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
        
        #information area
        self.inf_temp = Label(self, text='Temperatura:', font=('Helvetica', 30, 'bold'), fg='white', bg='#1ab5ef')
        self.inf_temp.place(x=70, y=70)

        self.inf_feels_like = Label(self, text='Sensação térmica:', font=('Helvetica', 30, 'bold'), fg='white', bg='#1ab5ef')
        self.inf_feels_like.place(x=70, y=140)

        self.inf_wind = Label(self, text='Vel. Vento:', font=('Helvetica', 30, 'bold'), fg='white', bg='#1ab5ef')
        self.inf_wind.place(x=70, y=210)

        self.inf_humidity = Label(self, text='Umidade:', font=('Helvetica', 30, 'bold'), fg='white', bg='#1ab5ef')
        self.inf_humidity.place(x=70, y=280)

        self.inf_pressure = Label(self, text='Pressão:', font=('Helvetica', 30, 'bold'), fg='white', bg='#1ab5ef')
        self.inf_pressure.place(x=70, y=350)

        self.inf_sunrise_time = Label(self, text='Amanhecer:', font=('Helvetica', 30, 'bold'), fg='white', bg='#1ab5ef')
        self.inf_sunrise_time.place(x=70, y=420)

        self.inf_sunset_time = Label(self, text='Pôr do Sol:', font=('Helvetica', 30, 'bold'), fg='white', bg='#1ab5ef')
        self.inf_sunset_time.place(x=70, y=490)

        self.inf_timezone = Label(self, text='Vel. Vento:', font=('Helvetica', 30, 'bold'), fg='white', bg='#1ab5ef')
        self.inf_timezone.place(x=70, y=560)


    def pesquisar(self):
        pass

w = TELA_PRINCIPAL()
w.mainloop()
