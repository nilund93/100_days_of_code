# Day 15
# Create a coffee machine program


# PROVIDED CODE
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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# MY CODE
MONEY = 0

def buy_drink(choice):
    global MONEY
    # gå igenom alla resurser för brygden
    for key in MENU[choice]['ingredients'].keys():
        if RESOURCES[key] >= MENU[choice]['ingredients'][key]:
            continue
        else:
            print(f"Sorry there is not enough {key}.")
            break
    else:
        # låt köpet gå igenom
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        
        if total >= MENU[choice]['cost']:
            cost = total - MENU[choice]['cost']
            MONEY += cost
            print(f"Here is ${cost:.2f} in change.")
            print(f"Here is your {choice}. Enjoy!")
            for key in MENU[choice]['ingredients'].keys():
                RESOURCES[key] -= MENU[choice]['ingredients'][key]
        else:
            print("Sorry that's not enough money. Money refunded.")

def report():
    print(f"Water: {RESOURCES['water']}ml")
    print(f"Milk: {RESOURCES['milk']}ml")
    print(f"Coffee: {RESOURCES['coffee']}g")
    print(f"Money: ${MONEY:.2f}")

def main():
    while True:
        while True:
            print("What would you like? (espresso/latte/cappuccino)")
            choice = input(">> ")
            if choice in ["espresso", "latte", "cappuccino"]: buy_drink(choice)
            elif choice == "report": report()
            elif choice == "off": 
                print("shutting down")
                exit()
            else: print("invalid command")
        

if __name__ == "__main__":
    main()
