import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry('400x300')

#widgets
label1 = ttk.Label(window, text= 'Label1', background = 'green')
label2 = ttk.Label(window,text = 'Label2',background='red')

#layout
#   Essa aula foi para mostrar que a maneira que vc usa o Layout posicionando as widgets se sobrepõem
label1.pack()
label2.pack()

#run
window.mainloop()