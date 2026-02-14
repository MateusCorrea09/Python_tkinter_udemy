import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, start_size):
        super().__init__()
        self.title('Responsive layout')
        self.geometry(f'{start_size[0]}x{start_size[1]}')
        
        SizeNotifier(self, {600: self.create_medium_layout, 300:self.create_small_layout})
 
        self.mainloop()

    def create_small_layout(self):
        print('Small layout')

    def create_medium_layout(self):
        print('medium layout')

class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = {Key: value for Key, value in sorted(size_dict.items())}
        self.window.bind('<Configure>', self.check_size)

    def check_size(self, event):
        self.size_dict[300]()   

app = App((400,300))