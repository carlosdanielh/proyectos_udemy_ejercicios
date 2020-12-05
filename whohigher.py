import random
import os
from logowhohigher import logo, vs_logo
from data_whohigher import data


def random_number():
    ''' will return a number from 0 to 49, due to our list have from a to 49
    index, total of 50'''
    return random.randint(0, 49)


compare_a = data[random_number()]
vs = data[random_number()]
count_score = 0
chose_higher = False
game_over = False
while not game_over:
    os.system('cls')
    print(logo)
    name = compare_a['name']
    description = compare_a['description']
    country = compare_a['country']
    if chose_higher:
        print(f"You're right! Current score: {count_score}.")
    print(f'Compare A: {name}, a {description}, from {country}')

    print(vs_logo)
    name_vs = vs['name']
    description_vs = vs['description']
    country_vs = vs['country']
    print(f'Against B: {name_vs}, a {description_vs}, from {country_vs}')

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    followers_A = compare_a['follower_count']
    followers_B = vs['follower_count']
    # check_if_is_higher(followers_A, followers_B)

    if answer == 'a':
        if followers_A > followers_B:
            count_score += 1
            chose_higher = True
            vs = data[random_number()]
            name_vs = vs['name']
            description_vs = vs['description']
            country_vs = vs['country']
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {count_score}")
            game_over = True
    else:
        if followers_B > followers_A:
            count_score += 1
            chose_higher = True
            compare_a = data[random_number()]
            name = vs['name']
            description = vs['description']
            country = vs['country']
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {count_score}")
            game_over = True
