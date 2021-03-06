from class_window import ToplevelCustomize
from pathlib import Path
from tkinter import messagebox as msg
from tkinter import ttk
import tkinter as tk
import shutil
import time

continue_transfering_files = True


class miniWin(tk.Tk):
    def __init__(self, textbutton):
        self.window = ToplevelCustomize(420, 350)
        self.window.wm_attributes('-topmost', 1)
        self.fm_top = tk.Frame(self.window)
        self.scrollbar = tk.Scrollbar(self.fm_top)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.list_box = tk.Listbox(self.fm_top,
                                   height=10,
                                   selectmode=tk.MULTIPLE)
        self.list_box.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.list_box.yview)
        self.list_box.pack()
        self.fm_top.pack(side=tk.TOP, pady=20)

        self.window.protocol('WM_DELETE_WINDOW', self.close_window_copy)

        self.textbutton = textbutton
        # button
        self.button = tk.Button(self.window,
                                text=self.textbutton,
                                command=self.listbox_selected)
        self.button.pack()

        #  menu
        self.menubar = tk.Menu(self.window)
        self.menubar.add_command(label="Open", command=self.to_open)
        self.menubar.add_command(label="Quit", command=self.window.quit)
        self.window.config(menu=self.menubar)

    def to_open(self):
        global folder_selected
        self.list_box.delete(0, tk.END)
        self.folder_selected = tk.filedialog.askdirectory(parent=self.window)

        lista = (Path(self.folder_selected)).glob('*')
        lista_suffix = [file.suffix for file in lista if len(file.suffix) != 0]

        if self.folder_selected != '':
            for index, files in enumerate(list(set(lista_suffix))):
                self.list_box.insert(index, files)

            if self.list_box.size() == 0:
                msg.showinfo('Info', 'this folder is empty')
            else:
                msg.showinfo('Info', 'We found some files extensions in this '
                             'folder select one extension to gather them into '
                             'one folder (select a folder to saved them)',
                             parent=self.window)

    def listbox_selected(self):
        global continue_transfering_files
        global window_progress

        if self.list_box.curselection() != ():
            selected_extension = [self.list_box.get(i) for i in
                                  self.list_box.curselection()]
            self.folder_to_save = tk.filedialog.askdirectory(parent=self.
                                                             window)

            if self.folder_to_save != '':
                answer = msg.askyesno('Info', 'Are your sure you want to save'
                                      'this extension into the selected folder'
                                      f' {self.folder_to_save}?', parent=self.
                                      window)

                if answer:
                    continue_transfering_files = True
                    self.window_progress = ToplevelCustomize(365, 30)
                    self.window_progress.title('coping...')
                    self.window_progress.wm_attributes('-topmost', 1)
                    self.window_progress.protocol('WM_DELETE_WINDOW',
                                                  self.close_window)
                    self.window_progress.resizable(False, False)

                    style_bar = 'black.Horizontal.TProgressbar'
                    self.ProgBar = ttk.Progressbar(self.window_progress,
                                                   length=365,
                                                   style=style_bar)
                    self.ProgBar.pack()

                    destination_path = str(Path(self.folder_to_save))

                    lista = []
                    for ext in selected_extension:
                        lista.extend(list((Path(self.folder_selected)).
                                          glob('*' + ext)))

                    x = 100 / len(lista)
                    add_progress = 0
                    interrupted = False
                    list_files_no_moved = []
                    for element in lista:
                        if not continue_transfering_files:
                            msg.showinfo('Info', 'some files have been'
                                         'transfered')
                            interrupted = True
                            break

                        if self.textbutton == 'move the selected':
                            try:
                                shutil.move(element, destination_path)
                            except shutil.Error:
                                list_files_no_moved.append(element.name)
                                pass
                        else:
                            shutil.copy(element, destination_path)

                        add_progress += x
                        self.ProgBar['value'] = add_progress
                        self.window_progress.update()

                    if not interrupted:
                        if len(list_files_no_moved) != 0:
                            file = ','.join(list_files_no_moved)
                            add_msg = (f',but, this file: {file} hasnt been '
                                       'moved because it alrady exist in the '
                                       'destination folder')
                        else:
                            add_msg = ''

                        self.update_list_box()
                        self.ProgBar['value'] = 100
                        time.sleep(1)
                        self.window_progress.destroy()
                        msg.showinfo('Info', 'the files have been transfered'
                                     f'{add_msg}', parent=self.window)

    def close_window(self):
        global continue_transfering_files
        continue_transfering_files = False
        self.window_progress.destroy()

    def close_window_copy(self):
        # enabling_all_buttons()
        self.window.destroy()

    def update_list_box(self):
        self.list_box.delete(0, tk.END)
        lista = (Path(self.folder_selected)).glob('*')
        lista_suffix = [file.suffix for file in lista if len(file.suffix) != 0]

        if self.folder_selected != '':
            for index, files in enumerate(list(set(lista_suffix))):
                self.list_box.insert(index, files)
