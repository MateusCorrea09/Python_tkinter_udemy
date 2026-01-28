#Canvas
#   Segundo o professor canvas são usados para desenhar shapes (ou formas geométricas)

import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# CANVAS, é uma propriedade que pode ser armazenada em uma variavel
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()
#   As formas geométricas podem ser criadas a partit do acesso dos métods e da passagem de algumas informações básicas por uma tupla
#canvas.create_rectangle((left, top, right, bottom)) ,  vc pode colcoar dentro de tuplas, listas, ou deixar sem nenuma estrutura de dados
canvas.create_rectangle((50, 20, 100, 200), fill ='Orange', width = 10, dash= (1,2,1,1), outline='grey' )
#   Com o canvas podemos criar linhas!
#canvas.create_line(start_x. start_y, end_x, end_y)
#canvas.create_line([0, 0, 100, 150], fill= 'Yellow')
#   Criação de circulos ou ovais
#canvas.create_oval(0, 0, 100, 100)
#   é possível usar a ferramenta do canvas para criar um cráfico ou uma forma personalizada de geometrica organizada a partir de algumas ifnormações
#canvas.create_oval(
#    200,0,300,100,
#    fill='green'
#)
#canvas.create_arc(
#    (200,0,300,100),
#    fill = 'red',
#    start = 45,
#    extent = 140,
#    style = tk.PIESLICE,
#    outline = 'red',
#    width = 1
#)
#   Com o canvas vc também pode crar texto, mas o professor disse que isso não é tão útil assim... e que existem outras fotmas
#de fazer isso melhor
#canvas.create_text((100, 200), text = 'This is a some txt :D', fill= 'Blue')

#   É possível criar uma janela dentro da janela master que criamos, usando o canvas
#canvas.create_window((150,100), window = ttk.Label(window, text = 'Esse é um texto dentro de uma janela... que esta dentro da janela principal'))


#EXERCÍCIO: criar uma janela que a aprtir da movimentação do Mouse seja colocabo uma amrcação visual, como paint
def draw_on_canvas(event):
    x = event.x
    y = event.y

    canvas.create_oval(
        x - brush_size / 2,
        y - brush_size / 2,
        x + brush_size / 2,
        y + brush_size / 2,
        fill = color_brush
    )
def brush_adjust(event):
    global brush_size 
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4 


color_brush = 'blue'
brush_size = 2

canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>',brush_adjust)
#run
window.mainloop()