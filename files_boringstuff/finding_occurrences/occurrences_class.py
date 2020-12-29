from pathlib import Path
import os
from tkinter import Tk, Label


class Ocurrences:
    def __init__(self, text_to_find):
        os.system('cls')
        self.list_found = []
        self.this_path = str(Path('C://') / 'find')
        self.text = text_to_find
        self.check_directory(self.this_path)
        self.execute_occurrences()

    def check_directory(self, path_file):
        windows = Tk()
        windows.geometry('100x100')
        if Path(path_file).is_dir():
            label_one = Label(windows, text='SEARCHING...')
            label_one.pack()
        else:
            label_two = Label(windows, text='WE\'VE CREATED THE FILE FOR YOU')
            Path(path_file).mkdir()
            label_two.pack()
        windows.after(10000, lambda: windows.destroy())
        windows.mainloop()

    def execute_occurrences(self):
        for filename in os.listdir(self.this_path):
            path_file = str(Path(self.this_path) / filename)
            count = 0
            with open(path_file) as file_open:
                all_text = file_open.read().lower()

            count = all_text.count(self.text.lower())

            if count > 0:
                self.list_found.append([filename, count])

        if len(self.list_found) > 0:
            print(f'the word {self.text} was found '
                  f'in these files...')

            for index, filename in enumerate(self.list_found):
                file_name = self.list_found[index][0]
                times = self.list_found[index][1]
                print(f'{index + 1}. {file_name} , {self.text} ' 
                      f'was found {times} times')
        else:
            print('No ocurrences were found!!')
