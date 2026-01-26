#Criar duas entry e uma label que sejam conectadas a uma stringvar
import tkinter as tk
from tkinter import ttk

def button_event():
    print(string_var.get())
    string_var.set('Button pressed')

#window
janela = tk.Tk()
janela.title('Exercício :D')
janela.geometry('290x180')

#TKinter variables
string_var = tk.StringVar()

#widgets
entrada = ttk.Entry(master = janela, textvariable = string_var)
entrada.pack()
entrada2 = ttk.Entry(master = janela, textvariable = string_var)
entrada2.pack()

label = ttk.Label(master = janela, textvariable = string_var)
label.pack()

botao = ttk.Button(master = janela, text = 'button', command = button_event )
botao.pack()

#run
janela.mainloop()
#Terminei :D