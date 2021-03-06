import tkinter as tk
from class_miniwin import miniWin

BUTTON_WIDTH = 15
BUTTON_HEIGHT = 3
button_clicked = False

class buttonCustomize(tk.Button):
    def __init__(self, master_, text_, command=None):
        super().__init__(master_,
                         text=text_,
                         width=BUTTON_WIDTH,
                         height=BUTTON_HEIGHT,
                         
                         )

    def click_button(self, option):
        if option == 'copy':
            b = miniWin('copy the selected')
        elif option == 'move':
            b = miniWin('move the selected')
        button_clicked = True

    def text(self):
        print('entro')
        return self['text']