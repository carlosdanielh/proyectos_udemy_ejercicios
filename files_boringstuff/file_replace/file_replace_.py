#! python 3
# file_replace.py, it will replace every ADJECTIVE, NOUN, ADVERB, or VERB 
# within a text file with a user's own text
from pathlib import Path
import re

def list_of_all_occurrences(text,words_to_find):

with open(Path.cwd() / 'udemy_projects' / 'files_boringstuff' / 'pro' /
          'replace.txt') as file_replace:
    all_text = file_replace.read()
    
