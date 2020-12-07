from data_coffe import MENU, resources

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


def check_resources(type_of_coffee, resources):

    ingredients_menu = MENU[type_of_coffee]['ingredients'].keys()

    for ingredients in ingredients_menu:
        ingredient_of_coffee_selected =\
             MENU[type_of_coffee]['ingredients'][ingredients]
        for resource in resources:
            if ingredients == resource and\
                 resources[ingredients] / ingredient_of_coffee_selected < 1:
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


def validate_if_enough_money_to_buy_coffe(type_, amount_provided):
    real_cost_of_coffe = MENU[type_]['cost']
    if amount_provided >= real_cost_of_coffe:
        return True
    return False


def change(money_given, type_):
    return money_given - MENU[type_]['cost']


def update_resources(resources, type_of_coffee):
    for ingredients in MENU[type_of_coffee]['ingredients']:
        for resource in resources:
            if ingredients == resource:
                resources[ingredients] -=\
                     MENU[type_of_coffee]['ingredients'][ingredients]


def ingredients_in_resources(resources, type_of_coffee):
    list_ingredients = []
    for ingredients in MENU[type_of_coffee]['ingredients']:
        ingredient_of_coffee_selected =\
             MENU[type_of_coffee]['ingredients'][ingredients]
                               
        for resource in resources:
            if ingredients == resource and\
                 resources[ingredients] / ingredient_of_coffee_selected <= 1:
                list_ingredients.append(ingredients)
    return list_ingredients


total_money_earned = 0
turn_off = False
while not turn_off:
    exist_type_of_coffe = False
    while not exist_type_of_coffe:
        type_ = input('What would you like?'
                      '(espresso/latte/cappuccino): ').lower()
        exist_type_of_coffe = verify_type_of_coffe(type_)

    if type_ == 'report':
        show_report(resources, total_money_earned)

    elif type_ in ['espresso', 'latte', 'cappuccino'] and\
            check_resources(type_, resources):
        print('please insert coint: ')
        quarters = int(input('how many quarters?: '))
        dimes = int(input('how many dimes?: '))
        nickles = int(input('how many nickles?: '))
        pennies = int(input('how many pennies?: '))

        amount = add_coints(quarters, dimes, nickles, pennies)
        cost_coffe = MENU[type_]['cost']
        amount = float('{:.2f}'.format(amount))
        print(f'total:{amount} the coffe cost: {cost_coffe} ')

        if validate_if_enough_money_to_buy_coffe(type_, amount):
            update_resources(resources, type_)
            total_money_earned += cost_coffe
            if change(amount, type_) > 0:
                money_change = change(amount, type_)
                print('Here is {:.2f} in change.'.format(money_change))
                print('Here is your espresso ☕️. Enjoy!')
            else:
                print('Here is your espresso ☕️. Enjoy!')
        else:
            print('Sorry that\'s not enough money. Money refunded.')

    elif type_ in ['espresso', 'latte', 'cappuccino'] and not\
            check_resources(type_, resources):

        ingredients = ingredients_in_resources(resources, type_)
        print(f'Sorry there is not enough {ingredients}.')

    else:
        turn_off = True
