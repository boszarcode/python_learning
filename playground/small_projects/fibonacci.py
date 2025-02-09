# fibonacci calculator to x amount of places

import sys

sys.set_int_max_str_digits(50000)

second = int(input("Fibonacci how many times? >> "))


def fib_seq(second):
    a = 0
    b = 1
    c = 0

    print(b)

    for x in range(1, second):
        print(a + b)
        print('')
        c = a + b
        a = b
        b = c
    return


fib_seq(second)
