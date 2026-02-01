import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
# Mudança na inicialização
#   Até então vimos em .geometry() que podemos passar dois argumentos como parâmetro, widthxheight, entretanto
#há duas informações a mais que podem ser passadas como parâmetro e essas mesmas se tratam da froma com que a
#aplicação será inicializada e essas mesmas são passadas por '+' em seguida ao width e height 

window.title('More on the window')

#EXERCÍCIO: crie uma forma de deixar sua aplicação no centro da tela :D
#window.attributes('-fullscreen', True)
#Descobrindo qual é o tamanho da tela do monitor
#print(window.winfo_screenheight())
#print(window.winfo_screenwidth())
#decobindo o quato do valor
#print(f'A metade da metade de width {(window.winfo_screenwidth())/4}\nA metade da metade de ehight {(window.winfo_screenheight())/4}')
#alterando a geometria da tele
#window.geometry('600x400+342+192')
    #Solução do professor: mais eficiênte
#Primeiro ele armazena em variaveis todas as informações
window_width = 600
window_height = 500
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()
#Depois ele realiza um calculo com base na divisão e subtração das informações, e aramzena o dado convertido em um inteiro
#para evitar erro na hora de armazenar no '.geometry()' proque ele espera um int e divisões retornam float
left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
#por final ele passa como argumento no parâmetro do método '.geometry()' usando f_string
window.geometry(f'{window_width}x{window_height}+{left}+{top}')


# Mudança de icon da aplicação
#   Lembre-se de priorizar a extenção '.ico' para usar essa possibilidade
#window.iconbitmap('python.ico')
# Window size
#   Limitação de o quanto pequena essa aplicação pode ser minimizada
#window.minsize(width , height)
#window.minsize(200, 100)
#   Limitação de o quanto grande esa aplicação pode ser maximizada
#window.maxsize(800, 700)
#   Limitação de qual EIXO pode ser 'esticado' ter sua dimensão alterada
#window.resizable(True, False)

# Screen atributes
#   Esse método window.winfo_screenwidth() e window.winfo_screenheight() retornam a posição da aplicação no minitor
#pode ser util na hora de posicionar a sua aplicação em algum local específico da tela
#print(window.winfo_screenheight())
#print(window.winfo_screenwidth())

# Window attributes
#   Transparência de tela (visibilidade)
window.attributes('-alpha', 0.8) #O ajuste ocorre ente 0 para invisível e 1 para totalmente visível
#   Hierarquia de importância da aplicação, isso deixa a sua aplicação na frente de todas as outras
#window.attributes('-topmost', True) 

# Security event
#   Permite que uma tecla seja responsavel por finalizar a aplicação
window.bind('<Escape>', lambda event: window.quit()) #Quando o usuário precionar o 'Esc' a aplicação fecha
#   Impede interações na sua aplicação (impede que o suuário interaja com algo)
#window.attributes('-disable', True)
#   Permite que a aplicação seja inicializada em fullscreen
#window.attributes('-fullscreen', True)

# Title bar 
#   O método 'overrideredirect(True)' permite esconder a barra que contem o icone, nome e botões da sua aplicação (aqueles que vem por padrão)
window.overrideredirect(True)
#   Um problema que surge quando usamos o 'overrideredirect(True)' é que fica desabilitado o remencionamento de tela
#para isso podemis usar uma widget que há no 'ttk' chamada Sizegrip(tela_que_ta_com_o_overrideredirect(True))
grip = ttk.Sizegrip(window)
#grip.pack() #Um problema surge, a posição da widget, mas concertamos com .place(rex = float, rely= float, anchor = 'inicial_letra + inicial_letra')
grip.place(relx = 1.0, rely = 1.0, anchor = 'se') #'se' é algo como Sul (South) e o Leste (East)

#run
window.mainloop()