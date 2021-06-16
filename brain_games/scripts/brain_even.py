#!/usr/bin/env python3


from brain_games import first_game


def main():
    print('Welcome to the Brain Games!')
    name = first_game.welcome_user()
    first_game.even_game(name)


if __name__ == '__main__':
    main()
