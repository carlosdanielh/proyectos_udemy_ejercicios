# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     }}

# print(MENU['espresso']['ingredients']['coffee'])
# print(MENU['espresso']['ingredients']['water'])
# print(MENU['espresso']['cost'])
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


def show_report(resources, total_money):
    money = total_money
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    print(f'Water: {water}')
    print(f'Milk: {milk}')
    print(f'Coffee: {coffee}')
    print(f'Money: {money}')


def verify_type_of_coffe(type_of_coffe):
    if type_of_coffe not in ['espresso', 'latte', 'cappuccino', 'report']:
        return False
    return True


def add_coints(quarters, dimes, nickles, pennies):
    return quarters * QUARTERS + dimes * DIMES +\
           nickles * NICKLES + pennies * PENNIES


def validate_if_enough_money_to_buy_coffe(type_, amount_provided):
    real_cost_of_coffe = MENU[type_]['cost']
    if amount_provided >= real_cost_of_coffe:
        return True
    return False


def change(money_given, type_):
    return money_given - MENU[type_]['cost']


total_money_earned = 0
endless = True
while endless:
    exist_type_of_coffe = False
    while not exist_type_of_coffe:
        type_ = input('What would you like? (espresso/latte/cappuccino): ').lower()
        exist_type_of_coffe = verify_type_of_coffe(type_)

    if type_ == 'report':        
        show_report(resources, total_money_earned)
    elif exist_type_of_coffe:
        print('please insert coint: ')
        quarters = int(input('how many quarters?: '))
        dimes = int(input('how many dimes?: '))
        nickles = int(input('how many nickles?: '))
        pennies = int(input('how many pennies?: '))

        amount = add_coints(quarters, dimes, nickles, pennies)
        cost_coffe = MENU[type_]['cost']
        print(f'total:{amount} the coffe cost: {cost_coffe} ')
        
        if validate_if_enough_money_to_buy_coffe(type_, amount):
            total_money_earned += cost_coffe
            if change(amount, type_) > 0:
                money_change = change(amount, type_)             
                print(f'Here is {money_change} in change.')
                print('Here is your espresso ☕️. Enjoy!')
            else:
                print('Here is your espresso ☕️. Enjoy!')

        else:
            print('Sorry that\'s not enough money. Money refunded.')
    else:
        exist_type_of_coffe = False
