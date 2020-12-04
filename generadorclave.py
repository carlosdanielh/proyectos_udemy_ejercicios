#! python 3
'''
Password Generator Project
'''
import random


def genera_password(lista, longitud):
    lista_new = []
    for number in range(longitud):
        lista_new.append(random.choice(lista))

    return lista_new


letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

lista_password = []
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

lista_password.extend(genera_password(letters, nr_letters))
lista_password.extend(genera_password(symbols, nr_symbols))
lista_password.extend(genera_password(numbers, nr_numbers))

random.shuffle(lista_password)
password = ''.join(lista_password)
print(f'your password is {password}')
