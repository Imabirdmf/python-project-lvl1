import random

import prompt
from brain_games.games import greetings


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(1, 4):
        number = random.randint(1, 1000)
        answer = prompt.string('Question: {}\nYour answer: '.format(number))
        if number % 2 == 0 and answer == 'yes':
            total = 'yes'
        elif number % 2 != 0 and answer == 'no':
            total = 'no'
        if answer == total:
            print('Correct!')
        else:
            greetings.failure(answer, total, name)
            break  # Здесь потом можно возвращать значение
    else:
        greetings.congratulations(name)  # Здесь потом можно возвращать значение
