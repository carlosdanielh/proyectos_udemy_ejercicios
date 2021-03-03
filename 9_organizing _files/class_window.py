import tkinter as tk


class Window(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        xpos = round((self.winfo_screenwidth() / 2) - (self.width / 2))
        ypos = (round((self.winfo_screenheight() / 2) - (self.height / 2)))-40
        self.geometry(f'{width}x{height}+{xpos}+{ypos}')

        self.button = tk.Button(window,
                           text='copy all',
                           width=BUTTON_WIDTH,
                           height=BUTTON_HEIGHT,
                           command=copy_files)
        button.grid(column=0, row=1, padx=10, pady=30)

class ToplevelCustomize(tk.Toplevel):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        xpos = round((self.winfo_screenwidth() / 2) - (self.width / 2))
        ypos = (round((self.winfo_screenheight() / 2) - (self.height / 2)))-40
        self.geometry(f'{width}x{height}+{xpos}+{ypos}')
    