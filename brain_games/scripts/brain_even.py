#!/usr/bin/env python3
from brain_games.games import even_game, greetings


def main():
    print('Welcome to the Brain Games!')
    name = greetings.welcome_user()
    even_game.even_game(name)


if __name__ == '__main__':
    main()
