import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def congratulations(name):
    print('Congratulations, {}!'.format(name))


def failure(answer, total, name):
    print("{} is wrong answer ;(. Correct answer was {}.\nLet's try again, {}!".format(answer, total, name))
