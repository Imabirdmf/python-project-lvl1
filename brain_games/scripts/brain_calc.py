#!/usr/bin/env python3
from brain_games.games import calc, engine, greetings


def main():
    print('Welcome to the Brain Games!')
    name = greetings.welcome_user()
    engine.game_circle(name, calc)


if __name__ == '__main__':
    main()
