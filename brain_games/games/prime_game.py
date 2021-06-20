import random

import prompt
from brain_games.games import greetings


def is_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(1, 4):
        num = random.randint(1, 100)
        flag = True
        for i in range(2, num ** 0.5 + 1):
            if num % i == 0:
                flag = False
        if num > 1 and flag is True:
            total = 'yes'
        else:
            total = 'no'
        answer = prompt.string('Question: {}\nYour answer: '.format(num))
        if int(answer) == total:
            print('Correct!')
        else:
            greetings.failure(answer, total, name)
            break  # Здесь потом можно возвращать значение
    else:
        greetings.congratulations(name)  # Здесь потом можно возвращать значение
