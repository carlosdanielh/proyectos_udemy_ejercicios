import tkinter as tk


class Window(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        xpos = round((self.winfo_screenwidth() / 2) - (self.width / 2))
        ypos = (round((self.winfo_screenheight() / 2) - (self.height / 2)))-40
        self.geometry(f'{width}x{height}+{xpos}+{ypos}')


class ToplevelCustomize(tk.Toplevel):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        xpos = round((self.winfo_screenwidth() / 2) - (self.width / 2))
        ypos = (round((self.winfo_screenheight() / 2) - (self.height / 2)))-40
        self.geometry(f'{width}x{height}+{xpos}+{ypos}')
    