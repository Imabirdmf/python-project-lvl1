import random

RULE = 'What is the result of the expression?'
START = 1
STOP = 100


def get_right_answer_and_question():
    num1 = random.randint(START, STOP)
    num2 = random.randint(START, STOP)
    operator = random.choice('+-*')
    question = '{0} {1} {2}'.format(num1, operator, num2)
    if operator == '-':
        right_answer = num1 - num2
    elif operator == '+':
        right_answer = num1 + num2
    elif operator == '*':
        right_answer = num1 * num2
    return (question, right_answer)
