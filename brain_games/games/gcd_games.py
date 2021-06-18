import random

import prompt
from brain_games.games import greetings


def gcd(name):
    print('Find the greatest common divisor of given numbers.')
    for _ in range(1, 4):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        if number1 % number2 == 0:
            total = number2
            return total
        elif number2 % number1 == 0:
            total = number2
            return total
        for i in range(1, int(number1 ** 0.5) + 1):
            if number1 % i == 0 and number2 % i == 0:
                total = i
        answer = prompt.string('Question: {} {}\nYour answer: '.format(number1, number2))
        if int(answer) == total:
            print('Correct!')
        else:
            greetings.failure(answer, total, name)
            break
    else:
        greetings.congratulations(name)
