#! python 3
'''
primenumber.py Check if a number is a prime number.
'''


def check_if_its_prime_number(number):
    cont = 0

    for division in range(1, number + 1):
        if number % division == 0:
            cont += 1

    if cont > 2 or cont == 1:
        return False

    return True


lista = []
for number in range(1, 100):
    lista.append(number)

for number in lista:
    if check_if_its_prime_number(number):
        print(f'the number {number} is a Prime')
    else:
        print((f'the number {number} is not!! a Prime'))
