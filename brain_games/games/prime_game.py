import random

rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
left_border = 1
right_border = 100


def calculation():
    num = random.randint(1, 100)
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
