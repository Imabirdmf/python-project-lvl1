import prompt
import random


def welcome_user():
    name = prompt.string('May I have you name? ')
    print('Hello, {}!'.format(name))
    return name


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(1, 4):
        number = random.randint(1, 1000)
        answer = prompt.string('Question: {}\nYour answer: '.format(number))
        if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {}!".format(name))
            break  # Здесь потом можно возвращать значение
    else:
        print('Congratulations, {}!'.format(name))  # Здесь потом можно возвращать значение
