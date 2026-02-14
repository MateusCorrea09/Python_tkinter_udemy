import tkinter as tk
from tkinter import ttk

def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(master =  parent)

    #grid layout
    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')

    #widgets
    ttk.Label(frame, text= label_text).grid(row =0,  column=0, sticky='nswe')
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky='nsew')

    return frame

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(master = parent)

        #grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform= 'a')
        #widgets
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')
        
        #posicionando a caixa qeu criamos no exercício
        self.create_exercise_box('Exercício').grid(row =0, column = 2, stick = 'nsew')
        
        #place method :D
        self.pack(expand=True, fill='both',padx=10, pady=10)
        #exercício, eu cometi um erro de identação aki... se vc perceber o 'exercício' com '#' ficou dntro do método acima, eometi esse erro e fiquei um bom tempo tentando entender porque
        #o método que eu criei estava inacessível..... :D só percebi o erro depois que joguei na ia (depois de ficar uns bonms 10nm olhando pra tela), se essa línguagem tivesse '{}' como identação
        # eu n teria cometido esse erro bobo.... mas aki a identação é perfeita né ?????? :D 
        
    def create_exercise_box(self, text):
        frame = ttk.Frame(master= self)
        ttk.Entry(frame).pack(expand=True, fill='both')
        ttk.Button(frame,text=text).pack(expand=True, fill='both')
        return frame

#window
window = tk.Tk()
window.title('Widgets and return')
window.geometry('400x600')

# Criando um layout a partir de classes:
Segment(window, 'label', 'button')
Segment(window, 'test', 'Click')
Segment(window, 'Hello', 'Test :D')
Segment(window, 'He', 'Test :D')
Segment(window, 'By', 'Test :D')
Segment(window, ':D', 'Test :D')

#Criando um layout a partir de uma função
#create_segment(window, 'label', 'button').pack(expand=True, fill='both', padx=10, pady=10)
#create_segment(window, 'test', 'Click').pack(expand=True, fill='both', padx=10, pady=10)
#create_segment(window, 'Hello', 'Test :D').pack(expand=True, fill='both', padx=10, pady=10)
#create_segment(window, 'He', 'Test :D').pack(expand=True, fill='both', padx=10, pady=10)
#create_segment(window, 'By', 'Test :D').pack(expand=True, fill='both', padx=10, pady=10)
#create_segment(window, ':D', 'Test :D').pack(expand=True, fill='both', padx=10, pady=10)

#run
window.mainloop()