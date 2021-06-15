import prompt


def welcome_user():
    """Welcome user message."""
    name = prompt.string('May I have you name? ')
    print('Hello, {}!'.format(name))
