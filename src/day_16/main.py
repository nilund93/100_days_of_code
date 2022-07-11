from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    machine = CoffeeMaker()
    money = MoneyMachine()
    
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino/): ")
        if choice in menu.get_items():
            drink = menu.find_drink(choice)
            if machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                machine.make_coffee(drink)
        elif choice == 'report':
            machine.report()
            money.report()
        elif choice == "off":
            print("shutting down")
            break
        else: print("invalid command")
        
    

if __name__ == "__main__":
    main()