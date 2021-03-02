import tkinter as tk

class buttonCustomize(tk.Button):
    def __init__(self, master ,text_, width_, height_):
        button = tk.Button(window,
                           text='copy all',
                           width=BUTTON_WIDTH,
                           height=BUTTON_HEIGHT,
                           command=copy_files)
        button.grid(column=0, row=1, padx=10, pady=30)

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