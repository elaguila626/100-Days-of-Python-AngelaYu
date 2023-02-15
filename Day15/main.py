MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

#Is there a better way of accessing a dictionary within a dictionary?
#Is there an easier way to change a global number than appending a number inside a function to an empty list

coffee_gains = [0]
user_sum = [0]
price = [0]

espresso_drink = MENU['espresso']
latte_drink = MENU['latte']
cappuccino_drink = MENU['cappuccino']

espresso_ingredients = espresso_drink['ingredients']
latte_ingredients = latte_drink['ingredients']
cappuccino_ingredients = cappuccino_drink['ingredients']

espresso_cost = espresso_drink['cost']
latte_cost = latte_drink['cost']
cappuccino_cost = cappuccino_drink['cost']

def report(inquiry):
    if inquiry == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print (f"coffee: {resources['coffee']}g")
        print(f"money: ${coffee_gains[0]}")

def selection(coffee_type):
    if coffee_type == 'espresso':
        reduce_water = float(espresso_ingredients['water'])
        reduce_milk = float(espresso_ingredients['milk'])
        reduce_coffee = float(espresso_ingredients['coffee'])
        reduce_resources(reduce_water, reduce_milk, reduce_coffee)
    elif coffee_type == 'latte':
        reduce_water = float(latte_ingredients['water'])
        reduce_milk = float(latte_ingredients['milk'])
        reduce_coffee = float(latte_ingredients['coffee'])
        reduce_resources(reduce_water, reduce_milk, reduce_coffee)
    elif coffee_type == 'cappuccino':
        reduce_water = float(cappuccino_ingredients['water'])
        reduce_milk = float(cappuccino_ingredients['milk'])
        reduce_coffee = float(cappuccino_ingredients['coffee'])
        reduce_resources(reduce_water, reduce_milk, reduce_coffee)

def reduce_resources(reduced_water, reduced_milk, reduced_coffee):
    resources['water'] -= reduced_water
    resources['milk'] -= reduced_milk
    resources['coffee'] -= reduced_coffee
    #print(f"{resources['water']}, {resources['milk']}, {resources['coffee']}")

def sum_coins(user_q, user_d, user_n, user_p):
    quarter = 0.25
    total_quarters = quarter * user_q
    dime = 0.10
    total_dimes = dime * user_d
    nickle = 0.05
    total_nickles = nickle * user_n
    penny = 0.01
    total_pennies = penny * user_p
    total_sum = float(total_quarters + total_dimes + total_nickles + total_pennies)
    #print(f"Here's the user's total sum {total_sum}")
    user_sum[0] = total_sum

def ask_user_coins():
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input ("How many nickles? "))
    pennies = float(input("How many pennies? "))

    sum_coins(quarters, dimes, nickles, pennies)

def change(order_cost):
    if order_cost == 'espresso':
        price[0] = espresso_cost
        order_cost = espresso_cost
        if final_sum < order_cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            user_change = final_sum - order_cost
            coffee_gains[0] += order_cost
            print("Enjoy your espresso! ☕️")
            print(f"Here's your change ${round(user_change,2)}.")
    elif order_cost == 'latte':
        price[0] = latte_cost
        order_cost = latte_cost
        if final_sum < order_cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            user_change = final_sum - order_cost
            coffee_gains[0] += order_cost
            print("Enjoy your latte! ☕️")
            print(f"Here's your change ${round(user_change,2)}.")
    elif order_cost == 'cappuccino':
        price[0] = cappuccino_cost
        order_cost = cappuccino_cost
        if final_sum < order_cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            user_change = final_sum - order_cost
            coffee_gains[0] += order_cost
            print("Enjoy your cappuccino! ☕️")
            print(f"Here's your change ${round(user_change,2)}.")

# ask_user_coins()
# final_sum = user_sum[0]
# change(user_selects_coffee)
purchasing_coffee = True

while purchasing_coffee:
    user_selects_coffee = input("What would you like? (espresso/latte/cappuccino)? ")
    #print(f"This is the monetary gains: {coffee_gains[0]}")
    if user_selects_coffee == 'report':
        report(user_selects_coffee)
    elif user_selects_coffee == 'stop':
        purchasing_coffee = False
    elif resources['water'] > 100 and resources['milk'] > 0 and resources['coffee'] > 18:
        ask_user_coins()
        final_sum = user_sum[0]
        change(user_selects_coffee)
        if final_sum >= price[0]:
            selection(user_selects_coffee)
    else:
        print("Sorry insufficient resources.")
        purchasing_coffee = False

