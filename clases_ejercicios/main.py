from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = MenuItem('espresso', 50, 0, 18, 1.5)
#coffee_latte = MenuItem('latte', 200, 150, 24, 2.5)
#coffee_cappuccino = MenuItem('cappuccino', 250, 100, 24, 3.0)

# machine.name = 'espresso'

print('______________________atributos')
print(coffee.name)
print(coffee.cost)
print(coffee.ingredients)

print('________________________menu')
menu_ = Menu()
print(menu_.get_items())
a = menu_.find_drink('espresso')
menu_.find_drink('cola')
print(a.name)

print('________________________coffemaker')
maker = CoffeeMaker()
maker.report()
print(maker.is_resource_sufficient(a))
maker.make_coffee(a)
maker.report()


print('________________________moneymachine')
money = MoneyMachine()
money.report()
print(money.make_payment(coffee.cost))
money.report()