import tkinter as tk
import shutil
import time
from tkinter import filedialog
from pathlib import Path
from tkinter import messagebox as msg
from tkinter import ttk
from class_window import Window, ToplevelCustomize
from class_miniwin import miniWin
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
def close_window():
    global continue_transfering_files
    continue_transfering_files = False
    window_progress.destroy()


# ------------------------------- close windows copy --------------------------
def close_window_copy():
    enabling_all_buttons()
    window_copy_all.destroy()


# ------------------------------- ccopy all --- -------------------------------
def copy_files():
    global list_box
    global window_copy_all
    desabling_all_buttons()
    #  listbox
    window_copy_all = ToplevelCustomize(420, 350)
    window_copy_all.wm_attributes('-topmost', 1)
    fm_top = tk.Frame(window_copy_all)
    scrollbar = tk.Scrollbar(fm_top)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
    list_box = tk.Listbox(fm_top, height=10, selectmode=tk.MULTIPLE)
    list_box.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=list_box.yview)
    # list_box.bind("<<ListboxSelect>>", listbox_selected)
    list_box.pack()
    fm_top.pack(side=tk.TOP, pady=20)

    #  menu
    menubar = tk.Menu(window_copy_all)
    menubar.add_command(label="Open", command=to_open)
    menubar.add_command(label="Quit", command=window_copy_all.quit)
    window_copy_all.config(menu=menubar)
    window_copy_all.protocol('WM_DELETE_WINDOW', close_window_copy)

    # button
    button_transfer_copy = tk.Button(window_copy_all,
                                     text='copy the selected',
                                     command=listbox_selected)
    button_transfer_copy.pack()


# ------------------------------- move files ----------------------------------
def move_files():
    w = miniWin('move the selected')


# ------------------------------- event selected item list --------------------
def listbox_selected():
    global continue_transfering_files
    global window_progress

    if list_box.curselection() != ():
        selected_extension = [list_box.get(i) for i in list_box.curselection()]
        folder_to_save = filedialog.askdirectory(parent=window_copy_all)

        if folder_to_save != '':
            answer = msg.askyesno('Info', 'Are your sure you want to save'
                                  'this extension into the selected folder '
                                  f'{folder_to_save}?', parent=window_copy_all)

            if answer:
                continue_transfering_files = True
                window_progress = ToplevelCustomize(365, 30)
                window_progress.title('coping...')
                window_progress.wm_attributes('-topmost', 1)
                window_progress.protocol('WM_DELETE_WINDOW', close_window)
                window_progress.resizable(False, False)

                style_bar = 'black.Horizontal.TProgressbar'
                ProgBar = ttk.Progressbar(window_progress,
                                          length=365,
                                          style=style_bar)
                ProgBar.pack()

                destination_path = str(Path(folder_to_save))

                lista = []
                for ext in selected_extension:
                    lista.extend(list((Path(folder_selected)).glob('*' + ext)))

                x = 100 / len(lista)
                add_progress = 0
                interrupted = False
                for element in lista:
                    if not continue_transfering_files:
                        msg.showinfo('Info', 'some files have been transfered')
                        interrupted = True
                        break

                    shutil.copy(element, destination_path)
                    add_progress += x
                    ProgBar['value'] = add_progress
                    window_progress.update()

                if not interrupted:
                    ProgBar['value'] = 100
                    time.sleep(1)
                    window_progress.destroy()
                    msg.showinfo('Info', 'the files have been transfered',
                                 parent=window_copy_all)


# ------------------------------- create file ---------------------------------
def save_the_answer(the_answer):
    with open(the_path_answer, 'w') as the_file:
        the_file.write(str(the_answer))


# ------------------------------- open ----------------------------------------
def to_open():
    global folder_selected
    list_box.delete(0, tk.END)
    # this will select a folder
    folder_selected = filedialog.askdirectory(parent=window_copy_all)
    print(folder_selected)

    lista = (Path(folder_selected)).glob('*')
    lista_suffix = [file.suffix for file in lista if len(file.suffix) != 0]

    if folder_selected != '':
        for index, files in enumerate(list(set(lista_suffix))):
            list_box.insert(index, files)

        if list_box.size() == 0:
            msg.showinfo('Info', 'this folder is empty')
        else:
            msg.showinfo('Info', 'We found some files extensions in this '
                         'folder select one extension to gather them into one '
                         'folder (select a folder to saved them)',
                         parent=window_copy_all)


# ------------------------------- UI ------------------------------------------
window = Window(410, 300)

# ------------------------------- buttons -------------------------------------
button_copy_all = tk.Button(window,
                            text='copy all',
                            width=BUTTON_WIDTH,
                            height=BUTTON_HEIGHT,
                            command=copy_files)
button_copy_all.grid(column=0, row=1, padx=10, pady=30)

button_move = tk.Button(window,
                        text='move files',
                        width=BUTTON_WIDTH,
                        height=BUTTON_HEIGHT,
                        command=move_files)
button_move.grid(column=1, row=1, padx=10, pady=10)

button3 = tk.Button(window,
                    text='xxxx',
                    width=BUTTON_WIDTH,
                    height=BUTTON_HEIGHT,
                    command=copy_files)
button3.grid(column=2, row=1, padx=10, pady=10)

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
