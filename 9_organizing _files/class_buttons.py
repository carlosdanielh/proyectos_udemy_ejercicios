import tkinter as tk
from class_miniwin import miniWin

BUTTON_WIDTH = 15
BUTTON_HEIGHT = 3

class buttonCustomize(tk.Button):
    def __init__(self, master_, text_, task):
        self.button = tk.Button(master_,
                                text=text_,
                                width=BUTTON_WIDTH,
                                height=BUTTON_HEIGHT,
                                command=lambda: self.click_button(task))
        self.button.grid(column=0, row=1, padx=10, pady=30)

    def click_button(self, option):
        if option == 'copy':
            b = miniWin('copy the selected')

    # button_move = tk.Button(window,
    #                         text='move files',
    #                         width=BUTTON_WIDTH,
    #                         height=BUTTON_HEIGHT,
    #                         command=move_files)
    # button_move.grid(column=1, row=1, padx=10, pady=10)

    # button3 = tk.Button(window,
    #                     text='xxxx',
    #                     width=BUTTON_WIDTH,
    #                     height=BUTTON_HEIGHT,
    #                     command=copy_files)
    # button3.grid(column=2, row=1, padx=10, pady=10)