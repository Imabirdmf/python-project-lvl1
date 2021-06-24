import random

import prompt
from brain_games.games import greetings


def calc_game(name):
    print('What is the result of the expression?')
    for _ in range(1, 4):
        n1 = random.randint(1, 1000)
        n2 = random.randint(1, 1000)
        op = random.choice('+-*')
        print('Question: {} {} {}'.format(n1, op, n2))
        answer = prompt.string('Your answer: ')
        if op == '-':
            total = n1 - n2
        elif op == '+':
            total = n1 + n2
        elif op == '*':
            total = n1 * n2
        if int(answer) == total:
            print('Correct!')
        else:
            greetings.failure(answer, total, name)
            break  # Здесь потом можно возвращать значение
    else:
        greetings.congratulations(name)  # Здесь потом можно возвращать значение
