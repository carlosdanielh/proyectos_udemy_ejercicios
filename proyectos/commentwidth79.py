#! python 3
'''commentwidht79.py is a project that permit to copy a string and when you
execute the project it will paste it in a formatted width 70 with, between
comments'''

import pyperclip
import textwrap

pasted_text = pyperclip.paste()

wrapper = textwrap.TextWrapper(width=79)

cadena = "'''" + pasted_text + "'''"
cadena = wrapper.fill(text=cadena)
pyperclip.copy(cadena)
