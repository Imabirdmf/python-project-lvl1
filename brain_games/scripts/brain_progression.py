#!/usr/bin/env python3
from brain_games.games import progression_game, greetings


def main():
    print('Welcome to the Brain Games!')
    name = greetings.welcome_user()
    progression_game.progression_game(name)


if __name__ == '__main__':
    main()
