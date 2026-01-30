import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')

frame = ttk.Frame(window, width= 200, height= 200, borderwidth=10, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

label = ttk.Label(frame, text= 'Labal na frama')
label.pack()

button = ttk.Button(frame, text= 'Button')
button.pack()

label2 = ttk.Label(window, text= 'label fora do frame')
label2.pack()

window.mainloop()