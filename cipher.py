#! python 3
'''
cipher.py code and decode with cipher method.
'''

'''#############################functions###################################'''


def list_cipher(shift):
    start = 65 + shift
    end = start
    cipher_list = []

    for number in range(start, 91):
        cipher_list.append(chr(number).lower())

    for number in range(65, end):
        cipher_list.append(chr(number).lower())

    return cipher_list


def list_alphabet():
    alphabet = []

    for number in range(65, 91):
        alphabet.append(chr(number).lower())

    return alphabet


def code_cipher(string, shift, code_decode):
    alphabet = list_alphabet()
    cipher = list_cipher(shift)
    size_alphabet = len(alphabet)
    code = ''

    for char in string:
        if char in alphabet:
            if code_decode == 'code':
                for pocision in range(size_alphabet):
                    if char == alphabet[pocision]:
                        code += cipher[pocision]
            else:
                for pocision in range(size_alphabet):
                    if char == cipher[pocision]:
                        code += alphabet[pocision]
        else:
            code += char

    return code


'''##########################ends functions#################################'''
answer = 'y'
while answer != 'n':
    types = input('code or decode?: ').lower()
    string = input('what is the word?: ').lower()
    shift = int(input('number of shift?: '))
    codes = code_cipher(string, shift, types)

    if types == 'code':        
        print(f'your word in cipher is: {codes}')
    else:
        print(f'your word decode in cipher is: {codes}')

    answer = input('would you like to continue y or n?: ')
