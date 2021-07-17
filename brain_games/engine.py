import prompt

ITERATION = 3


def is_right_answer(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game.RULE)
    for _ in range(ITERATION):
        question, right_answer = game.get_right_answer()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == str(right_answer):
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(.".format(answer), end=' ')
            print("Correct answer was '{0}'.".format(right_answer))
            print("Let's try again, {0}!".format(name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
