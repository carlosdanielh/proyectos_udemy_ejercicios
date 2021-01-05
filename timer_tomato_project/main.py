import tkinter as tk
from pathlib import Path

# ---------------------------- CONSTANTS -------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Segoe Script"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# THE_IMAGE = str(Path.cwd() / 'udemy_projects' /
#                 'timer_tomato_project' / 'tomato.png')
THE_IMAGE = 'C:\\Users\\programacion\\Desktop\\ejercicios\\udemy_projects\\timer_tomato_project\\tomato.png'
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM --------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ----------------------- #
def count_down(count):
    pass
# ---------------------------- UI SETUP ---------------------------------- #

windows = tk.Tk()
windows.title('pomodora')
windows.config(padx=100, pady=50, bg='white')


label_timer = tk.Label(text='TIMER', font=(FONT_NAME, 26, 'bold'))
label_timer.grid(column=1, row=0)

button_start = tk.Button(text='Start')
button_start.grid(column=0, row=3)

button_reset = tk.Button(text='Reset')
button_reset.grid(column=2, row=3)

canvas = tk.Canvas(width=280, height=224, bg='red', highlightthickness=0,)
tomato_img = tk.PhotoImage(file=THE_IMAGE)
canvas.create_image(135, 112, image=tomato_img,)
canvas.create_text(135, 130, text='00:00', fill='white',
                   font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1, pady=30)
windows.mainloop()
