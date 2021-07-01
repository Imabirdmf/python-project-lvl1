import random

rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
l_border = 1
r_border = 100


def calculate():
    num = random.randint(l_border, r_border)
    question = 'Question: {0}'.format(num)
    flag = True
    for index in range(2, int(num ** 0.5) + 1):
        if num % index == 0:
            flag = False
            break
    if num > 1 and flag is True:
        total = 'yes'
    else:
        total = 'no'
    return (question, total)
