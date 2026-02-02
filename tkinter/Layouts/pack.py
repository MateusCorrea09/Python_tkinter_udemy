# Início
#   O método .pack() posiciona elementos na tela, com base na ordem de chagada, ele posiciona
#esses respectivos elementos de forma a inicializarem no topo a té a base da aplicação, como
#uma pilha... só que de cabeça pra baixo. Com a primeira widget inicializada e posicionada no
#topo da aplicação e as seguintes após serem inciializadas com o '.pack()' elas sempre estarão
#a abaixo dela.
# Comandos básicos
#   No método 'pack()' temos alguns argumentos que podem ser passados com o objetivo de personalizar
#como essa respectiva widget será inicializada na nossa aplicação, esses métods possuem suas formas
#de serem incializados.
# side = 'left', 'right', 'top', 'bottom' esse é usado para posicionar uma widget em um canto da aplicação
# expand = True, Fals esse fetermina se a widget pode ocupar as áreas livres na vertical ou horiozontal
# fill  'x', 'y', 'both', 'None' determina o quanto de espaço a widget vai ocupar

import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.title('Pack')
window.geometry('400x600')

#run
label = ttk.Label(window, text = 'First label', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Last of the labels', background = 'green')
button = ttk.Button(window, text = 'Button')

#layout
#   side
#label.pack(side = 'top')
#label2.pack(side = 'top')
#label3.pack(side = 'top')
#button.pack(side = 'top')
#   expand
#   No tkinter existem dois tipos de espaço, o espaço que a widget pode ocupar e o que ela vai ocupar, o professor
#usou duas palavras em inglês que talvez faça mais sentido 'can' e 'will', apenas com o expand = False, ou default,
#a widget vai ser lavada a apenas ocupar o tamanho referênte ao seu conteúdo... no caso da label é apenas o texto dentro dela.
#   Quando determinados o side = 'top' nós organizamos as widgets em uma determinada direção, e isso significa que
#determianda widget com o expand só pode ocupar os pespaços referentes a altura de cima para baixo, quando definimos
#o side = left nós organizamos a nossa widget em uma direção e isso siginifica que essa só pode ocupar os espaços referentes
#a largura. Isso pode ser um pouco complicado explicar com código ou com palavras, mas no visual isso fica mais simples de se entender
#   tente executar o código abaixo e modifique o 'expand' para True ou False para visualizar o comportamento das widgets
#label.pack(side = 'top', expand= True)
#label2.pack(side = 'top', expand= False)
#label3.pack(side = 'top', expand= False)
#button.pack(side = 'top', expand= True)

# fill
#   Ter o expand = True não colcoa a eifget como ocupando todo o determiando espaço, mas dizendo que essa mesma pode ocupado, para
#visualizar isso podemos usar o 'fill' para dizer que essa determianda widget pode ocupar todo esse espaço.
#   Com o 'fill' nós devemos passar uma direção com X ou Y para determinar qual direção essa mesma irá ser preenchida, nós também
#podemos passar 'both' ou 'None' como forma de dizer que queremos que ambas as direções podem ser prenchidas ou nenhuma, de forma padrão
#a configuração do fill já vem como 'None'
#label.pack(side = 'top', expand= True, fill = 'both')
#label2.pack(side = 'top', expand= False)
#label3.pack(side = 'top', expand= False)
#button.pack(side = 'top', expand= True, fill = 'y')

#Exercício! recriar um layout que o professor passou
#label.pack(side = 'top', expand = False, fill = 'x')
#label2.pack(side = 'top', expand= True)
#label3.pack(side = 'top', expand= True, fill = 'both')
#button.pack(side = 'top', expand= False, fill = 'x')

# PAC, existem dois tipos de padding
#   O primerio se refere ao 'padx' e o 'pady' esse cria uma espaço em volta da wifget que não é visível
#   O segundo é o 'ipadx' e o 'ipady' esse cria um 'padding' dentro da widget, o que significa que movimentamos
#a widget dentro dela mesma.
#   O 'pady' e o 'padx' cria um espaço em volta da widget, enquando o 'ipad' expande o tamanho da widget criando um
#espaço a partir de dentro da widget.
#label.pack(side = 'top', expand = False, fill = 'x', ipady = 50, padx = 100)
#label2.pack(side = 'top', expand= True, fill = 'both')
#label3.pack(side = 'top', expand= True, fill = 'both')
#button.pack(side = 'top', expand= False, fill = 'x')

#   Nesse final de aula o professor explicou que a hierarquia dada pela ordem de inicialização determina o quanto
#de espaço a widget vai ter para organziar seus respectivos parâmetros. Isso significa que :D
#   Observe como a primeira label é incializada e é dada a ela a prioridade maior de expaço no eixo X
#e a partir disso, o tanto de espaço que as outras labels e o buttom ocupa no wixo X é dado pelo nº de caracteres
#que o label3 tem... isso siginfica que... a primeira label pegou todo o espaço que ela precisa já que ela é a prioridade
#e depois deixou o sificiente para que as outras que estão sendo inicialziadas no 'top' apenas oq elas precisam para
#comportadas na apicação.
#   O professor disse que isso é algo que você pode pensar na hora de organizar as widgets na sua aplicação, mas que
#quando você for as orgzanizar você vai usar um 'frame', não essa forma a abaixo:

#EXERCÍCIO: reproduzir um layout que o professor passou:
label.pack(side = 'top', expand = True, fill = 'both', pady = 10, padx = 10)
label2.pack(side = 'left', expand= True, fill = 'both')
label3.pack(side = 'top', expand= True, fill = 'both')
button.pack(side = 'top', expand= True, fill = 'both')


#run
window.mainloop()