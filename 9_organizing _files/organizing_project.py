import tkinter as tk
import shutil
import time
from tkinter import filedialog
from pathlib import Path
from tkinter import messagebox as msg
from tkinter import ttk
from class_window import Window, ToplevelCustomize
from class_miniwin import miniWin
from class_buttons import buttonCustomize

# ------------------------------- constant ------------------------------------
BUTTON_WIDTH = 15
BUTTON_HEIGHT = 3
the_path_answer = Path.cwd() / 'data' / 'saved_answer'
folder_selected = ''
continue_transfering_files = True


# ------------------------------- desabling all buttons -----------------------
def desabling_all_buttons():
    button_copy_all.configure(state=tk.DISABLED)
    button_move.configure(state=tk.DISABLED)
    button3.configure(state=tk.DISABLED)


# ------------------------------- enabling all buttons -----------------------
def enabling_all_buttons():
    button_copy_all.configure(state=tk.NORMAL)
    button_move.configure(state=tk.NORMAL)
    button3.configure(state=tk.NORMAL)


# ------------------------------- close windows -------------------------------
# def close_window():
    # global continue_transfering_files
    # continue_transfering_files = False
    # window_progress.destroy()


# ------------------------------- close windows copy --------------------------
# def close_window_copy():
#     enabling_all_buttons()
#     window_copy_all.destroy()

def click_button():
    print('hola')
    if button_copy.text() == 'copy all':
        b = miniWin('copy the selected')
    elif option == 'move':
        b = miniWin('move the selected')
    button_clicked = True

def verify():
    window.after(100, verify)


# ------------------------------- move files ----------------------------------
def move_files():
    w = miniWin('move the selected')


# ------------------------------- create file ---------------------------------
def save_the_answer(the_answer):
    with open(the_path_answer, 'w') as the_file:
        the_file.write(str(the_answer))


# ------------------------------- UI ------------------------------------------
window = Window(410, 300)
verify()

# ------------------------------- buttons -------------------------------------
button_copy = buttonCustomize(window, 'copy all',
                              command=click_button)
button_copy.grid(column=0, row=1, padx=10, pady=30)

button_move = buttonCustomize(window, 'move files')
button_move.grid(column=1, row=1, padx=10, pady=10)

button_delete = buttonCustomize(window, 'delete files')
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
