#   Sliders
#slides podem ser usados de algumas formas e esses mesmos nos ajudam a entender progressão
#ou nos dar acesso a determinados elementos de uma apliação.
#   Progressbar -> nos mostram o progresso de uma determinada aplicação
#podem ser posicionados na horizontal e na vertical a depender da necessidade
#   Sliders -> podem ser usados pelo usuário ou setados por algum elemento de
#controle do sistema, posso usar o mause ou uma variavel.

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Sliders')

#widget
#   Usaremos uma propriedade de 'ttk' e atribuiremos 'Scale' em uma variavel, e através do comando abaixo
#é possível perceber que o event de interação com o slider nos devolve um número ponto flutuante que vai de 0 até 1.0
# e isso é bem interessante! :D, mas na verdade podemos usar o 'value' ao invés do 'event'
#scale = ttk.Scale(window, command = lambda event: print(f'{event:.4}'))
#   É importante resaltar que embora comece no 0 e vá até o 1.0, podemos delimitar o ponto de inicio e final usando
#o 'from_' e 'to'
    #Podemos usar uma variavel e atribuir a ela o controle ou armazenamento de dados da 'Scale' que estamos criando
#entretanto, é de se notar que a 'Scale' nos devolve inicialmente valores double, isso significa que para armazenamos valores
#int devemos atribuir na função lambd o seguinte termo 'nome_da_variavel_de_controle.get()' desssa forma será armanezano o valore
#igual a de definição da varioaval
scale_int = tk.IntVar(value= 15)
scale = ttk.Scale(window, 
                  command = lambda value: progress.stop(), 
                  from_ = 1, to=25,
                  length = 300, #Iso aki é ára controlar o tamanho do slider visualmente
                  orient= 'horizontal',
                  variable= scale_int )
scale.pack()

#Progress bar
progress = ttk.Progressbar(window, 
                           variable= scale_int, 
                           maximum = 25,
                           orient= 'horizontal',
                           mode='indeterminate',
                           length= 400)

progress.pack()

#progress.start(1000)

#ScrollText
#scrolled_text = scrolledtext.ScrolledText(window)
#scrolled_text.pack()


##
def controle_visualisador(valor):
    print(valor)
    progresso.start()
    
    

controle = tk.IntVar()
scala = ttk.Scale(window,
                  
                  from_ = 0, to = 100,
                  variable = controle)
progresso = ttk.Progressbar(window, orient='vertical', variable = controle)
progresso.start()

label = ttk.Label(window, textvariable = controle )

scala.pack()
progresso.pack()
label.pack()
#run
window.mainloop()