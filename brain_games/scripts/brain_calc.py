#!/usr/bin/env python3
from brain_games.games import calc, greetings


def main():
    print('Welcome to the Brain Games!')
    name = greetings.welcome_user()
    calc.calc_game(name)


if __name__ == '__main__':
    main()
