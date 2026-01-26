#   Na maioria dos casos nós temos 3 tipos de botões, os Buttons, Checkbuttonse os Radibuttons
#e para usa-los é necessário ter uma TKvariables

import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#buttons
def button_event():
    print('A basic button')
    print(radio_var.get())

button_string = tk.StringVar(value = 'A button with a string var')

#se nós deixarmos sem o 'master = ' e só atribuimos o 'window' ele sá o considera sendo o master.
button = ttk.Button(window, text='A simple button', command = button_event, textvariable = button_string)
button.pack()

#checkbutton, checkbotton não possuem 'textvariables' e sim apenas 'variable'
#check_var = tk.IntVar()
check_var = tk.IntVar(value = 10)
check1 = ttk.Checkbutton(window,
                        text='Checkbutton_1',
                        command = lambda: print(check_var.get()),
                        variable = check_var,
                        onvalue = 10,
                        offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(window,
                         text='Checkbox_2',
                         command = lambda: check_var.set(5))
check2.pack()

#radion buttons, importante destacar que se não colcoar nada em 'value' ele será iniciado com 0
radio_var = tk.StringVar()
radio1 =  ttk.Radiobutton(  window,
                            text= 'Radinbutton_1',
                            value = 1,
                            variable = radio_var,
                            command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window,
                         text = 'Radionbutton_2',
                         value = 1,
                         variable = radio_var)
radio2.pack()

#run
window.mainloop()