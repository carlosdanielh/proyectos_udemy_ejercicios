import random
import os
from logowhohigher import logo, vs
from data_whohigher import data


def choose_a_random_celebrety():
    return random.choice(data)


def print_user(dictionary, option):
    name = dictionary['name']
    description = dictionary['description']
    country = dictionary['country']

    if option == 'a':
        return print(f'Compare A: {name}, a {description}, from {country}')
    else:
        return print(f'Agains B: {name}, a {description}, from {country}')


def followers(dictionary):
    return dictionary['follower_count']


option_a = choose_a_random_celebrety()
option_b = choose_a_random_celebrety()
count_score = 0
chose_higher = False
game_over = False
while not game_over:
    os.system('cls')
    print(logo)
    print(f'for debugger propose A has: {followers(option_a)} '
          f'followers and B has {followers(option_b)} followers')
    if chose_higher:
        print(f"You're right! Current score: {count_score}.")
    print_user(option_a, 'a')
    print(vs)
    print_user(option_b, 'b')

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == 'a' and followers(option_a) > followers(option_b) or\
       answer == 'b' and followers(option_b) > followers(option_a):
        count_score += 1
        chose_higher = True
        option_a = option_b
        option_b = choose_a_random_celebrety()
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {count_score}")
        game_over = True
