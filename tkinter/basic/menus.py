#   A construção de menus no tkiner nos permite dar ao usuário a possibilidade
#de acessar diversas partes do nosso sistema, e isso a partir de possicionar
#uma widget chamata 'menu' que pode agrupar outras widgets ou outros menus (assim com mais possíbilidades de acesso)
import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

# menu
#   É interessante pensar que na criação de menus é usada com frequência uma palavra chamada 'Cascada' ou 'Cascade' que se refere 
#a uma cachoeira que cai... ou algo assim! então quando vc clica em um 'button' em um menu vc dá inicio a uma 'cascada' que 'cai'
#as outras opções de menu.
#   Primerio vamos criar a 'master' do menu onde ficarão agrupados as opções do menu.
menu = tk.Menu(window)
# Sub menu
#   Agora começaremos a colocar as opções dentro do menu.  Esse tearoff serve para impedir
#da opção que acabamos de criar ficar com um botão vazio que cria outra tela ao ser clicada
file_menu = tk.Menu(menu, tearoff = False)
#   Precisamos adicionar as características do nosso menu (O file_menu e oq tem dentro dele)
file_menu.add_command(label = 'new', command = lambda: print('New file'))
file_menu.add_command(label = 'Open file', command = lambda: print('File Open'))
file_menu.add_separator() #Isso aki é algo visual apenas

#   Precisamos adicionar essa opção no nosso menu principal, seria algo do tipo...
#'No menu principal que criamos no inicio e chamamos ele de 'menu' dê um nome de um atributo e chame esse mesmo de 'file' e logo depois
# atribua esse 'file' as características de 'file_menu' que criamos (entenda como características as linhas 21-25)' 
menu.add_cascade(label = 'File', menu = file_menu)

# Another sub menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'entry help', command =lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label= 'check', onvalue = 'on', offvalue = 'off', variable = help_check_string)

menu.add_cascade(label= 'help', menu= help_menu)
###Exercício
exercise_menu = tk.Menu(menu, tearoff= False)
exercise_menu.add_command(label= 'exercise_teste_1')
menu.add_cascade(label= 'exercise', menu = exercise_menu)

exercise_sub_menu = tk.Menu(menu, tearoff = False)
exercise_sub_menu.add_command(label= 'Opções dentro de opções', command=lambda:print('Aki ó :D'))
exercise_menu.add_cascade(label = 'Mais uma sessão', menu = exercise_sub_menu)


#   No menu n´so não damos 'pack()' e sim usamos essa forma de colocar em baixo, já que estamos usando a biblioteca 'tk' ou invés de 'ttk'
window.config(menu = menu)
# Menu button
#   A lógica de criação de botões que possuem suas respectivas cascadas, é a mesma da criação
#dos menus, se atente a que nesse casso nós estamos criando uma widget de menu... e para isso usamos
#o 'ttk', diferente deos menus acima que criamos usando apenas o 'tk'
menu_button = ttk.Menubutton(window, text ='menu button')
menu_button.pack()

button_sub_button = tk.Menu(menu_button, tearoff=False)
button_sub_button.add_command(label = 'entry', command = lambda: print('Test_1'))
button_sub_button.add_command(label = 'Check_1')
menu_button.config(menu = button_sub_button)


#run
window.mainloop()