from tkinter import *
class TELA_PRINCIPAL(Tk):
    def __init__(self):
        super().__init__()
        #configurando a janela principal
        self.geometry("600x600")
        self.resizable(True, True)
        self.title("Weather-App - UFSC POO2")
        #background image
        self.bg_image = PhotoImage(file = 'images/png/background.png')
        self.label_bg = Label(self, image=self.bg_image)
        self.label_bg.place(x = 0, y = 0)
        #configurando botoes
        self.b_search = Button(self)
        self.b_search['command'] = self.pesquisar
        #configurando input da pesquisa
        self.e_search = Entry(self)
    def pesquisar(self):
        pass

w = TELA_PRINCIPAL()
w.mainloop()