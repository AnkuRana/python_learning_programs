from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from prettytable import PrettyTable
from os import system


# Ask input from user
def ask_user():
    return input("What would you like espresso/cappuccino/latte or "
                 "'report:\"complete report\" or "
                 "profit:\" current profit\": ").lower()


# starting message as we start the coffee machine project
def welcome_msg():
    print("Welcome to the coffee vending machine..")
    list_item = Menu()
    items = list_item.get_items().split("/")
    # remove last item as it is just empty space
    items.pop()
    menu_table = PrettyTable()
    menu_table.add_column("Index", ["1.", "2.", "3."])
    menu_table.add_column("Items", items)
    menu_table.align = "l"
    print(menu_table)


def coffee_machine(menu_name_var, money_var, coffee_var):
    should_continue = True
    while should_continue:
        welcome_msg()
        # get user choice
        choice = ask_user()
        drink_ordered = menu_name.find_drink(choice)

        if choice == 'report':
            coffee.report()
        elif choice == 'profit':
            money.report()
        elif drink_ordered:
            if coffee.is_resource_sufficient(drink_ordered) and money.make_payment(drink_ordered.cost):
                coffee.make_coffee(drink_ordered)
        else:
            print("you have entered a invalid input !")

        get_user_input = input("Do you want to continue 'y' or 'n' or : ").lower()
        if get_user_input != 'y':
            should_continue = False
        system('cls')


print(logo)
# creating the object of Menu class
menu_name = Menu()
# creating object of MoneyMaking class
money = MoneyMachine()
# creating object of CoffeeMaker class
coffee = CoffeeMaker()

coffee_machine(menu_name, money, coffee)









