import random

rule = 'Find the greatest common divisor of given numbers.'
l_border = 1
r_border = 100


def calculate():
    num1 = random.randint(l_border, r_border)
    num2 = random.randint(l_border, r_border)
    question = 'Question: {0} {1}'.format(num1, num2)
    for index in range(1, (min(num1, num2)) + 1):
        if num1 % index == 0 and num2 % index == 0:
            total = index
    return (question, total)
