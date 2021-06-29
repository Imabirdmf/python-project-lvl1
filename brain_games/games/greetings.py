import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def congratulations(name):
    print('Congratulations, {0}!'.format(name))


def failure(answer, total, name):
    print("'{0}' is wrong answer ;(.".format(answer), end=' ')
    print("Correct answer was '{0}'.".format(total))
    print("Let's try again, {0}!".format(name))
