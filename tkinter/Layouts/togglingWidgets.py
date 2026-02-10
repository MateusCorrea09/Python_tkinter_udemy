#   Segundo o professor no tkinter você não consegue esconder ou trocar
#a visibilidade de widgets, você apenas as posiciona ou as remove, assim como 
#os métodos de posicionamento de widgets como place, grid e pack, temos métodos
#que removem as widgets da tela.

import tkinter as tk
from tkinter import ttk
    

window = tk.Tk()
window.geometry('600x400')
window.title('Hide widgets')

# place
#def toggle_label_place():
#    global label_visibile
#    if label_visibile:
#        label.place_forget()
#        label_visibile = False
#    else:
#        label_visibile = True
#        label.place(relx = 0.5, rely=0.5, anchor='center')

#button = ttk.Button(window, text='Toggle label', command= toggle_label_place)
#button.place(relx=0.4, rely=0.9)

#label_visibile = True
#label = ttk.Label(window, text='A_label')
#label.place(relx = 0.5, rely=0.5, anchor='center')

# grid
#window.columnconfigure((0,1), weight=1, uniform='a')
#window.rowconfigure(0, weight=1, uniform='a')

#def toggle_label_grid():
#    global label_visibile
#    if label_visibile:
#        label.grid_forget()
#        label_visibile = False
#    else:
#        label.grid(column= 1, row=0)
#        label_visibile = True

#button = ttk.Button(window, text='Toggle label', command= toggle_label_grid)
#button.grid(column= 0, row=0)

#label_visibile = True
#label = ttk.Label(window, text='A_label')
#label.grid(column= 1, row=0)

# pack
def toggle_label_pack():
    global label_visibile
    if label_visibile:
        label.pack_forget()
        label_visibile = False
    else:
        label.pack(expand= True)
        label_visibile = True

label_visibile = True
label = ttk.Label(window, text='A_label')
label.pack(expand= True)

button = ttk.Button(window, text='Toggle label', command= toggle_label_pack)
button.pack(side='bottom')

window.mainloop()