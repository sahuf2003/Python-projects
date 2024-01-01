MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

pantry = {
    "water": 500,
    "milk": 500,
    "coffee": 100,
    "money": 0
}


def resource():
    print(f"Water: {pantry['water']}ml, Milk: {pantry['milk']}ml, Coffee: {pantry['coffee']}ml, Money: {pantry['money']}$")


def compare(coffee):
    if pantry["water"] >= coffee['water'] and pantry['coffee'] >= coffee['coffee'] and pantry['milk'] >= coffee['milk']:
        return True
    else:
        return False


def price():
    Quater = int(input("Quater is 0.25: "))
    Dimes = int(input("Dimes is 0.10: "))
    Nickel = int(input("Nicker is 0.05: "))
    pennies = int(input("Pennies is 0.01: "))
    amount = (Quater * 0.25) + (Dimes * 0.10) + (Nickel * 0.05) + (pennies * 0.01)
    return amount


def transaction(choice):
    user_amount = price()
    if user_amount >= MENU[choice]['cost']:
        change = user_amount - MENU[choice]['cost']
        print(f"Your change is here is {change}")
        pantry['money'] += MENU[choice]['cost']
        return True
    else:
        print("Not enough money")
        return False


def decrement(choice):
    pantry['water'] -= MENU[choice]['ingredients']['water']
    pantry['milk'] -= MENU[choice]['ingredients']['milk']
    pantry['coffee'] -= MENU[choice]['ingredients']['coffee']
    return pantry


def order():
    is_on = True
    while is_on:
        user_choice = input("What would you like to have (espresso/cappuccino/latte) or 'report': ")
        if user_choice == "off":
            is_on = False
        elif user_choice == 'report':
            resource()
        elif user_choice in MENU:
            if compare(MENU[user_choice]["ingredients"]):
                if transaction(user_choice):
                    decrement(user_choice)
                    print("Here is your", user_choice)
            else:
                print("Not Enough resources available")
        else:
            print("Invalid choice")


order()
