# Coffee Machine Program

#TODO: 1. Data

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

profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on =True


#TODO: 2. Define Functions


"""Returns True when order can be made, False if ingredients are insufficient"""

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"Sorry there is not enough {item}.")
           is_enough = False
    return True

"""Returns the total calculated from coins inserted"""

def process_coins():
    print("Please insert coins.")
    total = float(input("howmany quarters?: ")) * 0.25
    total += float(input("how many dime?: ")) * 0.1
    total += float(input("how many nickles?: ")) * 0.05
    return total

"""Return True when payment is accepted, or False is money is sufficient"""
def is_transaction_successfull(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


"""Make coffee by deducting the required ingredients resources."""

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")



# TODO: 2. Actuall program

choice = input("What would you like to have? (espresso/latte/cappuccino): ")
if choice == "off":
    is_on = False
elif choice == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee powder: {resources['coffee']}g")
    print(f"Money: ${profit}")
else:
    drink = MENU[choice]
    print(drink)
    if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        if is_transaction_successfull(payment, drink["cost"]):
            make_coffee(choice, drink["ingredients"])



