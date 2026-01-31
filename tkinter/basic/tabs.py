#   Tabs são usadas para criar sessões, em que cada sessão agrupa uma quantidade
#de elementos, e podem ser acessadas a partir de uma barra posicionada em alguma
#extremidade da tela.
#   Será como um grupo de frames conectados a uma tela.
import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Tab Widget')

# Notebook widget
#   Assim como um caderno de 10 matérias que agrupa um um número de máterias, nós
#usaremos uma widget de ttk chamada 'notebook' ela nos permitirá agregar um número
#'x' de 'frames' dentro do notebook, como se estivessemos adicionando as máterias
#dentro do caderno.
notebook = ttk.Notebook(window)
#   Aqui começamos a criar os frames que serão agregados ao Notebook
tab1 = ttk.Frame(notebook) # Na 'master' colocamos o notebook, ao invés do window
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
#   Até então as 'tabs' não estão visíveis, para tornamos elas visíveis precisamos de um comando
#do notebook chamado 'add', assim como um tipo de dado composto, criamos os espaços e agora precisamos
#atribuir um conteúdo a esses espaços.
notebook.add(tab1, text = 'Tab 1')
txt_label = ttk.Label(tab1, text = 'Label do tab1')
txt_label.pack()
btb_button = ttk.Button(tab1, text = 'Button1')
btb_button.pack()

notebook.add(tab2, text = 'Tab 2')
txt_label1 = ttk.Label(tab2, text = 'Label do tab 2')
txt_label1.pack()
entry = ttk.Entry(tab2)
entry.pack()

notebook.add(tab3, text = 'Tab EXR')
btb_button3 = ttk.Button(tab3, text = 'Buton_3')
btb_button3.pack()
btb_button4 = ttk.Button(tab3, text = 'Button_4')
btb_button4.pack()
lbl_label = ttk.Label(tab3, text = 'Essa parte faz parte do exercício :D')
lbl_label.pack()
notebook.pack()
#run
window.mainloop()