#funções com argumentos em um botão
#   Para conseguir usar uma função que tem argumentos em um botão é necessário usar 'lambda',
#através dela é possível usar uma função que possuí um argumento, exemplo:
#comman = lambda: print('Hello!'), aqui nós estamos usando o lambda para usar a função print
# e que ela possuí um argumento sendo passada.

import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('The button was pressed')
    print(entry_string.get())

#window
window = tk.Tk()
#window.geometry('240x77')
window.title('Argument in function with buttons')


#widgets

entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

button = ttk.Button(window, text = 'Button', command = lambda: button_func(entry_string))
button.pack()

#run
window.mainloop()