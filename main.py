from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
machine_switch = True


while machine_switch:
    response = input(f"What would you like? ({menu.get_items()})").lower()
    if response == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif response == "off":
        machine_switch = False
    else:
        drink = menu.find_drink(response)
        resource_sufficient = coffeeMaker.is_resource_sufficient(drink)
        if resource_sufficient:
            money_sufficient = moneyMachine.make_payment(drink.cost)
            if money_sufficient:
                coffeeMaker.make_coffee(drink)
