import random

rule = 'Find the greatest common divisor of given numbers.'
#  Position to start and stop for randint method
START = 1
STOP = 100


def get_gcd(num1, num2):
    min_num = min(num1, num2)
    for index in range(1, (min_num + 1)):
        if num1 % index == 0 and num2 % index == 0:
            right_answer = index
    return right_answer


def get_right_answer():
    num1 = random.randint(START, STOP)
    num2 = random.randint(START, STOP)
    question = '{0} {1}'.format(num1, num2)
    right_answer = get_gcd(num1, num2)
    return (question, right_answer)
