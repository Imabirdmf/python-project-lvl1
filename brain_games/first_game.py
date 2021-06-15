import prompt
import random


def welcome_user():
    name = prompt.string('May I have you name? ')
    print('Hello, {}!'.format(name))


def even_game():
    i = 0
    while i < 3:
        number = random.randint(1, 101)
        answer = prompt.string('Answer "yes" if the number is even, otherwise answer "no". \nQuestion: {}'.format(number))
        if (number % 2 == 0 and answer == 'yes') or (number % 2 !=0 and answer == 'no'):
            print('Correct!')
            i += 1
        else:
            return "'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {}!".format(name)
    return 'Congratulations, {}!'.format(name)