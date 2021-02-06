#! python 3
#project_1_mclip.py a multi-clipboard program

import sys
import pyperclip

text = {'agree':''' estoy deacuerdo, me parece muy bien''',
        'busy' :''' Lo siento estoy muy ocupado ahora,podemos hacerlo mas tarde?''',
        'upsel':''' le gustaria hacer un pago extra por donacion?'''
        }

if len(sys.argv) < 2:
    print('usage:python mclip.py [keyphrase] - COPIANDO TEXTO')
    sys.exit()

keyphrase = sys.argv[1] #first command line arg is the keyphrase.

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('el texto ' + keyphrase + ' fue copiado al portapapeles')
else:
    print('no hay palabra para ' + keyphrase )
    