import random

import prompt
from brain_games.games import greetings


def progression_game(name):
    print('What number is missing in the progression?')
    for _ in range(1, 4):
        n = random.randint(1, 5)
        pos = random.randint(1, 10)
        progression = [random.randint(1, 15)]
        s = str(progression[0]) + ' '
        for i in range(1, 11):
            progression.append(progression[i - 1] + n)
            s = s + str(progression[i]) + ' '
            if i == pos:
                s = s.replace(str(progression[i]), '..')
        answer = prompt.string('Question: {}\nYour answer: '.format(s.rstrip()))
        total = progression[pos]
        if int(answer) == total:
            print('Correct!')
        else:
            greetings.failure(answer, total, name)
            break  # Здесь потом можно возвращать значение
    else:
        greetings.congratulations(name)  # Здесь потом можно возвращать значение
