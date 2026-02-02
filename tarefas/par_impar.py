import tkinter as tk
from tkinter import ttk

def valida_entrada(x):
    #print(x.get())
    entrada = x.get()
    if entrada % 2 == 0:
        entrada_string.set(value = 'É par')
    if entrada % 2 != 0:
        entrada_string.set(value = 'É ímpar')

#setup
window = tk.Tk()
window.title('É impar?')
window.geometry('600x400')

#grid
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 2)
window.rowconfigure(0,weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)


entrada_string = tk.StringVar(value = 'Aguardando entrada')
resultado_int = tk.IntVar()
##Aqui coloca pra inicializar no centro
##

#widgets
label = ttk.Label(window, text = 'Entre com um valor', 
                  font = 'Calibre 24 bold')
label.grid(row = 0, column = 0)

entry = ttk.Entry(window, textvariable = resultado_int)
entry.grid(row = 1, column = 0)

buttom = ttk.Button(window, 
                    text = 'Verificar', 
                    command = lambda :  valida_entrada(resultado_int))
buttom.grid(row = 2, column = 0)

label_resposta = ttk.Label(window, 
                           text='Aguardando_entrada', 
                           textvariable = entrada_string, 
                           background = 'red',
                           font = 'calibre 24 ',
                           foreground = 'orange')

#label_resposta.pack(side= 'left', expand= True, fill = 'both', padx = 10, pady = 10)
label_resposta.grid(row = 0, column = 1, rowspan = 2)
#run
window.mainloop()