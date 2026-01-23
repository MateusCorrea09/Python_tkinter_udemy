# widget 'componentes' como botões e caixas de texto
#loyout 'distribuição e posicionamento' como as coisas vão ficar na tela
#style o design e visual das aplicações ou IU

import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    #print(entry_Int.get())
    miles_input = entry_Int.get()
    kminput = miles_input * 1.61
    output_String.set(kminput)
#window
#window = tk.Tk()
window = ttk.Window(themename='journal')
window.title('Demo')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text= 'Miler to kilometers', font='Calibre 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_Int = tk.IntVar()
entry = ttk.Entry(
    master= input_frame,
    textvariable = entry_Int
    )
buttom = ttk.Button(
    master = input_frame,
    text= 'Convert',
    command= convert
    )
entry.pack(
    side='left',
    padx=10
    )
buttom.pack(
    side='left'
    )
input_frame.pack(
    pady = 10
    ) 

#output
output_String = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text=':D',font='Calibre 12',
    textvariable = output_String
    )
output_label.pack(
    pady= 5
    )
#run
window.mainloop()