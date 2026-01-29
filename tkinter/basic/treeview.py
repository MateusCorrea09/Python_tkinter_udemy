#Treeview
#   Me parece uma forma de construir tabelas a partir de listas

import tkinter as tk
from tkinter import ttk
from random import choice
#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

#data
first_name = ['Bob','Maria','Alex','James','Susan','Henry','Lisa','Anna','Lisa']
last_name = ['Smith','Brown','Wilson','Thomson','Cook','Tailor','Walker','Clark']

#treeview
#   Primeiro vamos criar uma variavel e atribuir a ela as características da widget treeview
#é importante resaltar que quando acessamos as propriedades de treeview elas se asemelham a elementos
#que encontramos em uma tabela como 'columns', entretanto... quando acessamos 'columns' é para dizer para
#a widget 'quantos elementos de colunas tem' :D e para dizer qual o nome desses elementos usamos o 'heading' como 'cabeçalho'
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
#   Aqui é mostrado como acessar uma determinada coluna criada, e dizer qual será o nome atribida a ela
table.heading('first', text = 'first_name')
table.heading('last', text = 'last_name')
table.heading('email', text = 'e-mail')
#   Aqui na criação da nossa tabela o professor pediu para colocarmos uns atribuitos de estilo, e ele irá explicar isso em outro momento
table.pack(fill = 'both', expand = True)

# insert values into a table
#   A estrutura de adição de valores na tabela se asemelha a algo assim, é importante lembrar de que 
#e o 'parent = " "' o professor disse que deixar vazio faz com que o paython entenda que vc quer atribuir
#esse novo valor a uma tabela principal, e como estamos trabalhando com apenas uma tabela, ela já é a nossa principal
# table.insert(parent = '', index = 0, values = ('john', 'Doe','johnDoe@rmail.com'))
#   Como estamos trabalhando com um volume grande de elementos podemos usar um lool para preencher toda a tabela
for i in range(100): #o professor sugeriu criarmos uma tabela com 100 valores
    #   Primeiro criaremos algumas variaveis locais dentro de cada loop para pegar um elemento das listas e atribuir a elas,
    #usademos a biblioteca 'random.choice' para fazer o python escolher um elemento das listas que criamos (de forma aleatória)
    first = choice(first_name)
    last = choice(last_name)
    #   Para o e-mail usaremos o f-string para juntar elementos
    email = f'{first}{last}@gmail.com'
    #   Agora juntamos isso tudo que criamos em uma variavel a ser atribuida na tabela
    data = (first, last, email)
    table.insert(parent = '', index = 0, values = data)

#Events :D
#   Esse event é pra te mostrar que podemos pegar os conteúdos da tabela e printa-los na tela, entretanto...
#se usarmos o print a baixo só irá mostrar o X=0 e Y=0, para capturarmos o conteúdeo precisamos usar o 'table.selection()'
#print(help(table.bind('<<TreeviewSelect>>', lambda event: print(event))))
#   É notável que o retorno se dá um numero que condiz com o espaço da memória cuja as informações dos itens da tabela estão
#armazenados, para reolver issso precisamos de uma função que nos retornará o que há nesse determinado endereço... que seria os itens :D
#print(help(table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))))

def item_select(qualquercoisa_que_vier):
    #print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])
def delete_items(qualquer_coisa_que_vier):
    for i in table.selection():
        table.delete(i)


table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)
#run
window.mainloop()