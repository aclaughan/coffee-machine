from data import MENU, resources
import logging

logging.basicConfig(level = logging.DEBUG)


def menu():
    selection = show_prompt()
    if selection == 'o':
        print("Turning OFF the machine")
        exit(0)
    elif selection == 'r':
        report()
        menu()
    else:
        prepare(selection)

def header(heading):
    new_string = ''
    for character in heading.upper():
        new_string += character + ' '

    width = len(new_string) + 1
    print(f" {new_string}\n{'-' * width}")

    return new_string

def show_prompt():
    selection = ''
    while selection not in ['e', 'l', 'c', 'o', 'r']:
        header('coffee machine menu')
        print( \
            f" prices:\n\n" \
            f"  espresso {'.' * 20}" \
            f"{'$' + str(MENU['espresso']['cost']):>5}0\n" \
            f"  latte {'.' * 23}" \
            f"{'$' + str(MENU['latte']['cost']):>5}0\n" \
            f"  cappuccino {'.' * 18}" \
            f"{'$' + str(MENU['cappuccino']['cost']):>5}0\n" \
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


def prepare( drink ):
    if drink == 'e':
        ingredients = MENU['espresso']['ingredients']
        fullname = 'espresso'
    elif drink == 'l':
        ingredients = MENU['latte']['ingredients']
        fullname = 'latte'
    else:
        ingredients = MENU['cappuccino']['ingredients']
        fullname = 'cappuccino'

    logging.info(f"ingredients = {ingredients}")
    logging.info(f"resources = {resources}")

    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}" \
                  f"to make a {fullname}.\n\nPlease select something else.")
            return False


def main():
    menu()


if __name__ == '__main__':
    main()

# logging.debug(stuff)
