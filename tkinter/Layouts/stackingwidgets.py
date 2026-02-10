# Toda vez qye vc cria um widget ele instântaneamente é colocado acima do anterior
#é como se existisse uma hierarquia em relação a sobreposição de widgets
#   Podemos usar um métodeo dentro das widgests chamado lift() e lower() para alterar a 
#hierarquia das widgets
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Stacking order')
window.geometry('400x400')

label1 = ttk.Label(window, text='Label_1', background='green')
label2 = ttk.Label(window, text='Label_2',background='red')
label3 = ttk.Label(window, text='Label_3', background='blue')

button1 = ttk.Button(window, text='Raize_label_1', command= lambda: label1.tkraise())
button2 = ttk.Button(window, text= 'Raize_label_2', command= lambda: label2.tkraise())
button3 = ttk.Button(window, text='Raize_label3', command= lambda: label3.tkraise())

label1.place(x = 50, y = 100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=180, y=90, width=240, height=100)

button1.place(rely= 1, relx=0.8, anchor='se')
button2.place(rely=1, relx=1, anchor='se')
button3.place(rely=1, relx=0.6, anchor='se')

window.mainloop()