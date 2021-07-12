import random

rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
#  Position to start and stop for randint method
START = 1
STOP = 100


def is_prime(num):
    flag = True
    for index in range(2, int(num ** 0.5) + 1):
        if num % index == 0:
            flag = False
            break
    return flag


def get_right_answer():
    num = random.randint(START, STOP)
    question = str(num)
    flag = is_prime(num)
    if num > 1 and flag is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)
