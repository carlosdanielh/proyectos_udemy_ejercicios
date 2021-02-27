from class_window import ToplevelCustomize
import tkinter as tk


class miniWin(tk.Tk):
    def __init__(self):
        super().__init__()
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
        # self.list_box.bind("<<ListboxSelect>>", listbox_selected)
        self.list_box.pack()
        self.fm_top.pack(side=tk.TOP, pady=20)

        #  menu
        self.menubar = tk.Menu(self.window)
        self.menubar.add_command(label="Open", command=to_open)
        self.menubar.add_command(label="Quit", command=self.window.quit)
        self.window.config(menu=self.menubar)