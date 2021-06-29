import random

rule = 'Answer "yes" if the number is even, otherwise answer "no".'
left_border = 1
right_border = 1000


def calculation():
    number = random.randint(left_border, right_border)
    question = 'Question: {0}'.format(number)
    if number % 2 == 0:
        total = 'yes'
    elif number % 2 != 0:
        total = 'no'
    return (question, total)
