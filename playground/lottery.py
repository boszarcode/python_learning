# lottery program to select numbers

from random import randint

MAX_BALLS = 49  # constant for max numbers of lottery balls
TICKET_BALLS = 8


def lottery_numbers():
    numbers = []
    count = 0

    while count < TICKET_BALLS:
        number = randint(1, MAX_BALLS)
        if number in numbers:
            count += 0
        else:
            numbers.append(number)
            count += 1

    print("Your lottery numbers are:")
    print(*numbers)


lottery_numbers()
