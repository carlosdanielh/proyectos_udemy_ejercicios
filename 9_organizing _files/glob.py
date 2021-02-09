import os
from pathlib import Path

lista = (Path(Path.home() / 'Desktop')).glob('*')
lista_suffix = [file.suffix for file in lista if len(file.suffix) != 0]


for files in list(set(lista_suffix)):
    print(files)
    Path(Path.home() / 'Desktop' / (files[1:] + '_Dir')).mkdir()
