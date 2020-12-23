list_names = []

with open('..\\ejercicios\\udemy_projects\\letters\\Input\\Names\\'
          'invited_names.txt') as file_names:
    names = file_names.readlines()

    for name in names:
        new_name = name.strip()
        list_names.append(new_name)

for name in list_names:
    with open('..\\ejercicios\\udemy_projects\\letters\\Input\\Letters\\'
              'starting_letter.docx') as replace_file:
        letter = replace_file.read()
        letter_replaced = letter.replace('[name]', name)

        with open(f'..\\ejercicios\\udemy_projects\\letters\\Output\\'
                  f'ReadyToSend\\letter_for_{name}', 'w') as document_letter:
            document_letter.write(letter_replaced)
