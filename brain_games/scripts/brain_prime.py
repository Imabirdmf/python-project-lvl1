#!/usr/bin/env python3
from brain_games.games import greetings, prime_game


def main():
    print('Welcome to the Brain Games!')
    name = greetings.welcome_user()
    prime_game.is_prime(name)


if __name__ == '__main__':
    main()
