import prompt


def welcome_user():
    name = prompt.string('May I have you name? ')
    print('Hello, {}!'.format(name))
    return name


def congratulations(n):
    print('Congratulations, {}!'.format(n))


def failure(a, t, n):
    print("{} is wrong answer ;(. Correct answer was {}.\nLet's try again, {}!".format(a, t, n))