#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.
# import pdb; pdb.set_trace()
if len(sys.argv) == 3:
    option = sys.argv[1]
    phrase = sys.argv[2]
    if option.lower() == 'save':
        mcbShelf[phrase] = pyperclip.paste()
    if option.lower() == 'delete':
        mcbShelf.pop(phrase)
elif len(sys.argv) == 2:
    option = sys.argv[1]
    if option.lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif option.lower() == 'delete':
        mcbShelf.clear()
        pyperclip.copy('all list was deleted')
    else:
        phrase_to_load = option
        pyperclip.copy(mcbShelf[phrase_to_load])

# TODO: List keywords and load content.

mcbShelf.close()
