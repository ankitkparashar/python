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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_in_machine = 0


def count_money():
    coin_values = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}
    money_entered = 0
    print("Please insert coins.")
    for coin in coin_values:
        num_of_coins = int(input(f"How many {coin}?: "))
        money_entered += num_of_coins * coin_values[coin]
    return money_entered


def make_the_drink(resources_needed, choice_entered):
    global MENU
    for ingredient in MENU[choice_entered]["ingredients"]:
        resources_needed[ingredient] -= MENU[choice_entered]["ingredients"][ingredient]
    print(f"Enjoy your {choice_entered}!")
    return


def drink_is_possible(resources_needed, choice_entered):
    global MENU
    for ingredient in MENU[choice_entered]["ingredients"]:
        if resources_needed[ingredient] < MENU[choice_entered]["ingredients"][ingredient]:
            print(f"Sorry there's not enough {ingredient}. Money refunded.")
            return False
    return True


def print_resources_report(resources_remaining):
    for key in resources_remaining:
        print(f"{key.title()}: {resources_remaining[key]} " + ("g" if key == "coffee" else "ml"))


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in MENU:
        money_provided = count_money()
        cost_of_drink = MENU[choice]['cost']
        if money_provided < cost_of_drink:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if drink_is_possible(resources, choice):
                make_the_drink(resources, choice)
                if money_provided > cost_of_drink:
                    print(f"Here's your change: ${round(money_provided - cost_of_drink, 2)}")
                money_in_machine += cost_of_drink
    elif choice == "report":
        print_resources_report(resources)
        print(f"Money: ${money_in_machine}")
    elif choice == "off":
        machine_on = False
    else:
        print("Invalid choice. Please enter from the given options.")
