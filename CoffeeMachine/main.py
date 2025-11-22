from functools import total_ordering

MENU = {"espresso": {"ingredients": {"water": 50,"coffee": 18, }, "cost": 1.5 },"latte": {"ingredients": {"water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine_money = 0
cost = 0


#TODO 2 :Report generation
def report():
    for key in  resources:
        if key == "water":
            print(f"{key}: {resources[key]}ml")
        if key == "milk":
            print(f"{key}: {resources[key]}ml")
        if key == "coffee":
            print(f"{key}: {resources[key]}g")
    print(f" Money: ${cost}")



user_total = 0
# TODO 1: Prompt user for coffee type

dont_continue = False






def espresso():
    print("This cost $ 1.5")
    if resources["water"] < 50:
        print("Sorry there is not enough water")
        global dont_continue
        dont_continue = True
    elif resources["coffee"] < 18:
        print("Sorry there is not enough coffee")
        dont_continue = True
    else:
        print("Insert coins")
        resources["water"]-=50
        resources["coffee"]-= 18

def latte():
    print("This cost $ 2.5")
    if resources["water"] < 200:
        print("Sorry there is not enough water")
        global dont_continue
        dont_continue = True
    elif resources["coffee"] < 24:
        print("Sorry there is not enough coffee")
        dont_continue = True
    elif resources["milk"] < 150:
        print("Sorry there is not enough milk")
        dont_continue = True
    else:
        print("Insert coins")
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150
def cappuccino():
    print("This cost $ 3.0")
    if resources["water"] < 250:
        print("Sorry there is not enough water")
        global dont_continue
        dont_continue = True
    elif resources["coffee"] < 24:
        print("Sorry there is not enough coffee")
        dont_continue = True
    elif resources["milk"] < 100:
        print("Sorry there is not enough milk")
        dont_continue = True
    else:
        print("Insert coins")
        resources["water"] -= 250
        resources["coffee"] -= 100
        resources["milk"] -= 200
def check_resources():
    if coffee_type == "expresso":
        if resources["water"] < 50:
            print("Sorry there is not enough water")
        elif resources ["coffee"] <18:
            print("Sorry there is not enough coffee")
        else:
            check = True
            print("All ingredients available")
    elif coffee_type == "latte":
        if resources["water"] < 200:
            print("Sorry there is not enough water")
        elif resources ["coffee"] <24:
            print("Sorry there is not enough coffee")
        elif resources["milk"] <150:
            print("Sorry there is not enough milk")
        else:
            check = True
            print("All ingredients available")
    elif coffee_type == 'cappuccino':
        if resources["water"] < 250:
            print("Sorry there is not enough water")
        elif resources ["coffee"] <24:
            print("Sorry there is not enough coffee")
        elif resources["milk"] <100:
            print("Sorry there is not enough milk")
        else:
            check = True
            print("All ingredients available")
def coins ():
    global user_total
    amount_quarters =int(input ('how many quarters are you inserting '))
    amount_dimes =int(input ('how many dimes are you inserting '))
    amount_nickles = int(input('how many nickles are you inserting '))
    amount_pennies = int(input ('how many pennies are you inserting '))
    total_quarters = amount_quarters * 0.25
    user_total += total_quarters
    total_dimes = amount_dimes * 0.10
    user_total += total_dimes
    total_nickles = amount_nickles * 0.05
    user_total += total_nickles
    total_pennies = amount_pennies * 0.01
    user_total += total_pennies
    return round(user_total)

def check_amount():
    global machine_money
    global dont_continue
    if coffee_type == "expresso":
        if user_total < MENU['expresso']['cost']:
            print("Sorry thats not enough money. Money refunded")
            dont_continue = True
        elif user_total> MENU['expresso']['cost']:
            actual_cost = round(user_total -MENU['expresso']['cost'])
            machine_money += MENU['expresso']['cost']
            print(f"Here is ${actual_cost}in change")
        else:
            machine_money += user_total
    if coffee_type == "latte":
        if user_total < MENU['latte']['cost']:
            print("Sorry thats not enough money. Money refunded")
            dont_continue = True
        elif user_total > MENU['latte']['cost']:
            actual_cost = round(user_total - MENU['latte']['cost'])
            machine_money += MENU['latte']['cost']
            print(f"Here is ${actual_cost}in change")
        else:
            machine_money += user_total
    if coffee_type == 'cappuccino':
        if user_total < MENU['cappuccino']['cost']:
            print("Sorry thats not enough money. Money refunded")
            dont_continue = True
        elif user_total > MENU['cappuccino']['cost']:
            actual_cost = round(user_total- MENU['cappuccino']['cost'])
            machine_money += MENU['cappuccino']['cost']
            print(f"Here is ${actual_cost} in change")
        else:
            machine_money += user_total


while dont_continue is False:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == 'espresso':
        cost = 1.5
    elif coffee_type == 'latte':
        cost = 2.5
    elif coffee_type == 'cappuccino':
        cost = 3.0
    if coffee_type == "latte":
        check_resources()
        latte()
    elif coffee_type == "espresso":
        check_resources()
        espresso()
    elif coffee_type == "cappuccino":
        check_resources()
        cappuccino()

    if dont_continue is False:
        coins()
        print(f'Total amount is ${user_total}')
        check_amount()
        report()

        print(f"Here is your {coffee_type}. Enjoy!")
    turn_off = input("Type 'off' to turn of the machine or 'buy' again to buy new coffee")
    if turn_off == 'off':
        dont_continue = True