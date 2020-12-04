import random
from os import system, name
 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
 
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'Q', 'K', 'J']
 
def rand_choice():
    rand_num = random.choice(cards)
    return rand_num
 
 
def deal(players_card, computers_card ):
        players_card.append(rand_choice())
        computers_card.append(rand_choice())
 
def winner(players_card, computers_card):
    
    player_total = player_score(players_card)
    computer_total = player_score(computers_card)
 
 
    if player_total > 21 :
        print(f'You Lose : {player_total} \nComputer Wins : {computer_total}')
 
    elif player_total <= 21 and computer_total > 21 :
        print(f'You Win : {player_total} \nComputer lose : {computer_total}')
 
    elif abs(21 - player_total) > abs(21 - computer_total) :
        print(f'You Lose : {player_total} \nComputer Wins : {computer_total}')
 
    elif abs(21 - player_total) < abs(21 - computer_total) :
        print(f'You Win : {player_total} \nComputer lose : {computer_total}')
 
    else:
        print(f'Your Total : {player_total} \nComputer Total : {computer_total}, Draw !')
    
def player_score(player_hand):
    total = 0
    for position in range(len(player_hand)):
        letter = player_hand[position]
        
        if letter in ['Q','K','J']:
            total += 10
        elif type(letter) == int:
            total += letter
        elif letter == 'A' and total <= 10 and player_hand.count('A') < 2 :
            total += 11
        else:
            letter == 'A' and total >= 10 and player_hand.count('A') >= 1
            total += 1
 
    return total
 
def black_jack():
    
    your_cards = []
    computer_cards = []
    
    player_total_score = 0
    computer_total_score = 0
 
    play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    #clear()
 
    if play == 'y':
            deal(your_cards, computer_cards)
            print(f'Your Cards: {your_cards}')
            print(f'Computer Cards: {computer_cards}')
            player_total_score = player_score(your_cards)
            computer_total_score = player_score(computer_cards)
            print(player_total_score)
            print(computer_total_score)
            
            end_of_play = False
            while not end_of_play:
 
                if player_total_score < 21 and computer_total_score < 21:
                   
                    user_choice = input("would you like to deal again, 'y' or 'n' :")
                    
                    if user_choice == 'y':
                        #clear()
                        end_of_play = False
                        deal(your_cards, computer_cards)
                        #your_cards.append(rand_choice())
                        player_total_score = player_score(your_cards)
                        computer_total_score = player_score(computer_cards)
                        print(f'your hand : {your_cards}')
                        print(f'Computer hand : {computer_cards}')
                        print(player_total_score)
                        print(computer_total_score)
                    
                    else:
                        player_total_score = player_score(your_cards)
                        computer_total_score = player_score(computer_cards)
                        if computer_total_score < 17 :
                            computer_cards.append(rand_choice())
                            print(your_cards)
                            print(computer_cards)
                            winner(your_cards,computer_cards)
                            end_of_play = True
                            black_jack()
                        else:
                            print(your_cards)
                            print(computer_cards)
                            winner(your_cards,computer_cards)
                            end_of_play = True
                            black_jack()
 
                elif player_total_score == 21 or computer_total_score == 21:
                    print(your_cards)
                    print(computer_cards)
                    winner(your_cards,computer_cards)
                    end_of_play = True
                    black_jack()
 
                else:
                    print(your_cards)
                    print(computer_cards)
                    winner(your_cards,computer_cards)
                    end_of_play = True
                    black_jack()
    
    else:
        end_of_play = True
 
black_jack()