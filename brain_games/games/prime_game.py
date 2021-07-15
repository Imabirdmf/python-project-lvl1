import random

rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
#  Position to start and stop for randint method
START = 1
STOP = 100


def is_prime(num):
    if num <= 1:
        return False
    for index in range(2, int(num ** 0.5) + 1):
        if num % index == 0:
            return False
    return True


def get_right_answer():
    num = random.randint(START, STOP)
    question = str(num)
    if is_prime(num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)
