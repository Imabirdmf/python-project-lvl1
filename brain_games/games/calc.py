import random

import prompt


from brain_games.games import greetings


def calc_game(name):
    print('What is the result of the expression?')
    for _ in range(1, 4):
        number1 = random.randint(1, 1000)
        number2 = random.randint(1, 1000)
        operation = random.choice('+-*')
        answer = prompt.string('Question: {} {} {}\nYour answer: '.format(number1, operation, number2))
        if operation == '-':
            total = number1 - number2
        elif operation == '+':
            total = number1 + number2
        elif operation == '*':
            total = number1 * number2
        if answer == total:
            print('Correct!')
        else:
            greetings.failure(answer, total, name)
            break  # Здесь потом можно возвращать значение
    else:
        greetings.congratulations(name)  # Здесь потом можно возвращать значение
