#Combobox and Spinbox

#   Combobox e SpininBox são widgets que são conectadas a um tipo de lisa, e essas
#listas podem ser a base para que um usuário possa selecionar um dos elementos dessa lista
#e podemos usar uma tkinter_variable para armazenar um elemento selecionado pelo usuário

import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')


#widgets


#combobox
#   Primeiro precisamos criar um tipo de listas com as 'opções' ou 'Alternativas' que teriam
#nesse combobox!
itens = ('Sorvete', 'Pizza', 'Brocolis')
#   Depois de criar uma lista, precisamos criar uma variavel que ficará responsável por deter 
#as características de 'combobox' essas características que estão na biblioteca ttk (porque é um widget)
#   Podemos armazenar uma selecção de item feita pelo usuário  armazenando dentro de uma string_var
food_string = tk.StringVar(value = itens[0])
combo = ttk.Combobox(window, textvariable = food_string) #Lembrar sempre de atribuir a variavel a uma 'master'
#   Depois precisamos acessar uma das características dessa variavel, que seria a de atribuir uma lista a ela
combo['values'] = itens #Uma escrita alternativa a essa é 'combo.configure(values = itens)'
combo.pack()

#Mostrando oq ta selecionado
txt_label = ttk.Label(window, text = 'Selecione uma comida', font='12px', padding= 12)
txt_label.pack()

#Events for a combobox
combo.bind('<<ComboboxSelected>>', lambda event: txt_label.config(text = f'Comida selecionada: {food_string.get()}'))

#SpinBox
#   Vendo o professor falar sobre a SpinBox é perceptivel que ela é bem similar a ComboBox, mas tem uma caraterística que
#me chamou a atenção! ela tem dois botões que servem como controle de estado, ao apertar o botão com seta para cima
# o seletor sobe um valor a cima para lista e o inverso ocorre quando usamos o botão com a seta para baixo.
# isso significa que esse botão captura a interação do usuário e interage com a lista de valores que está conectada a SpinBox

spin_int = tk.IntVar(value = 3)
spin = ttk.Spinbox(
    window,
    from_ = 5, #Aqui é importante lembrar que é um método que faz com que os números começam a a partir de e isso se dá pelo comando 'from_'
    to = 20,
    increment = 2, #isso aki é tipo um loop de for básico
    command = lambda: print(spin_int.get()),
    textvariable = spin_int
)
#Essa parte de baixo é para mostrar que é possível ter acesso ao evento que os botões capturam
spin.bind('<<Increment>>', lambda event: print('Up'))
spin.bind('<<Decrement>>', lambda event: print('Down'))
spin.pack()

#Exercício: Criar uma SpinBox que tenha os valores 'A,B,C,D,E'
spin_values = ('A','B','C','D','E',)
spin_letras_start = tk.StringVar(value = spin_values[0])
spin_letras = ttk.Spinbox(
    window,
    textvariable = spin_letras_start,
)
spin_letras['values'] = spin_values
spin_letras.bind('<<Increment>>', lambda event: print(spin_letras_start.get())) #Eu não entendi o porque da spin o print ser meio lagado ???  tem um lag no print
spin_letras.bind('<<Decrement>>', lambda event: print(spin_letras_start.get()))
spin_letras.pack()
#run
window.mainloop()