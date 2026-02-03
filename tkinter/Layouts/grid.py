import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.title('Grid')
window.geometry('600x400')

#widgets
label1 = ttk.Label(window, text='label_1', background = 'red')
label2 = ttk.Label(window, text='Label_2', background = 'blue')
label3 = ttk.Label(window, text='Label_3', background = 'green')
label4= ttk.Label(window, text='Label_4', background='yellow')
button1 = ttk.Button(window, text = 'button_1')
button2 = ttk.Button(window, text = 'button_2')
entry = ttk.Entry(window)

# define a grid
window.columnconfigure((0,1,2), weight = 1, uniform = 'a')
window.columnconfigure(3, weight = 2 ,uniform = 'a')
window.rowconfigure(0, weight = 1, uniform = 'a')
window.rowconfigure(1, weight = 1, uniform = 'a')
window.rowconfigure(2, weight = 1, uniform = 'a')
window.rowconfigure(3, weight = 3, uniform = 'a')

# place a widget -> nome_da_widget(linha = int, coluna = int)
label1.grid(row = 0, column = 0, sticky='nsew')

label2.grid(row = 1, column = 1,rowspan = 3, sticky='nsew')
label3.grid(row = 1, column = 0,columnspan = 3, sticky='nsew', padx = 20, pady = 10)
label4.grid(row = 3, column = 3, sticky = 'se')

#Exercício> reproduzir o restante do layout que o professor passou:
button1.grid(row = 0, column = 3, sticky='nsew')
button2.grid(row = 2, column = 2, sticky='nsew')
entry.grid(row=2, column=3, sticky='ew',rowspan=2,padx=35)


#run
window.mainloop()