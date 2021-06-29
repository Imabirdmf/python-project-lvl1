import random

rule = 'What is the result of the expression?'
left_border = 1
right_border = 100


def calculation():
    num1 = random.randint(left_border, right_border)
    num2 = random.randint(left_border, right_border)
    operator = random.choice('+-*')
    question = 'Question: {0} {1} {2}'.format(num1, operator, num2)
    if operator == '-':
        total = num1 - num2
    elif operator == '+':
        total = num1 + num2
    elif operator == '*':
        total = num1 * num2
    return (question, total)
