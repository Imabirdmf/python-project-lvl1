import random

rule = 'Find the greatest common divisor of given numbers.'
#  Position to start and stop for randint method
START = 1
STOP = 100


def get_gcd(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    while max_num != 0 and min_num != 0:
        q = max_num % min_num
        if q == 0:
            right_answer = min_num
            break
        max_num = min_num
        min_num = q
    return right_answer


def get_right_answer():
    num1 = random.randint(START, STOP)
    num2 = random.randint(START, STOP)
    question = '{0} {1}'.format(num1, num2)
    right_answer = get_gcd(num1, num2)
    return (question, right_answer)
