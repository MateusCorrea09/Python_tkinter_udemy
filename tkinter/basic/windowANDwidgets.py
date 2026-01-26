#tema da aula 'create a basic window with some widgets'
#   widgets são os elementos que compõem uma tela, sejam eles botões, caixas de texto, titulos,
#menus e entre outros elementos, segundo o professor compreender oq cada widget pode oferecer 
#e como usa-los é a chave para compreender qualquer framework.
#   A maior parte dos frameworks possue um certo grau de semelhança, mas cada um tem suas
#respectivas diferenças.

#   No Tkinter usamos dois tipos de widgets, os do tk widgets que são os originais e antigos
#e os do ttk que são os mais atuais e modernos.

#_________________________________________________________
#Primerio sempre se lembre de importar o tkinter
import tkinter as tk
from tkinter import ttk

def button_func():
    print('The button has pressed :D')
def hello_print():
    print('Hello :D')


#   assim como no projeto do Acelera que eu fiz (está no meu githhub 'Canguru') precisamos adicionar 
#características a uma determinada variavel para assim manipularmos elas da forma que desejamos.
#   Exemplo: criaremos uma variavel e instânciamos ele com as propriedades de tk.Tk(), esse 'TK' tem
#propriedades que colocamos dentro dessa variavel e assim conseguimos manipular elas :D

#Create a window
window = tk.Tk() #Precisamos dar 'run' nessa tela usando uma propriedade que agora ela possuí, através do método mainloop()

#   Em 'window' nós podemos acessar diversas características sejam elas de texto, titulo, eventos.... cores
#e entre outras.
window.title('Window and widgets') #através do método 'title' podemos mudar o titulo da janela
#   Experimente usar o '.' logo depois da variavel para visualizar os métodos dispooniveis e oq ele pode oferecer
window.geometry('800x500')

#Create widgets
#   Esse 'master' significa onde esse texto vai ficar aclopado ('de onde é sse widget?') com isso cominicamos que
# esse widget é um 'filho' de um outro elemento, que nos referimos a ele por 'master'. E usamos o 'pack()' para
#inicializarmos no topo e no centro da nossa aplicação, atenção... sem o 'pack()' não vai aparecer nada :D, é
#possivel custominar onde o widget será inciado, e isso se dá pelo argumento passado no 'pack()'
texto = tk.Text(master = window)
texto.pack()

#ttk
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#ttk buttom
button = tk.Button(master = window, text='Button', command = button_func)
button.pack()


##Exercício: criar mais uma label e um botão quando apertado diz 'hello' :D

label_2 = ttk.Label(master = window, text = 'Label :D')
label_2.pack()
button_2 = ttk.Button(master = window, text = ':D', command = hello_print)
button_2.pack()

#Run
#   Nós temos a nosa tela principal, e para dar inicio a ela e que através dela sejam posicionados widgets, precisamos
#usar um método dentro dela chamado mainloop(), esse método fica sempre atento as ações de eventos, sejam elas de clique
#ou marcações de texto e entre outras.

window.mainloop()

#Considerações!
#   importante lembrar que essa aula é introdutória e a base dela é entender quais tipos de widgets estão disponiveis
#para serem usados e que todos eles possuem varios parâmetros que podemos usar para c=personaliza-los a nossa escolha
#podemos acessar esses parâmetros passando o mause por cima dos parênteses.