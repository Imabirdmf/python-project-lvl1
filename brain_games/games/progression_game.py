import random

rule = 'What number is missing in the progression?'
#  Position to start and stop
START = 1
STOP = 20
LENGTH = 10


def create_progression():
    progression_start = random.randint(START, STOP)
    diff = random.randint(1, 5)
    progression_stop = progression_start + LENGTH * diff
    return list(range(progression_start, progression_stop, diff))


def get_right_answer():
    position = random.randint(0, LENGTH - 1)
    progression = create_progression()
    right_answer = progression[position]
    progression[position] = '..'
    progression = ' '.join(str(number) for number in progression)
    return ('{0}'.format(progression), right_answer)
