from data import MENU, resources
from art import cup
import logging

#logging.basicConfig(level = logging.DEBUG)


def menu():
    selection = show_prompt()
    selection = expand_selection(selection)

    if selection == 'off':
        print("Turning OFF the machine")
        exit(0)
    elif selection == 'report':
        report()
        menu()
    else:
        if not resources_available(selection):
            menu()

    change = collect_coins(selection)
    if change:
        print(f"Here is your ${change:0.2f} change")

    make_the_coffee(selection)
    menu()


def header( heading ):
    new_string = ''
    for character in heading.upper():
        new_string += character + ' '

    width = len(new_string) + 1
    print(f" {new_string}\n{'-' * width}")

    return new_string


def expand_selection( selection ):
    expanded = {
        'e': 'espresso',
        'l': 'latte',
        'c': 'cappuccino',
        'o': 'off',
        'r': 'report'
    }

    return expanded[selection]


def show_prompt():
    selection = ''
    while selection not in ['e', 'l', 'c', 'o', 'r']:
        header('coffee machine menu')
        print( \
            f" prices:\n\n" \
            f"  espresso {'.' * 21}" \
            f" ${MENU['espresso']['cost']:>1.2f}\n" \
            f"  latte {'.' * 24}" \
            f" ${MENU['latte']['cost']:>1.2f}\n" \
            f"  cappuccino {'.' * 19}" \
            f" ${MENU['cappuccino']['cost']:>0.2f}\n" \
            )
        selection = input( \
            "What would you like? (espresso/latte/cappuccino):\n  > "
        ).lower()[:1]

    return selection


def report():
    header('coffee machine report')
    print( \
        f" resources available:\n\n" \
        f"  water {'.' * 23}{resources['water']:>5}ml\n" \
        f"  milk {'.' * 24}{resources['milk']:>5}ml\n" \
        f"  coffee {'.' * 22}{resources['coffee']:>5}g\n" \
        f"  money {'.' * 23} {'$' + str(resources['money']):>5}\n"
    )


def resources_available( drink ):
    ingredients = MENU[drink]['ingredients']

    logging.info(f"ingredients = {ingredients}")
    logging.info(f"resources = {resources}")

    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}" \
                  f"to make a {drink}.\n\nPlease select something else.")
            return False
    return True


def collect_coins( selection ):
    cost = MENU[selection]['cost']
    coins = \
        [
            { "name": "quarters", "value": 25 },
            { "name": "dimes", "value": 10 },
            { "name": "nickles", "value": 5 },
            { "name": "pennies", "value": 1 }
        ]
    print(f"a {selection} costs {cost}\nPlease insert some coins.")

    coins_total = 0

    while True:
        for coin in range(len(coins)):
            received = int(
                input(f"{cost - coins_total:>5.2f}: How many {coins[coin]['name']}? "))

            coins_total += (coins[coin]['value'] / 100) * received
            logging.info(
                f"\nreceived = {received}\ncost = {cost}\ncoins_total = {coins_total}")
            if int(coins_total*100) >= int(cost*100):
                return coins_total - cost

def make_the_coffee(selection):
    print(f"creating a fresh {selection} masterpiece.")
    info = MENU[selection]
    for ingredient in info['ingredients']:
        resources[ingredient] -= info['ingredients'][ingredient]
    resources['money'] += info['cost']
    print(f"\n{cup}\nEnjoy your coffee and have a great day\n")





def main():
    menu()


if __name__ == '__main__':
    main()

# logging.debug(stuff)
