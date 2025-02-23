# rock, paper, scissors game

import random

emojis = {'r': '🪨', 'p': '📄', 's': '🔪'}
choices = ['r', 'p', 's']

print("Rock, Paper, Scissors - The Game\n")

while True:
    user_input = input("Rock, Paper, or Scissors? (r, p, s): ").lower()
    if user_input not in choices:
        print("Invalid choice.")
        continue

    comp_input = random.choice(choices)

    print(f"You chose {emojis[user_input]}")
    print(f"Computer chose {emojis[comp_input]}")

    if user_input == comp_input:
        print("It's a draw!")
    elif \
            user_input == 'r' and comp_input == 's' or \
            user_input == 'p' and comp_input == 'r' or \
            user_input == 's' and comp_input == 'p':
        print('You win!')
    else:
        print('You lose!')

    should_continue = input("Do you want to continue? (y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing!")
        break
    elif should_continue == 'y':
        continue
