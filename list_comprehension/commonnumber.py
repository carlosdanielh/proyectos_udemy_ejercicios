from pathlib import Path


def list_element_from_textfile(filename):
    with open(Path() / filename) as file_open:
        list_file = file_open.readlines()
        new_list_file = [element.strip() for element in list_file]
    return new_list_file


list_file1 = list(set(list_element_from_textfile('file1.txt')))
list_file2 = list(set(list_element_from_textfile('file2.txt')))

print(list_file1)
print(list_file2)


common_number_list = [n for n in list_file2 if n in list_file1]

print(common_number_list)