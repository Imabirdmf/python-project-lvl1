import random

rule = 'Find the greatest common divisor of given numbers.'
left_border = 1
right_border = 100


def calculation():
    num1 = random.randint(left_border, right_border)
    num2 = random.randint(left_border, right_border)
    question = 'Question: {0} {1}'.format(num1, num2)
    for index in range(1, (max(num1, num2) // 2) + 1):
        if num1 % index == 0 and num2 % index == 0:
            total = index
        if index > min(num1, num2):
            break
    return (question, total)
