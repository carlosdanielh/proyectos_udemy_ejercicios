import tkinter as tk
from pathlib import Path
import math
# from img_class import PhotoMain
from PIL import ImageTk, Image
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
PHOTO_PATH = str(Path.cwd() / 'img' / 'check.png')
THE_IMAGE = str(Path.cwd() / 'udemy_projects' / 'timer_tomato_project' / 
                'tomato.png')


# ---------------------------- TIMER RESET ------------------------------- #
def hide_all_check_buttons():
    global label_image
    label_image.grid_remove()
    label_image1.grid_remove()
    label_image2.grid_remove()
    label_image3.grid_remove()


# ---------------------------- PHOTO CHECK ------------------------------- #
def phto_label(path, w, h):
    image = Image.open(path)
    image = image.resize((w, h), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    return photo


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global counting
    counting = 0
    canvas.itemconfig(timer_text, text='00:00')
    # print(f'cancel id: {id_after} ')
    windows.after_cancel(id_after)
    button_start.configure(state=tk.ACTIVE)


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_counting():
    global counting
    button_start.configure(state=tk.DISABLED)

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


label_timer = tk.Label(text='TIMER', font=(FONT_NAME, 26, 'bold'),
                       bg='lightblue')
label_timer.grid(column=1, row=0, columnspan=3, sticky='WE')

button_start = tk.Button(text='Start', command=start_counting)
button_start.grid(column=0, row=3)

button_reset = tk.Button(text='Reset', command=reset_time)
button_reset.grid(column=2, row=3)

###############################################################################
photo = phto_label(PHOTO_PATH, 40, 30)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=2)

photo1 = phto_label(PHOTO_PATH, 40, 30)
label_image1 = tk.Label(image=photo1)
label_image1.grid(column=1, row=3, columnspan=3, sticky='W')

photo2 = phto_label(PHOTO_PATH, 40, 30)
label_image2 = tk.Label(image=photo2, bg='lightblue')
label_image2.grid(column=1, row=3, columnspan=1)

photo3 = phto_label(PHOTO_PATH, 40, 30)
label_image3 = tk.Label(image=photo3)
label_image3.grid(column=1, row=3, columnspan=1, sticky='E')
###############################################################################
hide_all_check_buttons()

canvas = tk.Canvas(width=280, height=224, bg='red', highlightthickness=0,)
tomato_img = tk.PhotoImage(file=THE_IMAGE)
canvas.create_image(135, 112, image=tomato_img,)
timer_text = canvas.create_text(135, 130, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1, pady=30)
windows.mainloop()
