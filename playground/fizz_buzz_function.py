first_number = int(input('First number: '))
second_number = int(input('First number: '))


def game(num1, num2):
    for i in range(num1, num2):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


game(first_number, second_number)
