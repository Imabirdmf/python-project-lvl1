import random

rule = 'What is the result of the expression?'
l_border = 1
r_border = 100


def calculate():
    num1 = random.randint(l_border, r_border)
    num2 = random.randint(l_border, r_border)
    operator = random.choice('+-*')
    question = 'Question: {0} {1} {2}'.format(num1, operator, num2)
    if operator == '-':
        total = num1 - num2
    elif operator == '+':
        total = num1 + num2
    elif operator == '*':
        total = num1 * num2
    return (question, total)
