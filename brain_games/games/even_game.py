import random

rule = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
STOP = 1000


def get_right_answer():
    number = random.randint(START, STOP)
    question = str(number)
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)
