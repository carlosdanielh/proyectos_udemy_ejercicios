import random


def introduction():
    return f'''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is {guess_number()}'''


def guess_number():
    return random.randint(1, 100)


EASY = 10
HARD = 5

print(introduction())
difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

if difficulty == 'easy':
    times_attempts = EASY
else:
    times_attempts = HARD

print(f'You have {times_attempts} attempts remaining to guess the number.')

number_to_guess = guess_number()
run_out_of_attempts = False
while not run_out_of_attempts:
    make_guess = int(input('Make a guess: '))

    if make_guess > number_to_guess:
        print('Too high.')
        times_attempts -= 1
    elif make_guess < number_to_guess:
        print('Too low.')
        times_attempts -= 1
    else:
        print(f'you got it! the answer was {number_to_guess}')
        break

    if times_attempts != 0:        
        print('Guess again.')
        print(f'You have {times_attempts} attempts remaining to guess the'
              'number.')
    else:
        run_out_of_attempts = True
        print('You\'ve run out of guesses, you lose.')
