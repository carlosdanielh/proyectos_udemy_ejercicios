import tkinter as tk
from pathlib import Path
import math
from PIL import ImageTk, Image
# ---------------------------- CONSTANTS -------------------------------- #
FG_BREAK = "#e7305b"  # PINK
BG_COLOR = '#464646'  # GREY 
WORK_COLOR = '#5aa57d'  # GREEN
FONT_NAME = "Comic Sans MS"
FONT_LABEL_TIMER = (FONT_NAME, 26, 'bold')
PATH_CHECKS = str(Path.cwd() / 'img' / 'check.png')
PATH_TOMATO = str(Path.cwd() / 'img' / 'tomato2.png')
PATH_ICON = str(Path.cwd() / 'img' / 'tomate_ico.png')
BUTTON_FONT = ('Arial', 10, 'bold')
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 11
MIN = 1
counting = 0
label_count = 0


# ---------------------------- HIDE CHECK LABELS ------------------------- #
def hide_all_check_buttons():
    for label_check_image in list_check_image:
        label_check_image.pack_forget()


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
    label_timer.configure(text='TIMER', font=FONT_LABEL_TIMER, bg=BG_COLOR,
                          fg='black')
    hide_all_check_buttons()


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_counting():
    global counting
    button_start.configure(state=tk.DISABLED)
    counting += 1

    WORK = WORK_MIN * MIN
    SHORT_BREAK = SHORT_BREAK_MIN * MIN
    LONG_BREAK = LONG_BREAK_MIN * MIN

    if counting < 9:
        if counting % 2 == 1:
            count_down(WORK)
            label_timer.configure(text='WORK',
                                  font=FONT_LABEL_TIMER, fg=WORK_COLOR)
        elif counting % 2 == 0 and counting != 8:
            count_down(SHORT_BREAK)
            label_timer.configure(text='BREAK',
                                  font=FONT_LABEL_TIMER, fg=FG_BREAK)
        else:
            count_down(LONG_BREAK)
            label_timer.configure(text='LONG BREAK',
                                  font=FONT_LABEL_TIMER, fg=FG_BREAK)
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
            list_check_image[label_count].pack(side=tk.LEFT)
            label_count += 1
        start_counting()


# ---------------------------- UI SETUP ---------------------------------- #
windows = tk.Tk()
windows.title('pomodora')
windows.config(bg=BG_COLOR)
icon = tk.PhotoImage(file=PATH_ICON)
windows.iconphoto(False, icon)

label_timer = tk.Label(text='TIMER', font=FONT_LABEL_TIMER,
                       bg=BG_COLOR)
label_timer.grid(column=1, row=0)

button_start = tk.Button(text='Start', command=start_counting,
                         font=BUTTON_FONT, height=10, width=4)
button_start.grid(column=0, row=1)

button_reset = tk.Button(text='Reset', command=reset_time,
                         font=BUTTON_FONT, height=10, width=4)
button_reset.grid(column=2, row=1)

###############################################################################
frame_bottom = tk.Frame(windows, bg=BG_COLOR, width=160, height=30)
photo = photo_resize(PATH_CHECKS, 40, 30)

list_check_image = [tk.Label(frame_bottom, image=photo, bg=BG_COLOR)
                    for element in range(4)]
frame_bottom.grid(column=1, row=2)

###############################################################################
canvas = tk.Canvas(width=280, height=224, bg=BG_COLOR, highlightthickness=0)
tomato_img = photo_resize(PATH_TOMATO, 260, 210)
canvas.create_image(135, 112, image=tomato_img)
timer_text = canvas.create_text(135, 130, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'),)
canvas.grid(column=1, row=1, pady=15)

windows.resizable(False, False)
windows.mainloop()
