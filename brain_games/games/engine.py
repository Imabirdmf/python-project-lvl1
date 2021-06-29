import prompt
from brain_games.games import greetings


def game_circle(name, game):
    print(game.rule)
    for _ in range(1, 4):
        question_and_total = game.calculation()
        (question, total) = question_and_total
        print(question)
        answer = prompt.string('Your answer: ')
        if int(answer) == total:
            print('Correct!')
        else:
            greetings.failure(answer, total, name)
            break
    else:
        greetings.congratulations(name)
