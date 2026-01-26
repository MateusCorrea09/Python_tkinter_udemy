#   Existem duas formas de pegar as entradas e interações do usuário, uma delas é atribuir uma variavel do tkinter 
#mas isso será tratato ao decorrer do curso (como o professor disse), então vamos agora ver como usar o '.get()'

import tkinter as tk
from tkinter import ttk

def button_func():
    #get the content of th entry
    #print(entry.get()) #Aqui printa no terminal o conteúdo dentro de 'entry'
    #é importante ter em mente que só é possível conseguir usar o get() a partir de um Entry(), pelo menos até os
    #widgets que temos até então :D se vc tentar usar um get() em uma .Label() vai resultar em um erro

    #   Todo widget do TKinter possuí uma configuração, e podemos usar essa mesma para modifica-lo a partir da nossa
    #vontade. Usaremos o .config() para isso
    #Update the label
    #label.config(text='Some other text')
    #   Podemos usar esse meio mais moderno apra acessar o atributo de texto da variavel que possúi as características
    #de uma label e modifica-la.
    #label['text'] = 'Some other text'

    #Agora oq faremos é pegar oq está dentro de entry.get() e armazena-la dentro da label!
    #Para isso vamos pegar o texto usando o .get() e armazenar dentro de uma variavel local
    entry_text = entry.get() #importante lembrar que sempre retorna uma string
    #agora acessamos a label (a variavel que criamos) e mudamos sua propriedade de texto para oq a entry_text tem
    label['text'] = entry_text

def button_reset():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

#window
window = tk.Tk()
window.title('Getting and Setting widgets')

#widgets

label = ttk.Label(master=window, text='Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text='Button', command = button_func)
button.pack()

#Exercício: criar um novo botão que deve retornar o texto do label para 'some text' e deixar a entry enable
button_2 = ttk.Button(master = window, text = 'Reset',command = button_reset)
button_2.pack()
#run
window.mainloop()