import random

import prompt
from brain_games.games import greetings


def gcd(name):
    print('Find the greatest common divisor of given numbers.')
    for _ in range(1, 4):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        answer = prompt.string('Question: {} {}\nYour answer: '.format(n1, n2))
        for i in range(1, int(max(n1, n2) // 2) + 1):
            if n1 % i == 0 and n2 % i == 0:
                total = i
        if int(answer) == total:
            print('Correct!')
        else:
            greetings.failure(answer, total, name)
            break
    else:
        greetings.congratulations(name)
