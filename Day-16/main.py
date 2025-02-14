from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    my_order = input(f"What would you like? ({menu.get_items()}): ").lower()

    if my_order == 'report':
         coffee_maker.report()
         money_machine.report()

    elif my_order == 'off':
        print("GOOD BYE!")
        is_on = False
    else:
        drink = menu.find_drink(my_order)
        if coffee_maker.is_resource_sufficient(drink):
            if drink in menu.menu:
                cost = drink.cost
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(drink)
