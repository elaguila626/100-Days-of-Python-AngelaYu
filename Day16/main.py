from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# MenuItem is the class or blueprint
# Item is the new object created
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_selects = input(f"What would you like {options}?")
    if user_selects == 'report':
        money_machine.report()
        coffee_maker.report()
    elif user_selects == 'off':
        is_on = False
    else:
        #menu.find_drink(user_selects)returns an object not a string
        drink = menu.find_drink(user_selects)
        if money_machine.make_payment(drink.cost) and coffee_maker.is_resource_sufficient(drink) == True:
            coffee_maker.make_coffee(drink)
        else:
            is_on = False
















