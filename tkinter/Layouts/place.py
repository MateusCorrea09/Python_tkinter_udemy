# Place Absolute
#   'place(...)' se trata de um método de posicionar elementos na tela a partir de coordenadas X e Y
# para posicionar um elemento na tela você deve entrar com dois valores referente ao X e Y da widget
# e a partir disso o tkinter vai considerar a posição x=0 e y=0 da widget (que seria o topo esquerdo
# da widget) e posicionar a apartir disso, você também pode entrar com duas informações opcionais que
# seriam a largra e altura da widget, mas é algo opcional, se você não entrar com esses valores o tkinter
# vai considerar o tamanho do conteúdo da widget como largura e altura. Importante lembrar que esse
# método fixa um elemento na tela e dessa forma impedindo que o mesmo seja redimencionada a parit do
# reajuste de tamanho da tela.
# Place relative
#   Esse é um método similar, oq diferencia seria a consideração do valor mínimo a ser colocado é x = 0.0
# e y = 0.0 e o valor máximo seria x = 1.0 e y = 1.0 e a partir disso as widgets passam a ser relativas 
# em consideração ao tamanho da tela, se a tela sofrer um reajuste de tela as widgets acompanharam esse
# reajuste.

import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Place')
window.geometry('400x600')

#widgets
label1 = ttk.Label(window, text= 'Label_1', background='red')
label2 =  ttk.Label(window, text='Label_2', background='blue')
label3 =  ttk.Label(window, text='Label_3', background='green')
button1 = ttk.Button(window, text='Button_1')

#layout
#   Usando o método absoluto e fixando elementos na tela
label1.place(x=300, y=200, width=100, height=200)
#   Usando o método relativo, facilmente identidicado a partir do uso do 'rel' de 'relativo'
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
label3.place(x = 80, y = 60,width = 160, height= 300)

#   'Anchor controls' é o ponto de controle utilizado para posicioanr elementos na tela, em
#default ele vem posicionado na widget em x=0 e y=0, mas podemos configura-lo, usamo o termo
#'anchor = "n","s","w","e" ou uma combinação ou "center"'
button1.place(relx=1, rely=1, anchor='se')

# frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text= 'Frame_label', background='yellow')
frame_button = ttk.Button(frame, text='Frame_Button')

# frame layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

exercici_label = ttk.Label(window, text='exercicio', background='orange')
exercici_label.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, height=200)
#run
window.mainloop()