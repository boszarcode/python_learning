# dice roller

from random import randint

SIDES = 6
roll_counter = 0
roll_total = 0

SIDES = int(input("How many sides: "))

while True:
    reply = input("Roll? (y/n): ").lower()
    if reply == 'y':
        die1 = randint(1, SIDES)
        die2 = randint(1, SIDES)
        print(f"({die1}, {die2})")
        roll_counter += 1
        roll_total += die1 + die2
        print(f"Roll: {roll_counter}")
        continue
    elif reply == 'n':
        print(f"You rolled {roll_counter} times for a total of {roll_total}.")
        print("Goodbye.")
        break
    else:
        print("Please enter a valid command.")
