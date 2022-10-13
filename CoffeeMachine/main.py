# import statements
from art import logo
from machine_data import MENU, resources
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01
# TODO 1:Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO 2:Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3:Print report.When the user enters “report” to the prompt, a report should be generated that shows.
# TODO 4:Check resources sufficient?
# TODO 5:Process coins
# TODO 6:Check transaction successful?
# TODO 7:Make Coffee


def get_input():
    return input("What would you like? (espresso/latte/cappuccino/off/report):").lower()


# Get the cost of coffee
def get_coffee_cost(coffee_name):
    return MENU[coffee_name]['cost']


# Return Required Milk
def get_required_milk(coffee_name):
    return MENU[coffee_name]['ingredients']['milk']


# Return Required Coffee
def get_required_coffee(coffee_name):
    return MENU[coffee_name]['ingredients']['coffee']


# Return Required Water
def get_required_water(coffee_name):
    return MENU[coffee_name]['ingredients']['water']


# Check All available resources at a time
def get_avail_resources():
    print(f"Coffee : {resources['coffee']} g")
    print(f"Milk : {resources['milk']} ml")
    print(f"Water : {resources['water']} ml")
    print(f"Money : ${resources['money']}")


# List all input option's available to the user
def list_all_options():
    inputs_list = ["OFF", "REPORT", "COFFEE", ["ESPRESSO", "LATTE", "CAPPUCCINO"]]
    for i in range(0, 3):
        if i == 2:
            print(f" + {inputs_list[i]} : {inputs_list[i+1]}")
        else:
            print(f" + {inputs_list[i]}")


# return Total money entered by the user
def process_coins():
    print("Please insert coins.")

    quarters_no = int(input("How many quarters?: "))
    dimes_no = int(input("How many nickels?: "))
    nickels_no = int(input("How many nickels?: "))
    pennies_no = int(input("How many nickels?: "))

    total_money = (QUARTER * quarters_no) + (DIME * dimes_no) + (NICKEL * nickels_no) + (PENNY * pennies_no)
    return total_money


# process the transaction after coffee is selected and money entered
def process_transaction(coffee_name):
    coffee_cost = get_coffee_cost(coffee_name)
    avail_coffee = resources['coffee']
    avail_water = resources['water']
    avail_milk = resources['milk']

    if avail_coffee >= get_required_coffee(coffee_name):
        resources['coffee'] -= get_required_coffee(coffee_name)
    else:
        print("Sorry! Not enough coffee in machine ")
        return
    if avail_water >= get_required_water(coffee_name):
        resources['water'] -= get_required_water(coffee_name)
    else:
        print("Sorry! Not enough water in machine ")
        return
    if coffee_name != "espresso":
        if avail_milk >= get_required_milk(coffee_name):
            resources['milk'] -= get_required_milk(coffee_name)
        else:
            print("Sorry! Not enough milk in machine ")
            return

    money = process_coins()
    if money >= coffee_cost:
        resources['money'] += coffee_cost
        money -= coffee_cost
        money = round(money, 2)
        print(f"Here is your ${money} change")
        print(f"Here is your {coffee_name} coffee ☕. Enjoy!")

    else:
        print("Sorry! That's not enough money. Money refunded!")


# Main code to run the machine
def coffee_machine():
    print("Welcome ! Please select one of the following!")
    list_all_options()
    user_input = get_input()
    if user_input == "off":
        return False

    if user_input == "espresso":
        process_transaction(user_input)
    elif user_input == "cappuccino":
        process_transaction(user_input)
    elif user_input == "latte":
        process_transaction(user_input)
    elif user_input == "report":
        get_avail_resources()
    else:
        print(" *** Invalid Input. Try again! ***")
    return True


should_continue = True
print(logo)

while should_continue:
    should_continue = coffee_machine()
    if not should_continue:
        break
    option = input("Do you want to use Coffee Machine again 'y' or 'n': ").lower()
    if option != 'y':
        should_continue = False
