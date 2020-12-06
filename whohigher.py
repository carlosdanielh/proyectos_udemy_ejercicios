import random
import os
from logowhohigher import logo, vs
from data_whohigher import data


def random_number():
    ''' will return a number from 0 to 49, due to our list have from a to 49
    index, total of 50'''
    return random.randint(0, 49)


# user a
option_a = data[random_number()]
name_a = option_a['name']
description_a = option_a['description']
country_a = option_a['country']
followers_a = option_a['follower_count']

# user b
option_b = data[random_number()]
name_b = option_b['name']
description_b = option_b['description']
country_b = option_b['country']
followers_b = option_b['follower_count']

count_score = 0
chose_higher = False
game_over = False
while not game_over:
    os.system('cls')
    print(logo)
    print(f'for debugger propose A has: {followers_a} '
          f'followers and B has {followers_b} followers')
    if chose_higher:
        print(f"You're right! Current score: {count_score}.")
    print(f'Compare A: {name_a}, a {description_a}, from {country_a}')
    print(vs)
    print(f'Against B: {name_b}, a {description_b}, from {country_b}')
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == 'a':
        if followers_a > followers_b:
            count_score += 1
            chose_higher = True

            name_a = option_b['name']
            description_a = option_b['description']
            country_a = option_b['country']
            followers_a = option_b['follower_count']

            option_b = data[random_number()]
            name_b = option_b['name']
            description_b = option_b['description']
            country_b = option_b['country']
            followers_b = option_b['follower_count']
        else:
            chose_higher = False
    else:
        if followers_b > followers_a:
            count_score += 1
            chose_higher = True

            name_a = option_b['name']
            description_a = option_b['description']
            country_a = option_b['country']
            followers_a = option_b['follower_count']

            option_b = data[random_number()]
            name_b = option_b['name']
            description_b = option_b['description']
            country_b = option_b['country']
            followers_b = option_b['follower_count']
        else:
            chose_higher = False

    if not chose_higher:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {count_score}")
        game_over = True
