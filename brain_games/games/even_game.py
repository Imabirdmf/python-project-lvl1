import random

rule = 'Answer "yes" if the number is even, otherwise answer "no".'
l_border = 1
r_border = 1000


def calculate():
    number = random.randint(l_border, r_border)
    question = 'Question: {0}'.format(number)
    if number % 2 == 0:
        total = 'yes'
    elif number % 2 != 0:
        total = 'no'
    return (question, total)
