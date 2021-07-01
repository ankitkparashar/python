from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
machine_is_on = True

while machine_is_on:
    choice: str = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif choice == "off":
        machine_is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
