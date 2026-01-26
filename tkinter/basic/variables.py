#   O uso de variaveis é oq faz os widgets comunicarem entre si! o tkinter possui uma boa
#comunicação com variaveis, isso significa que uma variável pode ser atualziada por um
#widget e um widget pode ser atualizado por uma variavel. Mas nesse momento vamos trabalhar
#apenas com variaveis simpels.
#   Um exemplo simples seria a relação dentre uma Entry e uma Label é o conteúdo que é 
#colocado dentro de uma entry (como uma entrada realizada pelo usuário) essa mesma entrada
#pode ser armazenada em uma variavel que logo em seguida atualiza o conteúdo da label.
#   Para esse exemplo vamos criar uma variavel que armazenará uma entrada do usuário
#e instantaneamente  atualiza o conteúdeo de uma label (em tempo real de digitação), dessa
#forma usaremos uma ferramenta de criação de variaveis do próprio framework, atenção para 
#parte de 'TKinter variables'

import tkinter as tk
from tkinter import ttk

def button_event():
    print(string_var.get())
    string_var.set('Button pressed')

#window
window = tk.Tk()
window.title('Test')
window.geometry('210x190')

#TKinter variables
string_var = tk.StringVar(value = 'Digite algo aqui!')
                            #Aqui acessamos uma ferramenta de criação de variaveis dentro do framework
                            #oq estamos fazendo é atribuindo uma série de caracteristicas pertencentes a
                            #'.StringVar()' e atribuindo essas mesmas a uma string que acabamos de criar
                            #e chamamos ela de 'string_var'
#string_var.initialize('Digite algo aqui!')

#   O que vaos fazer agora é usarmos um outro parâmetro disponivel, seria o 'textvariable' e a partir
#disso nós conseguiremos conectar a label e a entry a tarvés dessa variavel


#widgets
label = ttk.Label(master = window, text = 'TKinter variables',textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text='Button', command = button_event)
button.pack()

#run
window.mainloop()