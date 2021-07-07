#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import prime_game


def main():
    print('Welcome to the Brain Games!')
    engine.is_right_answer(prime_game)


if __name__ == '__main__':
    main()
