MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 500,
    }
}
print("\tWelcome To CCD")
print("\tMENU")
print("\t1.Espresso - Rs.100")
print("\t1.Latte - Rs.200")
print("\t1.Cappucino - Rs.500")
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True


def is_transaction_successful(money_recieved, drink_cost):
    """Return T when the payment is accepted, F when money is insufficient"""
    if money_recieved >= drink_cost:
        change = int(money_recieved - drink_cost)
        print(f"Here is Rs.{change} in change")
        global profit  # Global is used to access the global varibale locally
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money Refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\tHere is your {drink_name} ☕")


def is_resource_suff(order_ingredients):
    """Returns True when order can be made, False if ingredients are sufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"\tSorry there is not enough {item}.")
            is_enough = False
    return is_enough


def process_money():
    """Returns the total money calculated from notes inserted"""
    print("\tPlease insert notes")
    total = int(input("\tHow many hundreds?: ")) * 100
    total += int(input("\tHow many fifties?: ")) * 50
    total += int(input("\tHow many twenties ?: ")) * 20
    total += int(input("\tHow many tens?: ")) * 10
    return total


while is_on:
    choice = input("\tWhat would you like? (espresso/latte/cappucino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"\tWater: {resources['water']}ml")
        print(f"\tMilk: {resources['milk']}ml")
        print(f"\tCoffee: {resources['coffee']}g")
        print(f"\tMoney: Rs{profit}")
    else:
        drink = MENU[choice]
        if is_resource_suff(drink["ingredients"]):
            payment = process_money()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
