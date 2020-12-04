''' Hi!
It is a rock, paper, scissors game with ascii art!
Input paper / rock / scissors, or
simply p, r, or s.
Hope you like it!
'''

# Thanks to wynand1004, whose art I borrowed from github.
arts = {
'r': 
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', 
'p':
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
's':
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

from random import choice

win = {'r': 's', 's': 'p', 'p': 'r'}
full = {'r': 'rock', 'p': 'paper', 's': 'scissors'} #diccionario del juego

def game(pl):
    while True:
        op = choice(['r', 's', 'p'])
        if win[pl] == op:
            return True, op
        elif pl == op:
            # If tie, comp chooses again
            continue
        else:
            return False, op

pl = input().lower()[0]
assert pl in ['r', 's', 'p'], 'Choose rock, scissors, or paper!'
cond, op = game(pl)
print()
print(f'You chose {full[pl]}{arts[pl]}')
print(f'Comp chose {full[op]}{arts[op]}')
print()
if cond:
    print('You win!')
else:
    print('You lose!')