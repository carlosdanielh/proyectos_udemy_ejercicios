import random
import os
from logowhohigher import logo, vs_logo
from data_whohigher import data


def random_number():
    ''' will return a number from 0 to 49, due to our list have from a to 49
    index, total of 50'''
    return random.randint(0, 49)


option_a = data[random_number()]
name = option_a['name']
description = option_a['description']
country = option_a['country']
followers_A = option_a['follower_count']

option_b = data[random_number()]
name_vs = option_b['name']
description_vs = option_b['description']
country_vs = option_b['country']
followers_B = option_b['follower_count']

count_score = 0
chose_higher = False
game_over = False
while not game_over:
    os.system('cls')
    print(logo)
    print(f'for debugger propose A has: {followers_A}'
          f'followers  and B has {followers_B} followers')
    if chose_higher:
        print(f"You're right! Current score: {count_score}.")
    print(f'Compare A: {name}, a {description}, from {country}')
    print(vs_logo)
    print(f'Against B: {name_vs}, a {description_vs}, from {country_vs}')
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == 'a':
        if followers_A > followers_B:
            count_score += 1
            chose_higher = True

            option_b = data[random_number()]
            name_vs = option_b['name']
            description_vs = option_b['description']
            country_vs = option_b['country']
            followers_B = option_b['follower_count']
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {count_score}")
            game_over = True
    else:
        if followers_B > followers_A:
            count_score += 1
            chose_higher = True

            name = option_b['name']
            description = option_b['description']
            country = option_b['country']
            followers_A = option_b['follower_count']

            option_b = data[random_number()]            
            name_vs = option_b['name']
            description_vs = option_b['description']
            country_vs = option_b['country']
            followers_B = option_b['follower_count']
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {count_score}")
            game_over = True
