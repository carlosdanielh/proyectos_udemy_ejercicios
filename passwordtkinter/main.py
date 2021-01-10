import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

CHAIN_IMAGE_PATH = str(Path() / 'img' / 'logo.png')


def photo_resize(path, w, h):
    image = Image.open(path)
    image = image.resize((w, h), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    return photo


# ---------------------------- PASSWORD GENERATOR --------------------------- #

# ---------------------------- SAVE PASSWORD -------------------------------- #

# ---------------------------- UI SETUP ------------------------------------- #
windows = tk.Tk()
windows.geometry('450x450')

canvas = tk.Canvas(width=400, height=400, bg='lightblue', highlightthickness=0)
chain_img = photo_resize(CHAIN_IMAGE_PATH, 200, 200)
canvas.create_image(200, 200, image=chain_img)
canvas.grid(column=0, row=0, padx=20, pady=20)
windows.mainloop()
