#!python 3
''' 
auction.py a project from udemy to create a auction.

'''
import os

##############################FUNCTIONS########################################


def logo():
    print(
    '''
                                          ""                              
                                    ,d    ""                          
                                    88                                
,adPPYYba, 88       88  ,adPPYba, MM88MMM 88  ,adPPYba,  8b,dPPYba,   
""     `Y8 88       88 a8"     ""   88    88 a8"     "8a 88P'   `"8a  
,adPPPPP88 88       88 8b           88    88 8b       d8 88       88  
88,    ,88 "8a,   ,a88 "8a,   ,aa   88,   88 "8a,   ,a8" 88       88  
`"8bbdP"Y8  `"YbbdP'Y8  `"Ybbd8"'   "Y888 88  `"YbbdP"'  88       88  
    '''
         )


def add_bidders(name, bid):
    bidders[name] = bid


def clear():
    os.system('cls')


def look_for_highest_bidder(dictionary):
    higher = 0
    for keys, values in dictionary.items():
        if values > higher:
            higher = dictionary[keys]
            key = keys
    return key
############################END-FUNCTIONS######################################


bidders = {}
Finished = False
logo()

while not Finished:
    name = input('what\'s your name?: ')
    bid = int(input('what\'s your bid?: $'))

    add_bidders(name, bid)

    Finished = input('there\'s another bidder? yes or no: ')

    if Finished == 'yes':
        Finished = False
        os.system('cls')

bidder = look_for_highest_bidder(bidders)
amount = bidders[bidder]

print(f'the highest bidder was {bidder} with ${amount} ')
