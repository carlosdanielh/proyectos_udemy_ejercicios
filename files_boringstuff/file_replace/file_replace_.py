#! python 3
# file_replace.py, it will replace every ADJECTIVE, NOUN, ADVERB, or VERB
# within a text file with a user's own text
from pathlib import Path
import re
import os
import sys


def list_of_all_occurrences(text, words_to_find):
    list_to_match = words_to_find.split(',')
    patterns = '|'.join(list_to_match)
    regex = re.compile(patterns)
    find = regex.findall(text)
    return find


os.system('cls')
with open(Path.cwd() / 'udemy_projects' / 'files_boringstuff' / 'pro' /
          'replace.txt') as file_replace:
    all_text = file_replace.read()

    list_match =\
        list_of_all_occurrences(all_text, 'ADJECTIVE,NOUN,ADVERB,VERB')

print(list_match)
print(all_text)

list_new_words = []
print("let's start replacing")
for word in list_match:
    pharse = input(f'Enter and {word}: \n')
    list_new_words.append(pharse)

answer = input('are you sure you want to make all this changes? y/n')

if answer == 'y':
    for index, new_word in enumerate(list_new_words):
        old_word = list_match[index]
        all_text = all_text.replace(old_word, new_word, 1)

    with open(Path.cwd() / 'udemy_projects' / 'files_boringstuff' / 'pro' /
              'replace.txt', 'w') as file_replace:

        file_replace.write(all_text)
else:
    sys.exit()
