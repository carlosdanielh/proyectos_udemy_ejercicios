from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu_coffee = Menu()
cash_machine = MoneyMachine()
turn_off = False
while not turn_off:
    coffee_avalible = menu_coffee.get_items()
    type_coffee = input(f'What would you like? {coffee_avalible}: ').lower()

    if type_coffee == 'off':
        turn_off = True
    elif type_coffee == 'report':
        coffee_maker.report()
        cash_machine.report()

    coffee = menu_coffee.find_drink(type_coffee)
    if coffee != None:
        if coffee_maker.is_resource_sufficient(coffee):            
            if cash_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)