from menu_resource import MENU, resources, logo


print(logo)

money: float = 0
resource_sufficient = True


def balance_resources(order):
    """balances used resource to reflect what is left in the machine"""
    flavour = MENU[order]['ingredients']
    for key1 in resources:
        for key2 in flavour:
            if key1 == key2:
                resources[key1] -= flavour[key2]

def coins():
    """collects coins from the user and returns the total amount paid"""
    quarter = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many quarters?: ")) * 0.10
    nickles = float(input("How many quarters?: ")) * 0.05
    pennies = float(input("How many quarters?: ")) * 0.01
    total_coins = quarter + dimes + nickles + pennies
    return total_coins


def process_coins(order):
    """Checks if the coins inserted into the coffee machine is sufficient for the order"""
    global money
    bill = MENU[order]['cost']
    total_coins = coins()
    if bill > total_coins:
        print("Sorry that's not enough money. Money refunded.")
    else:
        # Return balance if any
        balance = total_coins - bill
        print(f"Here is ${balance} in change.\nHere is your {order} ☕️. Enjoy")
        balance_resources(order)
        money += bill


def check_order(order):
    """Takes an order from the user and checks if the resources are sufficient"""
    global resource_sufficient
    resource_sufficient = True
    # Turn off the Coffee Machine by entering “off” to the prompt
    if order == "off":
        print("GOOD BYE!")
        exit()
    # Print report. {resources and finances}
    elif order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
        return False
    else:
        # Check resources sufficient?
        flavour = MENU[order]['ingredients']
        for key1 in resources:
            for key2 in flavour:
                if key1 == key2:
                    if flavour[key2] > resources[key1]:
                        print(f"Sorry there is not enough {key2}")
                        resource_sufficient = False
                        return False
        return True

machine_on = True
while machine_on:
    # Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    order: str = input("What would you like? (espresso/latte/cappuccino): ").lower()



    if check_order(order):
        # Process coins.
        print("Please insert coins.")
        process_coins(order)