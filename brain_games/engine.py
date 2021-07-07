import prompt

GAME_CIRCLE_FROM = 1
GAME_CIRCLE_TO = 4


def is_right_answer(game):
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game.rule)
    for _ in range(GAME_CIRCLE_FROM, GAME_CIRCLE_TO):
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