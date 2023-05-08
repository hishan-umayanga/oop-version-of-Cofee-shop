from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating some  objects from the classes and store inside the variable
# name for the object sams as the class name but use lower_case
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
drink_menu = Menu()
is_work = True
# if you want to generate report - select the object and call the method
# money_machine.report()


while is_work:
    option = drink_menu.get_items()
    user_input = input(f"What would you like? {option} : ")
    if user_input == "off":
        is_work = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = drink_menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
