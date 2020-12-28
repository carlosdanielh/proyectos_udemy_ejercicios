from pathlib import Path
import os


phrase = input('which phrase would you like to find in "find directory?"')
list_found = []
this_path = str(Path('C://') / 'find')
for filename in os.listdir(this_path):
    path_file = str(Path(this_path) / filename)
    count = 0
    with open(path_file) as file_open:
        all_text = file_open.read().lower()

    count = all_text.count(phrase.lower())

    if count > 0:
        list_found.append([filename, count])

if len(list_found) > 0:
    print(f'the phrase {phrase} was found in these files...')

    for index, filename in enumerate(list_found):
        file_name = list_found[index][0]
        times = list_found[index][1]
        print(f'{index + 1}. {file_name} , {phrase} was found {times} times')
else:
    print('No ocurrences were found!!')
