import tkinter as tk
from pathlib import Path
from tkinter import messagebox as msg
from class_window import Window
from class_miniwin import miniWin

# ------------------------------- constant ------------------------------------
BUTTON_WIDTH = 15
BUTTON_HEIGHT = 3
the_path_answer = Path.cwd() / 'data' / 'saved_answer'
folder_selected = ''
continue_transfering_files = True


# ------------------------------- desabling all buttons -----------------------
def desabling_all_buttons():
    button_copy.configure(state=tk.DISABLED)
    button_move.configure(state=tk.DISABLED)
    button_delete.configure(state=tk.DISABLED)


# # ------------------------------- enabling all buttons ----------------------
# def enabling_all_buttons():
#     button_copy.configure(state=tk.NORMAL)
#     button_move.configure(state=tk.NORMAL)
#     button_delete.configure(state=tk.NORMAL)


def click_button(option):
    desabling_all_buttons()
    objects = [button_copy, button_delete, button_move]
    if option == 'copy':
        b = miniWin('copy the selected', objects)
    elif option == 'move':
        b = miniWin('move the selected', objects)
    elif option == 'delete':
        b = miniWin('delete the selected', objects)


# ------------------------------- move files ----------------------------------
def move_files():
    w = miniWin('move the selected')


# ------------------------------- create file ---------------------------------
def save_the_answer(the_answer):
    with open(the_path_answer, 'w') as the_file:
        the_file.write(str(the_answer))


# ------------------------------- UI ------------------------------------------
window = Window(410, 300)

# ------------------------------- buttons -------------------------------------
button_copy = tk.Button(window,
                        text='copy all',
                        width=BUTTON_WIDTH,
                        height=BUTTON_HEIGHT,
                        command=lambda: click_button('copy'))
button_copy.grid(column=0, row=1, padx=10, pady=30)

button_move = tk.Button(window,
                        text='move files',
                        width=BUTTON_WIDTH,
                        height=BUTTON_HEIGHT,
                        command=lambda: click_button('move'))                        
button_move.grid(column=1, row=1, padx=10, pady=10)

button_delete = tk.Button(window,
                          text='delete files',
                          width=BUTTON_WIDTH,
                          height=BUTTON_HEIGHT,
                          command=lambda: click_button('delete'))
button_delete.grid(column=2, row=1, padx=10, pady=10)

# ------------------------------- labels --------------------------------------
title = tk.Label(window, text=' FILE\'S ORGANIZER', font=('Arial', 20, 'bold'))
title.grid(column=0, row=0, columnspan=3)

# ------------------------------- msg box -------------------------------------
if Path(the_path_answer).exists():
    with open(the_path_answer) as the_file:
        answer = the_file.read()

        if answer == 'True':
            response = msg.askyesno('wellcome', 'choose a folder in the menu'
                                    'bar to get all types extensions it has\n'
                                    'do you want next time ask you this?')
            save_the_answer(response)
else:
    response = msg.askyesno('wellcome', 'choose a folder in the menu'
                            'bar to get all types extensions it has\n'
                            'do you want next time ask you this?')
    save_the_answer(response)

window.mainloop()
