from PIL import ImageTk, Image
# import tkinter as tk
# from pathlib import Path


class PhotoMain:
    def __init__(self, path_photo, width, height):
        self.path = path_photo
        self.width = width
        self.height = height

    def draw_image(self):
        image = Image.open(self.path)
        image = image.resize((self.width, self.height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        return photo
        # lab = tk.Label(root, image=photo)
        # lab.image = photo
        # lab.pack()
        # root.mainloop()