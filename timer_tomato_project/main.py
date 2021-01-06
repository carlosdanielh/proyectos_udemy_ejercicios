import tkinter as tk
from pathlib import Path
import math
from PIL import ImageTk, Image
# ---------------------------- CONSTANTS -------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = '#f9caa7'
FONT_NAME = "Segoe Script"
PHOTO_PATH = str(Path.cwd() / 'img' / 'check.png')
THE_TOMATO_IMG_PATH = str(Path.cwd() / 'img' / 'tomato2.png')
BUTTON_FONT = ('Arial', 10, 'bold')
FONT_LABEL_TIMER = ("Segoe Script", 26, 'bold')
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 11
counting = 0
label_count = 0


# ---------------------------- HIDE CHECK LABELS ------------------------- #
def hide_all_check_buttons():
    for label_check_image in list_check_image:
        label_check_image.grid_remove()


# ---------------------------- PHOTO RESIZE ------------------------------- #
def photo_resize(path, w, h):
    image = Image.open(path)
    image = image.resize((w, h), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    return photo


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global counting
    global label_count
    counting = 0
    label_count = 0

    canvas.itemconfig(timer_text, text='00:00')
    windows.after_cancel(id_after)
    button_start.configure(state=tk.ACTIVE)
    label_timer.configure(text='TIMER', font=FONT_LABEL_TIMER, bg=BLUE,
                          fg='black')
    hide_all_check_buttons()


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_counting():
    global counting
    button_start.configure(state=tk.DISABLED)
    counting += 1

    if counting < 9:
        if counting % 2 == 1:
            count_down(WORK_MIN)
            label_timer.configure(text='Let\'s get to bussiness!!',
                                  font=FONT_LABEL_TIMER, fg='black')
        elif counting % 2 == 0 and counting != 8:
            count_down(SHORT_BREAK_MIN)
            label_timer.configure(text='It\'s time to rest',
                                  font=FONT_LABEL_TIMER, fg=GREEN)
        else:
            count_down(LONG_BREAK_MIN)
            label_timer.configure(text='It\'s time for a long rest',
                                  font=FONT_LABEL_TIMER, fg=GREEN)
    else:
        counting = 0
        reset_time()


# ---------------------------- COUNTDOWN MECHANISM ----------------------- #
def count_down(count):
    global id_after
    global counting
    global label_count
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min == 0 or count_min < 10:
        count_min = f'0{count_min}'

    if count >= 0:
        id_after = windows.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    else:
        if counting % 2 == 1:
            list_check_image[label_count].grid()
            label_count += 1
        start_counting()


# ---------------------------- UI SETUP ---------------------------------- #
windows = tk.Tk()
windows.title('pomodora')
windows.config(padx=100, pady=50, bg=BLUE)


label_timer = tk.Label(text='TIMER', font=FONT_LABEL_TIMER,
                       bg=BLUE)
label_timer.grid(column=0, row=0, columnspan=3, sticky='WE')

button_start = tk.Button(text='Start', command=start_counting,
                         font=BUTTON_FONT)
button_start.grid(column=0, row=3)

button_reset = tk.Button(text='Reset', command=reset_time,
                         font=BUTTON_FONT)
button_reset.grid(column=2, row=3)

###############################################################################
photo = photo_resize(PHOTO_PATH, 40, 30)

list_check_image = [tk.Label(image=photo, bg=BLUE) for element in range(4)]

list_check_image[0].grid(column=1, row=3, padx=70, sticky='W')
list_check_image[1].grid(column=1, row=3, padx=100, sticky='W')
list_check_image[2].grid(column=1, row=3, padx=150, sticky='W') 
list_check_image[3].grid(column=1, row=3, columnspan=1, padx=160, sticky='W')
###############################################################################
hide_all_check_buttons()

canvas = tk.Canvas(width=280, height=224, bg=BLUE, highlightthickness=0,)
tomato_img = photo_resize(THE_TOMATO_IMG_PATH, 260, 210)
canvas.create_image(135, 112, image=tomato_img)
timer_text = canvas.create_text(135, 130, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'),)
canvas.grid(column=1, row=1, pady=30)
windows.mainloop()
