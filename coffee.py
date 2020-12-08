#!python 3

from data_coffe import MENU, resources

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

def is_there_resources(type_of_coffee, resources):

    ingredients_coffee = type_of_coffee['ingredients']

    for ingredients in ingredients_coffee:
        if resources[ingredients] / ingredients_coffee[ingredients] < 1:
            return False
    return True


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
    if type_of_coffe not in\
                          ['espresso', 'latte', 'cappuccino', 'report', 'off']:
        return False
    return True


def add_coints(quarters, dimes, nickles, pennies):
    return quarters * QUARTERS + dimes * DIMES +\
           nickles * NICKLES + pennies * PENNIES


def is_enough_money_to_buy_coffe(type_coffee, amount_provided):
    real_cost_of_coffe = type_coffee['cost']
    if amount_provided >= real_cost_of_coffe:
        return True
    return False


def change(money_given, type_coffee):
    return money_given - type_coffee['cost']


def update_resources(resources, type_of_coffee):
    coffee = type_of_coffee['ingredients']
    for ingredients in type_of_coffee['ingredients']:
        resources[ingredients] -= coffee[ingredients]


def ingredients_in_resources(resources, type_of_coffee):
    list_ingredients = []
    for ingredients in type_of_coffee['ingredients']:
        ingredient_selected = type_of_coffee['ingredients'][ingredients]
        if resources[ingredients] / ingredient_selected <= 1:
            list_ingredients.append(ingredients)
    return list_ingredients


total_money_earned = 0
turn_off = False
while not turn_off:
    exist_type_of_coffe = False
    while not exist_type_of_coffe:
        type_coffee = input('What would you like?'
                            '(espresso/latte/cappuccino): ').lower()
        exist_type_of_coffe = verify_type_of_coffe(type_coffee)

    if type_coffee != 'off':

        if type_coffee != 'report':
            type_coffee = MENU[type_coffee]

        if type_coffee == 'report':
            show_report(resources, total_money_earned)
        elif is_there_resources(type_coffee, resources):
            print('please insert coint: ')
            quarters = int(input('how many quarters?: '))
            dimes = int(input('how many dimes?: '))
            nickles = int(input('how many nickles?: '))
            pennies = int(input('how many pennies?: '))
            amount = add_coints(quarters, dimes, nickles, pennies)
            cost_coffe = type_coffee['cost']
            amount = round(amount, 2)
            print(f'total:{amount} the coffe cost: {cost_coffe} ')

            if is_enough_money_to_buy_coffe(type_coffee, amount):
                update_resources(resources, type_coffee)
                total_money_earned += cost_coffe
                if change(amount, type_coffee) > 0:
                    money_change = round(change(amount, type_coffee), 2)
                    print(f'Here is {money_change} in change.')
                    print('Here is your espresso ☕️. Enjoy!')
                else:
                    print('Here is your espresso ☕️. Enjoy!')
            else:
                print('Sorry that\'s not enough money. Money refunded.')
        elif not is_there_resources(type_coffee, resources):
            ingredients = ingredients_in_resources(resources, type_coffee)
            print(f'Sorry there is not enough {ingredients}.')
    else:
        turn_off = True
