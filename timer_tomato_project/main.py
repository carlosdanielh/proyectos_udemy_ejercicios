import tkinter as tk
from pathlib import Path
import math
# ---------------------------- CONSTANTS -------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Segoe Script"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 11
counting = 0
# THE_IMAGE = str(Path.cwd() / 'udemy_projects' /
#                 'timer_tomato_project' / 'tomato.png')
THE_IMAGE = ('C:\\Users\\programacion\\Desktop\\ejercicios\\udemy_projects'
             '\\timer_tomato_project\\tomato.png')


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global counting
    counting = 0
    canvas.itemconfig(timer_text, text='00:00')
    # print(f'cancel id: {id_after} ')
    windows.after_cancel(id_after)


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_counting():
    global counting
    counting += 1

    if counting < 9:
        if counting % 2 == 1:
            count_down(WORK_MIN)
        elif counting % 2 == 0 and counting != 8:
            count_down(SHORT_BREAK_MIN)
        else:
            count_down(LONG_BREAK_MIN)
    else:
        counting = 0


# ---------------------------- COUNTDOWN MECHANISM ----------------------- #
def count_down(count):
    global id_after
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min == 0 or count_min < 10:
        count_min = f'0{count_min}'

    if count >= 0:
        id_after = windows.after(100, count_down, count - 1)
        canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    else:
        start_counting()


# ---------------------------- UI SETUP ---------------------------------- #
windows = tk.Tk()
windows.title('pomodora')
windows.config(padx=100, pady=50, bg='white')


label_timer = tk.Label(text='TIMER', font=(FONT_NAME, 26, 'bold'))
label_timer.grid(column=1, row=0)

button_start = tk.Button(text='Start', command=start_counting)
button_start.grid(column=0, row=3)

button_reset = tk.Button(text='Reset', command=reset_time)
button_reset.grid(column=2, row=3)

canvas = tk.Canvas(width=280, height=224, bg='red', highlightthickness=0,)
tomato_img = tk.PhotoImage(file=THE_IMAGE)
canvas.create_image(135, 112, image=tomato_img,)
timer_text = canvas.create_text(135, 130, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1, pady=30)
windows.mainloop()
