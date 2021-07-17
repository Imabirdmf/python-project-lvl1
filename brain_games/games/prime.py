import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
STOP = 100


def is_prime(num):
    if num <= 1:
        return False
    for number in range(2, int(num ** 0.5) + 1):
        if num % number == 0:
            return False
    return True


def get_right_answer_and_question():
    num = random.randint(START, STOP)
    question = str(num)
    if is_prime(num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)
