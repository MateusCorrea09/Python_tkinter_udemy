import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):
        
        #main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(600,600)

        #widgets
        self.menu = Menu(self)
        self.main = Main(self)

        self.mainloop()

class Menu(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=0, y=0, relwidth= 0.3, relheight=1)

        self.create_widgets()
    def create_widgets(self):
         #Criando as widgets
         menu_button1 = ttk.Button(self, text= 'Button_1')
         menu_button2 = ttk.Button(self, text= 'Button_2')
         menu_button3 = ttk.Button(self, text= 'Button_3')

         menu_slide1 = ttk.Scale(self, orient='vertical')
         menu_slide2 = ttk.Scale(self, orient='vertical')
        
        #Esse caso do toggle é interessante porque ele é um widgets que agrupa widgets, então apenas ele
        # inicialemente é posicionado com 'self' os que ficam dentro dele tem seu maim posicionado nele, como 
        # se ele fosse uma âncora        
         toggle_frame = ttk.Frame(self)
         menu_toggle1 = ttk.Checkbutton(toggle_frame, text ='Check_1')
         menu_toggle2 = ttk.Checkbutton(toggle_frame, text = 'Check_2')

         entry = ttk.Entry(self)

            #create the grid
         self.columnconfigure((0,1,2), weight = 1, uniform='a')
         self.rowconfigure((0,1,2,3,4), weight = 1, uniform='a')
            #place the widgets

        #Aqui eu cometi um erro de erscrever a primeira linha e apenas dar controlc+xontrolv... e esqueci de mudar
        #os row e column... tenha atenção nisso :D porque as coisas só não vão aparecer na tela se vc errar
         menu_button1.grid(row = 0, column = 0, stick = 'nsew', columnspan = 2)
         menu_button2.grid(row = 0, column = 2, stick = 'nsew')
         menu_button3.grid(row = 1, column = 0, stick = 'nsew', columnspan = 3)

         menu_slide1.grid(row = 2, column = 0, rowspan = 2, stick = 'nswe', pady = 20)
         menu_slide2.grid(row = 2, column = 2, rowspan = 2, stick = 'nswe', pady = 20)

         toggle_frame.grid(row = 4, column = 0, columnspan = 3, stick = 'nsew')
         menu_toggle1.pack(side = 'left', expand = True)
         menu_toggle2.pack(side = 'left', expand = True)
            
class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #ttk.Label(self, background='red').pack(expand=True, fill='both')
        self.place(relx= 0.3, y = 0, relheight=1, relwidth=0.7)
        Entry(self, 'Entry_1','Button_1','green')
        Entry(self, 'Entry_2','Button_2','red')
        Entry(self, 'Entry_3','Button_3','blue')
        Entry(self, 'Entry_4','Button_4','orange')
        

class Entry(ttk.Frame):
    def __init__(self, parent, label_text, button_text, label_background):
        super(). __init__(parent)
        
        
        label = ttk.Label(self, text = label_text, background=label_background)
        button = ttk.Button(self, text=button_text)

        label.pack(expand = True, fill = 'both')
        button.pack(expand = True, fill = 'both', pady = 10)

        self.pack(side = 'left',expand=True, fill='both',padx=20, pady=20)

App('Class based app', (600,600))