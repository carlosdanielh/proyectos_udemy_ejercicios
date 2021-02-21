import tkinter as tk
import shutil
from tkinter import filedialog
from pathlib import Path
from tkinter import messagebox as msg
from tkinter import ttk


# ------------------------------- constant ------------------------------------
the_path_answer = Path.cwd() / 'data' / 'saved_answer'
folder_selected = str()
continue_transfering_files = True


# ------------------------------- close windows -------------------------------
def close_window():
    global continue_transfering_files
    print('close windows')
    continue_transfering_files = False


# ------------------------------- event selected item list --------------------
def listbox_selected(event):
    global continue_transfering_files

    if list_box.curselection() != ():
        folder_to_save = filedialog.askdirectory()
        selection = list_box.get(list_box.curselection())
        answer = msg.askyesno('Info', 'Are your sure you want to save'
                              'this extension into the selected folder '
                              f'{folder_to_save}?')

        if answer:
            window_progress = tk.Toplevel()
            window_progress.title('coping...')
            window_progress.wm_attributes('-topmost', 1)
            window_progress.protocol('WM_DELETE_WINDOW', close_window)
            ProgBar = ttk.Progressbar(window_progress, length=365,
                                      style='black.Horizontal.TProgressbar')
            ProgBar.pack()

            destination_path = str(Path(folder_to_save))
            lista = list((Path(folder_selected)).glob('*' + selection))

            x = 100 / len(lista)
            add_progress = x
            for element in lista:
                if continue_transfering_files:
                    shutil.copy(element, destination_path)
                    ProgBar['value'] = add_progress
                    window_progress.update()
                    add_progress += x
                else:
                    continue_transfering_files = True
                    res = msg.askyesno('info', 'are you sure you want to stop '
                                       'the transfer')
                    print(res)
                    if res:
                        break
            window_progress.resizable(False, False)
            window_progress.destroy()


# ------------------------------- create file ---------------------------------
def save_the_answer(the_answer):
    with open(the_path_answer, 'w') as the_file:
        the_file.write(str(the_answer))


# ------------------------------- open ----------------------------------------
def to_open():
    global folder_selected
    list_box.delete(0, tk.END)
    # file_path = filedialog.askopenfilename()  # this will select a file
    folder_selected = filedialog.askdirectory()  # this will select a folder
    print(folder_selected)

    lista = (Path(folder_selected)).glob('*')
    lista_suffix = [file.suffix for file in lista if len(file.suffix) != 0]

    for index, files in enumerate(list(set(lista_suffix))):
        list_box.insert(index, files)

    if list_box.size() == 0:
        msg.showinfo('Info', 'this folder is empty')
    else:
        msg.showinfo('Info', 'We found some files extensions in this folder'
                     'select one extension to gather them into one folder'
                     '(select a folder to saved them)')


# ------------------------------- UI ------------------------------------------
window = tk.Tk()
window.geometry('420x350')

# ------------------------------- menu ----------------------------------------
menubar = tk.Menu(window)
menubar.add_command(label="Open", command=to_open)
menubar.add_command(label="Quit", command=window.quit)
window.config(menu=menubar)

# ------------------------------- labels --------------------------------------
title = tk.Label(window, text='ORGANIZER FILES', font=('Arial', 20, 'bold'))
title.pack()

# ------------------------------- listbox -------------------------------------
fm_top = tk.Frame(window)
scrollbar = tk.Scrollbar(fm_top)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
list_box = tk.Listbox(fm_top, height=10)
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)
list_box.bind("<<ListboxSelect>>", listbox_selected)
list_box.pack()
fm_top.pack(side=tk.TOP, pady=20)

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
