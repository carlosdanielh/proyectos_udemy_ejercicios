#!python 3
'''############################ steps to follow ###############################

- Deal both user and computer a starting hand of 2 random card values.  
-Detect when computer or user has a blackjack. (Ace + 10 value card).
-If computer gets blackjack, then the user loses (even if the user also has a 
blackjack).
-If the user gets a blackjack, then they win (unless the computer also has a
blackjack). 
-Calculate the users and computers scores based on their card values. 
-If an ace is drawn, count it as 11. But if the total goes over 21, count the 
ace as 1 instead.
-Reveal computers first card to the user.
-Game ends immediately when user score goes over 21 or if the user or computer
gets a  blackjack.   
-Ask the user if they want to get another card.  
-Once the user is done and no longer wants to draw any more cards, let the
computer play.
-The computer should keep drawing cards unless their score goes over 16.
-Compare user and computer scores and see if its a win, loss, or draw.
-Print out the players and computers final hand and their scores at the end of 
the game.  
-After the game ends, ask the user if theyd like to play again. Clear
the console for a fresh start.
###############################################################################
'''
import random
import os


def value_of_deck(card):
    if card in ['J', 'Q', 'K']:
        return cards[card]
    elif card == 'A':
        return random.choice(cards['A'])
    else:
        return card


def return_random_card(card):
    deck = list(card.keys())
    return random.choice(deck)


def black_jack(card):
    if sum_(card) == 21:
        return True
    return False


def sum_(card):
    count_A = card.count('A')
    add = 0

    for deck in card:
        if deck != 'A':
            add += value_of_deck(deck)

    if add <= 10 and count_A == 1:
        add += 11
    elif add > 10 and count_A >= 1:
        add += count_A

    return add


def show_current_score(players_cards, sum_players_cards, computers_cards):
    print(f'Your cards: {players_cards},'
          f'current score: {sum_players_cards}')
    print(f'Computer\'s first card: {computers_cards[0]}')
    print('---------------------------------------------')


def show_final_score(players_cards, sum_players_cards,
                     computers_cards, sum_computers_cards):
    print(f'Your final hand: {players_cards}, final score:'
          f'{sum_players_cards}')
    print(f'     Computer\'s final hand: {computers_cards},'
          f'final score: {sum_(computers_cards)}')
    print('---------------------------------------------')


def game():

    os.system('cls')

    players_cards = []
    computers_cards = []
    want_play = True
    while want_play:

        for times in range(2):
            players_cards.append(return_random_card(cards))
            computers_cards.append(return_random_card(cards))

        show_current_score(players_cards, sum_(players_cards), computers_cards)

        print('for debugger propose this is the second computer\'s card --> '
              f'{computers_cards[1]}\n')

        if black_jack(computers_cards)\
           or black_jack(players_cards):
            want_play = False
            if black_jack(computers_cards):
                print('YOU LOST!!! BLACK JACK FOR COMPUTER LOL')
            elif black_jack(players_cards):
                print('YOU WIN!!! BLACK JACK  COOL')

        while want_play:
            want_other_card = input('Type \'y\' to get another card, type'
                                    '\'n\' to pass: ')
            if want_other_card == 'y':
                players_cards.append(return_random_card(cards))
                show_current_score(players_cards, sum_(players_cards),
                                   computers_cards)

                if sum_(players_cards) > 21:
                    print('YOU LOST!!! POOR OF YOU')
                    show_final_score(players_cards, sum_(players_cards),
                                     computers_cards, sum_(computers_cards),)
                    want_play = False

            else:
                sum_(computers_cards)
                while sum_(computers_cards) <= 16:
                    computers_cards.append(return_random_card(cards))

                if sum_(players_cards) > sum_(computers_cards) or\
                        sum_(computers_cards) > 21:
                    print('YOU WIN!!! COOL :)')
                elif sum_(computers_cards) > sum_(players_cards) or\
                        sum_(players_cards) > 21:
                    print('YOU LOST!!! TRY AGAIN CHAMPION')
                else:
                    print('DRAWN !!! WHAT A SHAME')

                show_final_score(players_cards, sum_(players_cards),
                                 computers_cards, sum_(computers_cards),)
                want_play = False

        want_play = input('another round \'y\' or \'no\'?: ')

        if want_play == 'n':
            exit()
        elif want_play == 'y':
            game()


cards = {
    'A': [11, 1],
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    'J': 10,
    'Q': 10,
    'K': 10,
         }

game()
