# number guessing game

from random import randint

counter = 0
guess_limit = (5) - 1

print(f"\nWelcome to the guessing game.\n You have {guess_limit + 1} guesses.")
highest_num = int(input(
    "What number would you like the game to go up to? (1 - ?): "))

computer_number = randint(1, highest_num)

while True:
    user_number = int(input("What is your guess: "))

    if user_number == computer_number:
        print(f"You have won. The correct number was {computer_number}.")
        counter += 1
        print(f"It took you {counter} turns to get the correct answer.")
        break
    elif counter == guess_limit:
        print(f"You loose, the number was: {computer_number}!")
        break
    elif user_number != computer_number and user_number > computer_number:
        print(f"Try again, the number is lower.")
        counter += 1
    elif user_number != computer_number and user_number < computer_number:
        print(f"Try again, the number is higher.")
        counter += 1
