# frames + pack
#   Combinar frames e packs são uma ótima forma de conseguir construir bons layouts, a partir da união
#dessas duas ferramentas é possível conseguir posicionar widgets, através do pack(), em direções
#diferentes, e até mesmo poscionar frames dentro de outros frames e criar organizações de elementos
#mais dinâmicas.

import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

#top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'First label', background='red')
label2 = ttk.Label(top_frame, text = 'Label 2', background='blue')

#middle widget
label3 = ttk.Label(window, text = 'Another label', background='green')

#buttom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text = 'Last of labels', background='orange')
button1 = ttk.Button(bottom_frame, text = 'A Button')
button2 = ttk.Button(bottom_frame, text = 'Another Button')

#__LAYOUT__
#top layout
label1.pack(side='left',fill = 'both', expand=True)
label2.pack(side='left',fill = 'both', expand=True)
top_frame.pack(fill='both', expand=True)

#middle layout
label3.pack(expand=True)

#bottom layout
button1.pack(side='left', expand=True, fill='both')
label4.pack(side='left',expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')
bottom_frame.pack(expand = True, fill = 'both', padx = 20, pady = 20)

# Exercício: criar um frame dentro do bottom frame e adicioanr 3 botttons organizados
#de cima para baixo (vertical)
final_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(final_frame, text = 'button_exercício')
button4 = ttk.Button(final_frame, text = 'button_exercício')
button5 = ttk.Button(final_frame, text='button_exercício')

final_frame.pack(side='left',expand=True,fill='both')
button3.pack(side='top',expand=True, fill= 'both')
button4.pack(side='top',expand=True, fill = 'both')
button5.pack(side='top', expand = True, fill = 'both')
#run
window.mainloop()