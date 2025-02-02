# dice roller app with roll amount and dice sides

from random import randint


def get_sides():
    while True:
        dice_sides = input('How many sides would you like for your dice? ')
        if dice_sides.isdigit():
            dice_sides = int(dice_sides)
            break
        else:
            print('Please choose a number.')
    return dice_sides


def get_rolls():
    while True:
        dice_rolls = input('How many times do you want to roll? ')
        if dice_rolls.isdigit():
            dice_rolls = int(dice_rolls)
            break
        else:
            print('Please choose a number.')
    return dice_rolls


def main():
    sides = get_sides()
    rolls = get_rolls()
    dice = []

    for i in range(1, rolls):
        dice.append(randint(1, sides))

    print(f"You have rolled:")
    print(*dice, sep=', ')


main()
