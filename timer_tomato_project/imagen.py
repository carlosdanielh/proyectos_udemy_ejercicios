import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

PHOTO_PATH = str(Path.cwd() / 'img' / 'check.png')
root= tk.Tk()

image = Image.open(PHOTO_PATH)
image = image.resize((40, 40), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
my_img = tk.Label(image= photo)
my_img.image = photo
my_img.pack()

root.mainloop()