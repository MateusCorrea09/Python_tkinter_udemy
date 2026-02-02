# Layouts
#   Layouts são fundamentais em qualquer freamework e é através deles que conseguimos
#posicionar elementos na tela de forma a construír visualmente uma identidate para nossa
#aplicação. Entretanto, esses mesmos frameworks disponibilizam uma quantia de ferramentas 
#para que podemos cosntrír nossas aplicações, e essas mesmas podem ser frustrantes para
#nós programadores, por se tratar de um número extensivo de comandos e que muita vezes 
#posicionamos widgets em alguns lugares, depois de codar, e elas simplesmente não 'nos obedecem'
#então segundo o professor é necessário ter calma nessa parte :D
# Pack()
#   No tkinter, há algumas formas de posicionar elementos na tela, uma delas
#já foi vista até então, se chama '.pack()' e sem nenhum argumento passado como parâmetro
#ela pociona os elementos do topo da aplicação em direção a base da aplicação... como se fosse uma
#pilha... só que invertida :D
# Grid()
#   Os grides são uma ferramenta que possíbilia o posicionamento dinâmico de widgets, isso significa
#que através dos grides você pode posicionar elemtnosd e uma forma especifica na tela e mais complexa
#e até mesmo posicinar elementos acima um do outro.
# Place()
#   Através do place você consegue passar dois argumentos X e Y e posicionar um elemento na tela, o professor
#disse que esse é um método mais simples de posicioanr elementos na tela.

import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Layout intro')

# Widget
label1 = ttk.Label(window, text = 'Label_1', background = 'red')
label2 = ttk.Label(window, text = 'Label_2', background = 'blue')

# Pack
#   No método pack(), você pode passar alguns argumentos como parâmetro, um deles se refere a onde será
#posicionado o elemento na tela '.side = "left,tright,top,bottom" '
#   Um argumento que pode ser passado seria o 'expand = True/False', o false já vem por padrão, isso diz
#respeito a widget se expandir o suficiente para cobrir toda a área livre, e com o 'fill = "x, y, both"'
#você consegue ver isso visualmente.
#label1.pack(side = 'left', expand = True, fill = 'y')
#label2.pack(side = 'right', expand = True, fill = 'both')

# Grid
#   Com o gride nós precisamos de duas informações 'columnconfigure' e 'rowconfigure' é como se estivessemos
#mexendo em uma matrix em que podemos posicionar elementos a aprtir de suas respectivas colunas e linhas.
#   Em '.columnconfigure(...)' precisamos passar dois argumentos como parâmetro, o primerio seria um inteiro
#referente a coluna que ele ocupa e o segundo referênte ao 'peso' que seria a largura da coluna (que temq ue ser > 0)
#window.columnconfigure(0, weight = 1) #Essa é uma configuração de tela, então faça na tela que deseja configurar
#window.columnconfigure(1, weight = 1)
#window.columnconfigure(2, weight = 2)
#window.columnconfigure(3, weight = 1)

#   Em 'rowconfigure(...)' inicialmente passmos os mesmos tipos de argumentos, um inteiro referente a linha e um valore
#referente ao 'peso' da linha, 'window.rowconfigure(0, weight = 1)' com essa linha dizemos que nossa aplicação tem aglumas
#colunas... entretanto apenas uma linha.
#window.rowconfigure(0, weight = 1)
#window.rowconfigure(1, weight = 1)
#label1.grid(row = 0, column = 1, stick = 'nsew') com o 'stick = ' podemos pasar uma letra referente a uma direção e essa mesma widget será presa na borda referente a essa direção
#label1.grid(row = 0, column = 1, stick = 'nsew')
#label2.grid(row = 0, column = 0, stick = 'nsew')
# columnspan = int
#   Com o columnspan podemos fazer que um determinado widget possa se expandir até uma determinada coluna passando como
# argumento até qual coluna essa widget deve se expandir. Para esse exemplo eu poscionei +1 coluna para mostrar que a widget
#só se expande até a coluna específica
#label2.grid(row = 1, column = 1,columnspan = 2, stick = 'nsew')

# Place
#   Com o place nós podemos passar incialmente como parâmetro dois argumentos, que viriam a ser o X e Y e esses mesmos são os valores
# que o sistemas vai usar para posicionar na sua janela (aplicação) a widget que vc ta tentando poscionar.
#label1.place(x = 100, y = 200)
# Largura e alrura / width and height
label1.place(x = 100, y = 200, width = 200, height = 100)
# Largura e alrura / 'relx=' and 'rely=' que sejam adaptaveis ao tamanho da tela
#   Importante salientar que o mínimo é relx = 0.0 rely = 0.0 e o máximo é relx = 1.0 rely = 1.0
#isso significa que a widget sempre vai ficar sendo adaptada ao valore mínimo e máximo da aplicação...
#para se recordar melhor é apenas lembrar que 'tamanho relativo' usamos o 'rel' antes do parâmetro
#label2.place(relx = 0.5 , rely = 0.5, relwidth = 1)
# anchor
#   Podemos 'angorar' ou 'pregar' nossa widget para sempre estar em um determinado lugar da nossa aplicação usando o anchor e passando
#umma string 's', 'n' , 'e', 'w' ou uma combinação delas como 'anchor' 
label2.place(relx = 0.5 , rely = 0.5, relwidth = 1, anchor= 'se')


#run
window.mainloop()