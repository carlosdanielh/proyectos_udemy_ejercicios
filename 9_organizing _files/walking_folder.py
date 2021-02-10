import os
from pathlib import Path

the_path = str(Path('c:/n'))

a = []
print(f'the currect folder name is {the_path} ')
print('and has this folder inside')
for folder_name, sub_folders, file_names in os.walk(the_path):
    print(f'folder:  {folder_name} ')    
    # sub_folders return a list of the subfolder
    for sub in file_names:
        print(f'sub_folders in {folder_name}>  {sub} ')
    # file_names return a list of the files of the folder
    # print(f'file_names: {file_names}')
        for files in file_names:
            print(f'files in {folder_name}>  {files} ')
            print('-' * 10)
# for folder_name, sub_folders, file_names in os.walk(the_path):
#     print(f'sub_folder:  {sub_folders} ')