import random

rule = 'What number is missing in the progression?'
l_border = 1
r_border = 20
progression_len = r_border // 2


def calculate():
    # выбирается шаг прогрессии
    number = random.randint(1, 6)
    # выбирается случайная первая цифра прогрессии
    progression = [random.randint(l_border, r_border)]
    # выбирается случайная позиция не больше длины прогрессии
    position = random.randint(0, progression_len)
    # длина прогрессии (не задаётся случайно, зависит от правой границы)
    for index in range(1, progression_len + 1):
        progression.append(progression[index - 1] + number)
    total = progression[position]
    progression.insert(position, '..')
    progression.pop(position + 1)
    progression = ' '.join(str(number) for number in progression)
    return (progression, total)
