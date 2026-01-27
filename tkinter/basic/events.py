#Let's talk about events binding! (to treinando meu inglês :D)
#   O que o professor falou no início da aula se trata de uma comversa inicial sobre eventos
#me lembro que na aula de engenharia de software o professor falaou na sala sobre 'tringgers'
#que se trata de algo que acontece depois de um certo 'evento' ou 'gatilho' ativado a partir
#da interação do usuário que ocasiona em uma mudança de estrado.
#   Algo que eiu entendi sobre a explicação do professor do curso é que existe diversos tipos
#de eventos que realizam diversas mudnças no visual no GUI ou podem mudar o estado dos componenetes
#ou conteúdo das variaveis, e esses eventos estão 'bind' ou 'conectados' a widgts

import tkinter as tk
from tkinter import ttk

def get_pos(event):
    #oq acontece é que esse 'event' me retorna uma série de informações, mas eu só
    #quero saber a informaçãop do x e do y, onde a posição do mouse se encontra na tela
    #por isso escrevi 'event.x' e 'event.y'
    print(f'x: {event.x} y: {event.y}')

#window
window = tk.Tk()
window.geometry('600x500')
window.title('Event binding')

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()


#Events
#   É importante entender que inciialmente existem 3 detalhes importantes para
#se ter em mente quando falamos sobre eventos 'modifer-type-detail'
#window.bind('<modifer-type-detrail>', lambda: print('an event'))
#   Nota-se de que esta passado por uma string e <...> entre essa string, logo em
#seguida usamos a lambda: para usar uma função de print. Outro detalhe importante
#sobre oq foi escrito, é que 'window' se refere a 'master' onde o evento será capturado.

#Aqui passamos o comando que deve ser realizado como 'trigguer' para realização da função
#window.bind('<Alt-KeyPress-a>',lambda:print('An event'))
#se executarmos com o texto acima vamos obter o seguinte erro no terminal:
#TypeError: <lambda>() takes 0 positional arguments but 1 was given
#   Quando isso aocntece é basicamente o TKinter colocando automaticamente um argumento
#na função, e para não ocorrer um erro nós devemos 'CAPTURA-LO' (isso me pareceu um pouco confuso)
#para isso ocorrer devemos passar como argumento 'event' depois de labda
window.bind('<Alt-KeyPress-a>',lambda event : print('An event'))
#podemos captura-lo e demonstrar oq estamos capturando na realidade, é uma sequência
#de informações que estão relacionadas ao evento:
window.bind('<Alt-KeyPress-a>',lambda event : print(event))
#site muit bom com muitos tutoriais recomendados pelo professor: https://www.pythontutorial.net/tkinter/tkinter-event-binding/

#Com o evento abaixo nós capturamos a posição X e Y do mouse em toda nossa janela (a master)
#window.bind('<Motion>', get_pos)
#podemos específica em um widget específico também
text.bind('<Motion>', get_pos)

#   Importante dizer que as vezes não é necessário escrever todo <Alt-KeyPress-a> e sim apanas uma parte
#nesse código toda vez que um botão for apertado será printado no terminal a mensagem
#window.bind('<KeyPress>', lambda event: print('A button was pressed'))
#   É possível ter um print no terminal mais elaborado se acessarmos os conteúdos dentro de 'event' que está
#sendo capturado pelo 'bind' e dentro desse 'event' printarmos no terminal não o print('A button was pressed')
#e sim printar o botão que está sendo pressionado, para isso usamos o 'event.char' em uma f-string
window.bind('<KeyPress>',lambda event: print(f'a button was pressed({event.char})'))

#   Um outro evento que o prefessor gostaria de falar na aula é sobre o 'FocusIn' que se trata
#de printar no terminal quando a entry for selecionada, seria tipo para saber quando essa widget
#está sendo usada/selecionada pelo usuário
entry.bind('<FocusIn>', lambda event: print('The entry was select'))
entry.bind('<FocusOut>', lambda event: print('The entry was unselect'))


#Exercício: entrar no site e procurar uma forma de pritnar na tela quando o shift esta sendo usado e em conjunto com o mousewheel
text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

#run
window.mainloop()