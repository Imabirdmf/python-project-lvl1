#!/usr/bin/env python3
from brain_games.games import gcd_games, greetings


def main():
    print('Welcome to the Brain Games!')
    name = greetings.welcome_user()
    gcd_games.gcd(name)


if __name__ == '__main__':
    main()
