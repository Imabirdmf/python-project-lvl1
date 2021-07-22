import random

RULE = 'Find the greatest common divisor of given numbers.'
START = 1
STOP = 100


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2


def get_right_answer_and_question():
    num1 = random.randint(START, STOP)
    num2 = random.randint(START, STOP)
    question = '{0} {1}'.format(num1, num2)
    right_answer = get_gcd(num1, num2)
    return (question, right_answer)
