import random

RULE = 'What number is missing in the progression?'
START = 1
STOP = 20
LENGTH = 10
progression_start = random.randint(START, STOP)
DIFF_START = 1
DIFF_STOP = 5
diff = random.randint(DIFF_START, DIFF_STOP)
question_position = random.randint(0, LENGTH - 1)


def create_progression():
    progression_stop = progression_start + LENGTH * diff
    return list(range(progression_start, progression_stop, diff))


def get_right_answer_and_question():
    progression = create_progression()
    right_answer = progression[question_position]
    progression[question_position] = '..'
    progression = ' '.join(str(number) for number in progression)
    return (progression, right_answer)
