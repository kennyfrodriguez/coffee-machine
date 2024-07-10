from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome to the Coffee Machine! \n")
in_service = True
while in_service:
    selection = input("What would you like? : " + menu.get_items()).lower()
    if selection == "off":
        in_service = False
    elif selection == "report":
        print("Current Report:")
        print(coffee_maker.report())
    elif selection == "latte" or selection == "espresso" or "cappuccino":
        drink = (menu.find_drink(selection))
        print("Excellent. This drink will cost $" + str(drink.cost))
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
